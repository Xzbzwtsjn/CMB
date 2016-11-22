import sys
import os
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Policy(Base):
    __tablename__ = 'Policy'

    id = Column(String(20), primary_key=True)
    author = Column(String(20))
    resourceType = Column(String(20))
