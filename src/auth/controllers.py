from datetime import timedelta
from typing import Optional, Tuple
from bson.objectid import ObjectId
from flask_jwt_extended import create_access_token
from src.user.models import User
from src.user.repo import RepoReadUser


def corrects_credentials(login_credentials: dict) -> Tuple[Optional[User], bool]:
    user = RepoReadUser().get_one_user_by_email(email=login_credentials["email"])

    if user:
        password = user.password
        email = user.email

        if (
            email == login_credentials["email"]
            and password == login_credentials["password"]
        ):
            return user, True

    return None, False


def create_acess_token(user_id: ObjectId) -> str:

    return create_access_token(identity=str(user_id), expires_delta=timedelta(days=2))
