from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.modules.users.models import User
from app.core.security import *


def login_user(email: str, password: str, db: Session):

    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    access_token = create_access_token(subject=str(user.id))
    refresh_token = create_refresh_token(subject=str(user.id))

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


