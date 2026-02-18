from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.post("/login")
def login():
    return {"message": "Login working"}
