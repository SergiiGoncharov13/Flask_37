import os


# SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/dbname'

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123321@localhost/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False