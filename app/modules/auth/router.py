from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from . import schemas, service
from app.modules.users.schemas import UserCreate
from app.modules.auth.schemas import LoginRequest, TokenResponse
from app.modules.users.service import create_user

router = APIRouter(prefix="/auth", tags=["Auth"])

# @router.post("/register")
# def register(user: UserCreate, db: Session = Depends(get_db)):
#     return create_user(db, user)

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    result = service.login_user(data.email, data.password,db)

    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return result
