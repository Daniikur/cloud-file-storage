# 💁 Cloud File Storage API

A FastAPI-based backend service for uploading, storing, and managing files in cloud storage. Supports AWS S3 for file storage and PostgreSQL for metadata management.

## 🚀 Features
- Upload files to AWS S3
- Download files from AWS S3
- Store file metadata in PostgreSQL
- RESTful API with FastAPI
- Dockerized environment for easy deployment

---

## 🛠️ Setup and Installation

### **1️⃣ Clone the Repository**
```sh
git clone   https://github.com/Daniikur/cloud-file-storage.git
cd cloud-file-storage
```

### **2️⃣ Setup Environment Variables**
Create a `.env` file in the project root and add the required environment variables:
```env
DATABASE_URL=postgresql://user:password@db:5432/cloud_storage
SECRET_KEY=your_secret_key
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
S3_BUCKET_NAME=your_bucket_name
```

### **3️⃣ Start the Application with Docker**
Ensure you have **Docker** and **Docker Compose** installed. Then, run:
```sh
docker-compose up --build
```

This will start the FastAPI app, PostgreSQL database, and **pgAdmin 4**.

---

## 📊 Managing the Database with pgAdmin 4

pgAdmin 4 is included in the **Docker Compose** setup for database management.

### **Access pgAdmin 4**
1. Open your browser and go to:  
   **[http://localhost:5050](http://localhost:5050)**
2. Login using:
   - **Email:** `admin@admin.com`
   - **Password:** `password`
   
### **Connect to PostgreSQL**
1. Click **Add New Server**.
2. Under the **General** tab:
   - Name: `Cloud Storage DB`
3. Under the **Connection** tab:
   - Hostname: `db`
   - Port: `5432`
   - Username: `user`
   - Password: `password`
4. Click **Save**.

Now you can manage your PostgreSQL database through pgAdmin 4.

---

## 📌 API Endpoints

### **📄 Upload a File**
```sh
curl -X 'POST' \
  'http://localhost:8000/upload' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@yourfile.txt'
```

### **📂 Download a File**
```sh
curl -X 'GET' \
  'http://localhost:8000/download/yourfile.txt' \
  -H 'accept: application/json'
```

---

## 🏢 Deployment

For production deployment:
```sh
docker-compose -f docker-compose.prod.yml up --build -d
```

---

## 🛠️ Technologies Used
- **FastAPI** - Backend API framework
- **PostgreSQL** - Database for metadata storage
- **AWS S3** - Cloud file storage
- **Docker & Docker Compose** - Containerized environment
- **pgAdmin 4** - Database management

---

