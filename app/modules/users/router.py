from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.database.session import get_db
from . import schemas, service

router = APIRouter()

@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user)


@router.get("/users")
def read_users(db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    return service.get_users(db)


@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    return service.get_user_by_id(db, user_id)

@router.put("/users/{user_id}")
def update_user(
    user_id: int,
    user_data: schemas.UserUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return service.update_user(db, user_id, user_data)


@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return service.delete_user(db, user_id)