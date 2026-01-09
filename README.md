🚀 Backend CRM API (FastAPI)

A production-ready Backend CRM API built using FastAPI, featuring JWT authentication, role-based access control, PostgreSQL, and Dockerized deployment.

This project demonstrates how to build secure, scalable REST APIs suitable for real-world backend systems.

✨ Features

🔐 JWT Authentication

Login & signup

Access token–based security

👥 Role-Based Access Control (RBAC)

admin vs user

Admin-only endpoints

🧑‍💻 User Management

CRUD operations

Filtering, sorting, pagination

🗄️ PostgreSQL Database

SQLAlchemy ORM

Environment-based configuration

🐳 Dockerized Setup

Dockerfile + docker-compose

One-command startup

📘 Swagger API Documentation

Interactive API testing

🛠 Tech Stack

Backend: Python 3.10, FastAPI

Auth: JWT (Access Tokens)

Database: PostgreSQL

ORM: SQLAlchemy

Containerization: Docker, Docker Compose

Docs: Swagger / OpenAPI

📂 Project Structure

backend-crm-api/
│
├── app/
│   ├── auth/               # Auth, JWT, RBAC
│   ├── routers/            # API routes
│   ├── services/           # Business logic
│   ├── database/           # DB config & models
│   └── schemas/            # Pydantic schemas
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

🚀 Running the Project (Docker)
1️⃣ Clone the repo
git clone https://github.com/shubhangi2441992/backend-crm-api.git
cd backend-crm-api

2️⃣ Start with Docker
docker compose up --build

3️⃣ Access API

API: http://localhost:8000

Swagger Docs: http://localhost:8000/docs

🔑 Authentication Flow

Register user

Login → get JWT

Use JWT in Swagger → Authorize

Access protected endpoints

🛡️ Admin-Only Endpoints

GET /admin/stats

GET /admin/logs

Only users with role = admin can access these.

🧪 Testing

All APIs are tested via Swagger UI:

Auth flow

CRUD operations

RBAC enforcement

Dockerized environment

📌 Why This Project Matters

This backend demonstrates:

Real-world authentication & authorization

Clean separation of concerns

Production-ready Docker setup

Scalable backend architecture

Ideal for backend-focused projects, MVPs, and API-first systems.

👩‍💻 Author

Shubhangi D.
Python Backend Developer
FastAPI • JWT • PostgreSQL • Docker