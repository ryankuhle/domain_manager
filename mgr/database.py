import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from . import app

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Entry(Base):
    __tablename__ = "domains"

    id = Column(Integer, primary_key=True)
    date_added = Column(String(8))
    url = Column(String(63))
    web_host = Column(String(26))
    host_login = Column(String(63))
    username = Column(String(26))
    password = Column(String(26))
    city = Column(String(26))
    niche = Column(String(26))
    forwarding_email = Column(String(85))
    datetime = Column(DateTime, default=datetime.datetime.now)

Base.metadata.create_all(engine)
