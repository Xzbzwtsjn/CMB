import sys
import os
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MainPolicy(Base):
    __tablename__ = 'main_policy'

    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    cpu = Column(Integer, nullable=False)
    mem = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    invalid = Column(Integer, nullable=False)
    validTime = Column(Integer ,nullable=False)

class AUXMainPolicy(Base):
    __tablename__ = 'aux_main_policy'

    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    cpu = Column(Integer, nullable=False)
    mem = Column(Integer, nullable=False)
    weight =Column(Integer, nullable=False)
    invalid = Column(Integer, nullable=False)
    validTime =Column(Integer,nullable=False)

class CPUPolicy(Base):
    __tablename__ = 'cpu_policy'

    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    resourceType = Column(String, nullable=False)
    unitPrice = Column(Integer, nullable=False)
    invalid = Column(Integer, nullable=False)
    validTime = Column(DateTime, default=datetime.now, nullable=False)
    def __repr__(self):
        return __tablename__

class AUXCPUPolicy(Base):
    __tablename__ = 'aux_cpu_policy'

    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    resourceType = Column(String, nullable=False)
    unitPrice = Column(Integer, nullable=False)
    invalid = Column(Integer, nullable=False)
    validTime = Column(DateTime, default=datetime.now, nullable=False)


class MemPolicy(Base):
    __tablename__ = 'mem_policy'

    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    resourceType = Column(String, nullable=False)
    unitPrice = Column(Integer, nullable=False)
    invalid =Column(Integer, nullable=False)
    validTime = Column(DateTime,default=datetime.now, nullable=False)

class AUXMemPolicy(Base):
    __tablename__ = 'aux_mem_policy'

    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    resourceType = Column(String, nullable=False)
    unitPrice = Column(Integer, nullable=False)
    invalid =Column(Integer, nullable=False)
    validTime = Column(DateTime,default=datetime.now, nullable=False)


class DiskPolicy(Base):
    __tablename__ ='disk_policy'

    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    resourceType =Column(String, nullable=False)
    unitPrice = Column(Integer, nullable=False)
    invalid = Column(Integer, nullable=False)
    validTime = Column(DateTime, default=datetime.now, nullable=False)

class AUXDiskPolicy(Base):
    __tablename__ ='aux_disk_policy'

    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    resourceType =Column(String, nullable=False)
    unitPrice = Column(Integer, nullable=False)
    invalid = Column(Integer, nullable=False)
    validTime = Column(DateTime, default=datetime.now, nullable=False)

class NetPolicy(Base):
    __tablename__ = 'net_policy'

    id = Column(Integer,primary_key=True)
    author = Column(String(20), nullable=False)
    resourceType = Column(String, nullable=False)
    unitPrice = Column(String, nullable=False)
    invalid = Column(Integer,nullable=False)
    vlidTime = Column(DateTime, default=datetime.now, nullable=False)

class AUXNetPolicy(Base):
    __tablename__ = 'aux_net_policy'

    id = Column(Integer,primary_key=True)
    author = Column(String(20), nullable=False)
    resourceType = Column(String, nullable=False)
    unitPrice = Column(String, nullable=False)
    invalid = Column(Integer,nullable=False)
    vlidTime = Column(DateTime, default=datetime.now, nullable=False)


class Pair(Base):
    __tablename__ ='pair'

    id = Column(Integer, primary_key=True)
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)
    author = Column(String(20), nullable=False)
    modifiedTime = Column(DateTime, default=datetime.now, nullable=False)

class AUXPair(Base):
    __tablename__ ='aux_pair'

    id = Column(Integer, primary_key=True)
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)
    author = Column(String(20), nullable=False)
    modifiedTime = Column(DateTime, default=datetime.now, nullable=False)

#Base.metadata.create_all(engine)
