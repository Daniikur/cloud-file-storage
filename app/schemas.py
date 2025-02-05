from pydantic import BaseModel
from datetime import datetime

class FileMetadataBase(BaseModel):
    filename: str
    filepath: str
    user_id: int

class FileMetadataCreate(FileMetadataBase):
    pass

class FileMetadata(FileMetadataBase):
    id: int
    uploaded_at: datetime

    class Config:
        from_attributes = True