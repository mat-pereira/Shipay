from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.domain.user_request import UserRequest, UserResponse
from src.services.user_service import UserService
from src.infra.repositories.user_repository import UserRepository
from src.services.password_service import PasswordService
from src.infra.db import get_db

router = APIRouter(tags=["Users"])

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    user_repo = UserRepository(db)
    password_svc = PasswordService()
    return UserService(user_repo, password_svc)

@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(dto: UserRequest, user_service: UserService = Depends(get_user_service)):

    try:
        user = user_service.create_user(
            name=dto.name,
            email=dto.email,
            role_id=dto.role_id,
            password=dto.password
        )
        return user
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao criar usuário")