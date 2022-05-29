from mongoengine import connect


class DBConnectionHandler:
    """MongoEngine Database Connection"""

    def __init__(self) -> None:
        self.__connection_string = ""
        self.session = None

    def get_db_engine(self):

        db_engine = connect(self.__connection_string)
        return db_engine
