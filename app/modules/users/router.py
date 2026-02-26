from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from . import schemas, service

router = APIRouter()

@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user)


@router.get("/users")
def read_users(db: Session = Depends(get_db)):
    return service.get_users(db)


@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return service.get_user_by_id(db, user_id)