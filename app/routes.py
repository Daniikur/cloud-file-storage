from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session # type: ignore
from datetime import datetime

from .models import FileMetadata  # Ensure this model exists
from .schemas import FileMetadataCreate  # Ensure correct import
from .utils import upload_file_to_s3, download_file_from_s3
from config import Config  # Ensure config.py exists and has DATABASE_URL

from sqlalchemy import create_engine # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore

# Database setup
DATABASE_URL = Config.DATABASE_URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define API Router
api_router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@api_router.post("/upload")
async def upload_file(file: UploadFile = File(...), user_id: int = None, db: Session = Depends(get_db)):
    if not user_id:
        raise HTTPException(status_code=400, detail="User ID is required")

    if upload_file_to_s3(file.file, file.filename):
        new_file = FileMetadata(filename=file.filename, filepath=file.filename, user_id=user_id, uploaded_at=datetime.utcnow())
        db.add(new_file)
        db.commit()
        db.refresh(new_file)
        return {"message": "File uploaded successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to upload file")

@api_router.get("/download/{filename}")
async def download_file(filename: str):
    file_stream = download_file_from_s3(filename)
    if file_stream:
        return file_stream
    else:
        raise HTTPException(status_code=404, detail="File not found")
