from fastapi import APIRouter
from app.models.user_model import User
from app.services.user_service import user_service

router = APIRouter()

@router.get('/users')
def get_users():
    return user_service.get_users()

@router.post('/users')
def create_users(user: User):
    user_service.create_user(user)