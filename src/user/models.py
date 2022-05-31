from mongoengine import (
    BooleanField,
    Document,
    EmailField,
    StringField,
)


class User(Document):
    """User Model of the System"""

    name = StringField(required=True, max_length=255)
    email = EmailField(required=True)
    is_bride_or_groom = BooleanField(default=False, required=True)
    password = StringField(required=True, max_length=255)
