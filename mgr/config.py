import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///domain_manager.db"
    DEBUG = True
