Service raises HTTPException
        ↓
FastAPI catches it
        ↓
Your custom exception handler runs
        ↓
Response converted to your format



Client sends request
      │
      ▼
Router (users.py)
  - Calls service function
  - Expects return value
      │
      ▼
Service (user_service.py)
  - Queries DB
  - If data exists → returns User object
  - If not → raises HTTPException(status_code=404, detail="User not found")
      │
      ▼
FastAPI checks for exceptions
      │
      ├─ If HTTPException raised → goes to custom handler in main.py
      │       - Converts exception to:
      │         {
      │           "success": false,
      │           "message": exc.detail,
      │           "data": null
      │         }
      │
      └─ If no exception → router returns success response:
              {
                "success": true,
                "message": "User fetched/updated/deleted successfully",
                "data": <User or list>
              }
      │
      ▼
Client receives consistent response


🔹 Key points

Service never returns raw error responses — it raises HTTPException.

Router never manually checks for “not found” — it trusts the service.

Custom handler in main.py ensures all exceptions follow your success/message/data format.

This setup is clean, professional, and scalable — used in real-world projects.


1️⃣ main.py

Include your FastAPI app initialization

Include database table creation (for dev/testing)

Include routers (users)

Include HTTPException handler (custom response format)

Include validation exception handler

Optional root endpoint

Optional direct run block (uvicorn.run)

Already updated in previous steps

2️⃣ user_service.py

Keep all CRUD functions (create_user, list_users, get_user, update_user, delete_user)

Raise HTTPException if user not found (DO NOT remove)

Return User object(s) on success

All database operations use SQLAlchemy session

Already updated in previous steps

3️⃣ users.py (router)

All endpoints (POST, GET all, GET by id, PUT, DELETE)

Always return custom response format:

{
  "success": true|false,
  "message": "...",
  "data": <User object / list / null>
}


No need to check None manually — service raises exception, handler formats response

4️⃣ schemas/user.py

Pydantic models:

UserCreate → for input

User → for response

Ensure consistent field names (id, name, age)

5️⃣ database setup

database.py → SQLAlchemy engine + get_db dependency

models.py → UserModel table

main.py → models.Base.metadata.create_all(bind=engine) for dev

6️⃣ exceptions.py

validation_exception_handler (already implemented)

Registered in main.py