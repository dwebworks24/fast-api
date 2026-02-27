from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database.session import get_db
from . import schemas, service

router = APIRouter(tags=["Auth"])


@router.post("/login", response_model=schemas.TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    result = service.login_user(
        form_data.username,
        form_data.password,
        db
    )

    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    return result



@router.post("/logout")
def logout(
    token: str = Depends(OAuth2PasswordRequestForm),
    db: Session = Depends(get_db)
):
    blacklisted = TokenBlacklist(token=token)
    db.add(blacklisted)
    db.commit()

    return {"message": "Logged out successfully"}


# @router.post("/refresh")
# def refresh_token(
#     refresh_token: str,
#     db: Session = Depends(get_db)
# ):
#     try:
#         payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=[ALGORITHM])
#         user_id = payload.get("sub")

#         if user_id is None:
#             raise HTTPException(status_code=401, detail="Invalid refresh token")

#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid refresh token")

#     new_access_token = create_access_token(subject=user_id)

#     return {
#         "access_token": new_access_token,
#         "token_type": "bearer"
#     }