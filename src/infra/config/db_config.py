from mongoengine import connect
from .db_info import database_info


class DBConnectionHandler:
    """MongoEngine Database Connection"""

    def __init__(self) -> None:
        self.__connection_string = database_info["host"]
        self.__database_name = database_info["database"]

    def get_db_engine(self):

        db_engine = connect(db=self.__database_name, host=self.__connection_string)
        return db_engine
