from src.infra.repositories.user_repository import UserRepository
from src.services.password_service import PasswordService
from src.domain.user_model import UserModel
from src.utils.logger import log_info, log_success, log_warning, log_error, log_debug
from datetime import datetime, timezone

class UserService:
    def __init__(self, user_repository: UserRepository, password_service: PasswordService):
        self.user_repository = user_repository
        self.password_service = password_service

    def create_user(self, name: str, email: str, role_id: int, password: str = None) -> UserModel:
        try:
            log_info(f"Criando usuário")
            
            if not name or not name.strip():
                log_warning(f"Nome vazio para: {email}")
                raise ValueError("Nome não pode estar vazio")
            
            if not email or not email.strip():
                log_warning("Email vazio")
                raise ValueError("Email não pode estar vazio")
            
            if role_id <= 0:
                log_warning(f"Role ID inválido: {role_id}")
                raise ValueError("Role ID deve ser maior que 0")
            
            if not password:
                log_debug("Gerando senha automática...")
                password = self.password_service.generate()
                log_debug(f"Senha gerada: {password}")
            else:
                log_debug("Usando senha enviada pelo usuário")
            
            hashed_password = self.password_service.hash(password)
            log_debug("Senha hasheada com sucesso")
            
            user = UserModel(
                name=name,
                email=email,
                password=hashed_password,
                role_id=role_id,
                created_at=datetime.now(timezone.utc)
            )
            
            saved_user = self.user_repository.save(user)
            log_success(f"Usuário criado! ID: {saved_user.id}")
            
            return saved_user
            
        except ValueError as e:
            log_warning(f"Validação falhou: {e}")
            raise
        except Exception as e:
            log_error(f"Erro ao criar usuário: {e}", e)
            raise