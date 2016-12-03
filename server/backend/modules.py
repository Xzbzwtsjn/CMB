import sys
import os
from datetime import datetime
from sqlalchemy import Column, Float, String, Integer, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Job(Base):
    __tablename__ = 'job'

    id = Column(Integer, primary_key=True)
    job_name = Column(String, nullable=False)
    job_command = Column(String, nullable=False)
    job_shell = Column(Integer,nullable=False)
    job_owner = Column(String ,nullable=True)
    job_ownerName = Column(String, nullable=True)
    job_successCount = Column(Integer, nullable=False)
    job_errorCount = Column(Integer,nullable=False)
    job_lastSuccess = Column(String, nullable=True)
    job_lastError =Column(String, nullable=True)
    job_cpus = Column(Float, nullable=False)
    job_disk = Column(Float, nullable=False)
    job_mem = Column(Float, nullable=False)
    job_constraints = Column(String, nullable=True)
    job_schedule = Column(String,nullable=True)

class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    task_id = Column(String, nullable=False)
    task_state =Column(String, nullable=False)
    task_ts = Column(String, nullable=False)
    job_name = Column(String, nullable=False)

class Resource(Base):
    __tablename__ = 'resource'

    id = Column(Integer, primary_key=True)
    hostName = Column(String, nullable=False)
    pid = Column(String, nullable=False)
    active = Column(String, nullable=False)
    host_id = Column(String, nullable=False)
    host_cpus = Column(Float, nullable=False)
    host_mem = Column(Float, nullable=False)
    host_disk = Column(Float, nullable=False)

class Container(Base):
    __tablename__='container'
    id = Column(Integer, primary_key=True)
    containerID = Column(String, nullable=False)
    containerName = Column(String, nullable=False)
    containerImage = Column(String, nullable=False)
    containerStatus = Column(String, nullable=False)
    command = Column(String, nullable=False)
    cpu_usage_in_user = Column(String, nullable=False)
    cpu_usage_in_ker = Column(String, nullable=False)
    cpu_total = Column(String, nullable=False)
    rx_bytes = Column(String, nullable=True)
    tx_bytes = Column(String, nullable=True)
