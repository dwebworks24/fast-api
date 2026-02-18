from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from . import schemas, crud

router = APIRouter()

@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)
