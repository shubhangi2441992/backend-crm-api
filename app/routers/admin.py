from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.auth.jwt_dependency import get_current_user
from app.auth.role_dependency import require_role
from app.schemas.response import ResponseModel
from app.database.models import UserModel

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/stats", response_model=ResponseModel)
def admin_stats(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
    _ = Depends(require_role("admin"))
):
    total_users = db.query(UserModel).count()

    return ResponseModel(
        success=True,
        data={
            "total_users": total_users
        },
        message="Admin stats fetched"
    )

@router.get("/logs", response_model=ResponseModel)
def admin_logs(
    current_user = Depends(get_current_user),
    _ = Depends(require_role("admin"))
):
    return ResponseModel(
        success=True,
        data={
            "logs": [
                "User created",
                "User updated",
                "User deleted"
            ]
        },
        message="System logs"
    )
