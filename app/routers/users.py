from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.user import UserCreate
from app.schemas.response import ResponseModel
from app.services import user_service
from app.auth.jwt_dependency import get_current_user
from app.database.models import UserModel
from app.auth.role_dependency import require_role

router = APIRouter()

@router.post("/", response_model=ResponseModel)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)):
    """Create a new user (protected route)."""
    return user_service.create_user(db, user)


@router.get("/", response_model=ResponseModel)
def list_users(
    name: str = None,
    min_age: int = None,
    max_age: int = None,
    sort_by: str = "id",
    order: str = "asc",
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)):
    """List users with filtering, sorting, and pagination."""
    return user_service.list_users(db, name, min_age, max_age, sort_by, order, skip, limit)


@router.get("/{user_id}", response_model=ResponseModel)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)):
    """Get a single user by ID."""
    return user_service.get_user(db, user_id)


@router.put("/{user_id}", response_model=ResponseModel)
def update_user(
    user_id: int,
    user_data: UserCreate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)):
    """Update an existing user by ID."""
    return user_service.update_user(db, user_id, user_data)

@router.delete("/{user_id}", response_model=ResponseModel)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
    _ = Depends(require_role("admin"))
):
    return user_service.delete_user(db, user_id)



