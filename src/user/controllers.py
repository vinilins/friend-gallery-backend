from src.user.repo import RepoReadUser, RepoWriteUser


def get_users_by_id(users):

    message = []
    users = RepoReadUser().get_users_by_id(users)

    if users:
        message = [
            {
                "id": str(user.id),
                "attributes": {
                    "email": str(user.email),
                    "name": str(user.name),
                    "is_bride_or_groom": bool(user.is_bride_or_groom),
                },
            }
            for user in users
        ]

    return message


def get_all_users_registered():

    message = []
    users = RepoReadUser().get_all_users()

    if users:
        message = [
            {
                "id": str(user.id),
                "attributes": {
                    "email": str(user.email),
                    "name": str(user.name),
                    "is_bride_or_groom": bool(user.is_bride_or_groom),
                },
            }
            for user in users
        ]

    return message


def create_new_user(user_params):

    message = {}

    user = RepoWriteUser().create_user(
        email=user_params["email"],
        is_bride_or_groom=user_params["is_bride_or_groom"],
        name=user_params["name"],
        password=user_params["password"],
    )

    if user:
        message = {
            "type": "Users",
            "id": str(user.id),
            "attributes": {"name": str(user.name)},
        }

    return message


def user_is_bride_or_groom(user_id):
    user = RepoReadUser().get_one_user_by_id(user_id)

    if user.is_bride_or_groom:
        return True

    return False
