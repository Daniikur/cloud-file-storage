from fastapi import FastAPI
from app.routes import api_router  # ✅ Correct import
from dotenv import load_dotenv # type: ignore
import os

# Load environment variables from .env file
load_dotenv()

# Get environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))

# Create FastAPI instance
app = FastAPI(
    title="Cloud File Storage API",
    description="An API for uploading and managing files in cloud storage",
    version="1.0.0",
)

# ✅ Add root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Cloud File Storage API"}

# ✅ Include the router
app.include_router(api_router)

# Run FastAPI with Uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host=HOST,
        port=PORT,
        reload=True  # Remove in production for better performance
    )
