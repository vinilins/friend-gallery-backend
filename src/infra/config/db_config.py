from mongoengine import connect


class DBConnectionHandler:
    """MongoEngine Database Connection"""

    def __init__(self, db_url, db_name) -> None:
        self.__connection_string = db_url
        self.__database_name = db_name

    def get_db_engine(self):

        db_engine = connect(db=self.__database_name, host=self.__connection_string)
        return db_engine


def db_init_app(app):
    db_connection = DBConnectionHandler(
        db_url=app.config["DB"], db_name=app.config["DB_NAME"]
    )
    db_connection.get_db_engine()
