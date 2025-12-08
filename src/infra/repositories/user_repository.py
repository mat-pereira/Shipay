from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.domain.user_model import UserModel
from src.utils.logger import log_debug, log_warning, log_error

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, user: UserModel) -> UserModel:
        try:
            log_debug(f"Salvando usuário no banco de dados")
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
            
        
        except Exception as e:
            self.db.rollback()
            log_error(f"Erro ao salvar usuário: {e}", e)
            raise

    def find_by_email(self, email: str) -> UserModel:
        try:
            user = self.db.query(UserModel).filter(UserModel.email == email).first()
            
            if user:
                log_debug(f"Usuaário encontrado {user.id}")
            else:
                log_debug(f"Usuário não encontrado: {email}")
            
            return user
        except Exception as e:
            log_error(f"Erro ao buscar usuário no banco de dados: {e}", e)
            raise