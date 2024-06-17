from datetime import datetime, timedelta

from jose import JWTError, jwt

from user.auth.jwt_processor_interface import JwtProcessorInterface
from user.auth.jwt_settings import JwtSettings, get_jwt_settings


class JwtProcessor(JwtProcessorInterface):
    def __init__(self, jwt_settings: JwtSettings) -> None:
        self.jwt_settings = jwt_settings

    def create_set_password_token(self, user_id: int) -> dict:
        encode = {"id": user_id}
        expires = datetime.utcnow() + timedelta(hours=self.jwt_settings.expires_in)
        encode.update({"exp": expires})
        return jwt.encode(encode, self.jwt_settings.secret_key, algorithm=self.jwt_settings.algorithm)

    def create_access_token(self, username: str, user_id: int) -> dict:
        encode = {"sub": username, "id": user_id}
        expires = datetime.utcnow() + timedelta(hours=self.jwt_settings.expires_in)
        encode.update({"exp": expires})
        return jwt.encode(encode, self.jwt_settings.secret_key, algorithm=self.jwt_settings.algorithm)

    def validate_token(self, token: str) -> dict | bool:
        if token is None:
            return False

        try:
            payload = jwt.decode(token, self.jwt_settings.secret_key, algorithms=[self.jwt_settings.algorithm])
            return payload
        except JWTError:
            return False

    def create_confirm_email_token(self, user_id: int) -> str:
        payload = {
            "user_id": user_id,
            "exp": datetime.utcnow() + timedelta(hours=self.jwt_settings.expires_in),
        }

        return jwt.encode(payload, self.jwt_settings.secret_key, algorithm=self.jwt_settings.algorithm)


def get_jwt_processor() -> JwtProcessor:
    settings = get_jwt_settings()
    return JwtProcessor(settings)
