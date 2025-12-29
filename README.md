CRM Backend API

A production-ready CRM Backend API built using FastAPI, SQLAlchemy, and JWT Authentication.
This project demonstrates clean architecture, authentication, authorization, and advanced CRUD operations.

**Tech Stack**
Backend Framework: FastAPI
Language: Python 3.10.6
Database: SQLite
ORM: SQLAlchemy
Authentication: JWT (JSON Web Tokens)
Password Hashing: bcrypt (passlib)
API Docs: Swagger UI

**Project Structure**
backend-crm-api/
│
├── app/
│   ├── auth/
│   │   ├── auth_router.py
│   │   ├── auth_schema.py
│   │   ├── auth_service.py
│   │   ├── auth_utils.py
│   │   └── jwt_dependency.py
│   │
│   ├── database/
│   │   ├── database.py
│   │   └── models.py
│   │
│   ├── routers/
│   │   └── users.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   └── response.py
│   │
│   ├── services/
│   │   └── user_service.py
│   │
│   └── main.py
│
└── crm.db

**Authentication Flow**
Register User
Password is hashed using bcrypt
Login User
JWT access token is generated
Secure APIs
Protected routes require Authorization: Bearer <token>

**Features Implemented**
✅ Authentication
User registration
User login
Password hashing
JWT token generation & validation

✅ User Management (CRUD)
Create user
List users (with filters)
Get user by ID
Update user
Delete user

**Advanced API Features**
Filtering (name, age range)
Sorting (by id, name, age)
Pagination (skip & limit)
Centralized error handling
Consistent API response format

**API Documentation**
Once the server is running, access Swagger UI:
http://127.0.0.1:8000/docs

**Setup & Run Locally**
1️⃣ Clone the repository
git clone <your-repo-url>
cd backend-crm-api

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose

4️⃣ Run the server
uvicorn app.main:app --reload

**Database**
SQLite database (crm.db)
Tables auto-created on startup

**Future Enhancements (Planned)**
Role-based access control (Admin/User)
Refresh tokens
Docker support
PostgreSQL integration
Logging & monitoring
Unit tests (pytest)

**Author**
Shubhangi Deore
Backend Developer | FastAPI | Python | SQLAlchemy