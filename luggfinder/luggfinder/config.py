from flask import Config



class Development(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///unittest.db"
    SECRET_KEY = "AJ8sSjhS9Sj1@#9jd8123JKD(8((jdaskdjSÇASHd9217301!@*#&(klj@!klç"

class Production(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SECRET_KEY = "AJ8sSjhS9Sj1@#9jd8123JKD(8((jdaskdjSÇASHd9217301!@*#&(klj@!klç"