import sys
import os
import datetime
from sqlalchemy import Column, Float, String, Integer, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MainPolicy(Base):
    __tablename__ = 'main_policy'

    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    cpu_norm = Column(Integer, nullable=False)
    mem_norm = Column(Integer, nullable=False)
    basePrice = Column(Float, nullable=False)
    monPrice = Column(Float, nullable=False)
    aftPrice = Column(Float, nullable=False)
    nigPrice = Column(Float, nullable=False)
    invalid = Column(Integer, nullable=False)
    opType = Column(String, nullable=False)
    modifiedTime = Column(DateTime, default=datetime.datetime.now(), nullable=False)


class AUXMainPolicy(Base):
    __tablename__ = 'aux_main_policy'

    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    cpu_norm = Column(Integer, nullable=False)
    mem_norm = Column(Integer, nullable=False)
    basePrice = Column(Float, nullable=False)
    monPrice = Column(Float, nullable=False)
    aftPrice = Column(Float, nullable=False)
    nigPrice = Column(Float, nullable=False)
    invalid = Column(Integer, nullable=False)
    opType = Column(Integer, nullable=False)
    modifiedTime =Column(DateTime, default=datetime.datetime.now(), nullable=False)


class CPUPolicy(Base):
    __tablename__ = 'cpu_policy'

    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    resourceType = Column(String, nullable=False)
    unitPrice = Column(Float, nullable=False)
    invalid = Column(Integer, nullable=False)
    opType = Column(Integer, nullable=False)
    modifiedTime = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    def __repr__(self):
        return __tablename__


class AUXCPUPolicy(Base):
    __tablename__ = 'aux_cpu_policy'

    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    resourceType = Column(String, nullable=False)
    unitPrice = Column(Float, nullable=False)
    invalid = Column(Integer, nullable=False)
    opType = Column(Integer, nullable=False)
    modifiedTime = Column(DateTime, default=datetime.datetime.now(), nullable=False)


class MemPolicy(Base):
    __tablename__ = 'mem_policy'

    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    resourceType = Column(String, nullable=False)
    unitPrice = Column(Float, nullable=False)
    invalid =Column(Integer, nullable=False)
    opType = Column(Integer, nullable=False)
    modifiedTime = Column(DateTime, default=datetime.datetime.now(), nullable=False)


class AUXMemPolicy(Base):
    __tablename__ = 'aux_mem_policy'

    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    resourceType = Column(String, nullable=False)
    unitPrice = Column(Float, nullable=False)
    invalid =Column(Integer, nullable=False)
    opType = Column(Integer, nullable=False)
    modifiedTime = Column(DateTime, default=datetime.datetime.now(), nullable=False)


class DiskPolicy(Base):
    __tablename__ ='disk_policy'

    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    resourceType =Column(String, nullable=False)
    unitPrice = Column(Float, nullable=False)
    invalid = Column(Integer, nullable=False)
    opType = Column(Integer, nullable=False)
    modifiedTime = Column(DateTime, default=datetime.datetime.now(), nullable=False)


class AUXDiskPolicy(Base):
    __tablename__ ='aux_disk_policy'

    id = Column(Integer, primary_key=True)
    author = Column(String(20), nullable=False)
    resourceType =Column(String, nullable=False)
    unitPrice = Column(Float, nullable=False)
    invalid = Column(Integer, nullable=False)
    opType = Column(Integer, nullable=False)
    modifiedTime = Column(DateTime, default=datetime.datetime.now(), nullable=False)


class NetPolicy(Base):
    __tablename__ = 'net_policy'

    id = Column(Integer,primary_key=True)
    author = Column(String(20), nullable=False)
    resourceType = Column(String, nullable=False)
    unitPrice = Column(Float, nullable=False)
    invalid = Column(Integer,nullable=False)
    opType = Column(Integer, nullable=False)
    modifiedTime = Column(DateTime, default=datetime.datetime.now(), nullable=False)


class AUXNetPolicy(Base):
    __tablename__ = 'aux_net_policy'

    id = Column(Integer,primary_key=True)
    author = Column(String(20), nullable=False)
    resourceType = Column(String, nullable=False)
    unitPrice = Column(Float, nullable=False)
    invalid = Column(Integer,nullable=False)
    opType = Column(Integer, nullable=False)
    modifiedTime = Column(DateTime, default=datetime.datetime.now(), nullable=False)


class MeteringService(Base):
    __tablename__ = 'metering_service'

    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
    author = Column(String(20), nullable=False)
    modifiedTime = Column(DateTime, default=datetime.datetime.now(), nullable=False)


class DataSource(Base):
    __tablename__ = 'data_source'

    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
    author = Column(String ,nullable=False)
    modifiedTime = Column(String ,nullable=False)


class Pair(Base):
    __tablename__ = 'pair'

    id = Column(Integer, primary_key=True)
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)
    author = Column(String(20), nullable=False)
    modifiedTime = Column(DateTime, default=datetime.datetime.now(), nullable=False)


class AUXPair(Base):
    __tablename__ = 'aux_pair'

    id = Column(Integer, primary_key=True)
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)
    author = Column(String(20), nullable=False)
    modifiedTime = Column(DateTime, default=datetime.datetime.now(), nullable=False)
