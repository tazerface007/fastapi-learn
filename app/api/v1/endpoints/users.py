# app/api/v1/endpoints/users.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_users():
    return {"message": "List users"}