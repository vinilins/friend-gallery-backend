from src.user.models import User


class RepoReadUser:
    """Read Repo Class of the UserModel"""

    @staticmethod
    def get_one_user_by_id(id: str) -> User:
        return User.objects(id=id).limit(1).first()

    @staticmethod
    def get_one_user_by_email(email: str) -> User:
        return User.objects(email=email).limit(1).first()

    @staticmethod
    def get_users_by_id(users: list[str]) -> list[User]:
        return User.objects(id__in=users)

    @staticmethod
    def get_all_users() -> list[User]:
        return User.objects()

    @staticmethod
    def get_bride_or_groom() -> list[User]:
        return User.objects(is_bride_or_groom=True)


class RepoWriteUser:
    """Write Repo Class of the UserModel"""

    @staticmethod
    def create_user(
        email: str, password: str, is_bride_or_groom: bool, name: str
    ) -> User:
        try:
            exists_user = RepoReadUser().get_one_user_by_email(email=email)

            if exists_user:
                raise Exception("User already exists!")

            user = User(
                email=email,
                is_bride_or_groom=is_bride_or_groom,
                name=name,
                password=password,
            )
            user.save()

            return user
        except Exception as error:
            raise Exception(f"Error in create new User: {error}")
