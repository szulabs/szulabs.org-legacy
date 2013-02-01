"""Configure about salt"""
SALT = "ABCDEFGHIJK"

"""Configure about database"""
DATABASE_HOST = "localhost"
DATABASE_PORT = "5432"
DATABASE_USERNAME = "postgres"
DATABASE_PASSWORD = ""
DATABASE_NAME = "szulabs"

"""Initial URI for SQLAchelmy"""
SQLALCHEMY_DATABASE_URI = ("postgresql://" + DATABASE_USERNAME + ":" +
                            DATABASE_PASSWORD + "@" + DATABASE_HOST + ":" +
                            DATABASE_PORT + "/" + DATABASE_NAME)