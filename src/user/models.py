from mongoengine import (
    BooleanField,
    Document,
    StringField,
)


class User(Document):
    """User Model of the System"""

    name = StringField(required=True, max_length=255)
    email = StringField(required=True, max_length=255, unique=True)
    is_bride_or_groom = BooleanField(default=False, required=True)
    password = StringField(required=True, max_length=255)
