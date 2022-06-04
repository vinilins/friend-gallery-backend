from os import getenv


class Config:
    DB = getenv("MONGO_URL")
    DB_NAME = getenv("DATABASE_NAME")
    DEBUG = False
    JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM = "HS256"
    JWT_IDENTITY_CLAIM = "sub"
    TESTING = False

    AWS_BUCKET = getenv("AWS_BUCKET")
    AWS_PASSWORD_KEY = getenv("AWS_PASSWORD_KEY")
    AWS_ID_KEY = getenv("AWS_ID_KEY")


class ProductionConfig(Config):
    ENV = "production"
    LOG_LEVEL = "INFO"


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    LOG_LEVEL = "DEBUG"


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
