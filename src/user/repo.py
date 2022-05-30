from src.user.models import User


class RepoReadUser:
    """Read Repo Class of the UserModel"""

    @staticmethod
    def get_one_user_by_id(id) -> User:
        return User.objects(id=id).limit(1).first()

    @staticmethod
    def get_one_user_by_email(email) -> User:
        return User.objects(email=email).limit(1).first()

    @staticmethod
    def get_users_by_id(users):
        return User.objects(id__in=users)

    @staticmethod
    def get_all_users():
        return User.objects()

    @staticmethod
    def get_bride_or_groom() -> User:
        return User.objects(is_bride_or_groom=True)


class RepoWriteUser:
    """Write Repo Class of the UserModel"""

    @staticmethod
    def create_user(email, password, is_bride_or_groom, name) -> User:
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
