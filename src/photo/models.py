from mongoengine import (
    BooleanField,
    DictField,
    Document,
    ListField,
    StringField,
)


class Photo(Document):
    """Photo Model of the System"""

    link_aws = StringField(required=True)
    who_liked = ListField()
    approved = BooleanField(default=False, required=True)
    comments = ListField(DictField())
