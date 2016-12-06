import sys
import os
import random
import time
import datetime
from sqlalchemy import Column, Float, String, Integer, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Record(Base):
    __tablename__ = 'container_record'

    id = Column(Integer, primary_key=True)
    container_id = Column(String, nullable=False)
    host = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime,nullable=False)
    run_time = Column(Integer, nullable=False)
    cpu_assign = Column(Float, nullable=False)
    cpu_ave_cost = Column(Float, nullable=False)
    cpu_max_cost = Column(Float, nullable=False)
    cpu_max_cost_time = Column(Integer, nullable=False)
    cpu_ave_load = Column(Float, nullable=False)
    mem_assign = Column(Float, nullable=False)
    mem_ave_cost = Column(Float, nullable=False)
    mem_max_cost = Column(Float, nullable=False)
    mem_max_cost_time = Column(Integer, nullable=False)
    rx_bytes = Column(Integer, nullable=False)
    tx_bytes = Column(Integer, nullable=False)
    task_id = Column(String, nullable=False)

def ideal():
    e2 = create_engine("sqlite:///db/idealism")
    Base.metadata.create_all(e2)
    Session = sessionmaker(bind=e2)
    session = Session()
    for i in range(100):
        session.add(Record(container_id='130d20694836%d'%(i), \
                           host = '172.29.152.185', \
                           start_time = datetime.datetime.now(), \
                           end_time = datetime.datetime.now(), \
                           run_time = random.randint(170, 300), \
                           cpu_assign = random.randint(1, 8), \
                           cpu_ave_cost = 0.2, \
                           cpu_max_cost = 0.7, \
                           cpu_max_cost_time = random.randint(10, 40), \
                           cpu_ave_load = 0.4, \
                           mem_assign = 1024, \
                           mem_ave_cost = 0.2, \
                           mem_max_cost = 0.8, \
                           mem_max_cost_time = random.randint(10, 40), \
                           rx_bytes = 1000000, \
                           tx_bytes = 1000000, \
                           task_id = 'ct:1480766602841:0:test-%d:'%(i)))
    session.commit()
    session.close()

if __name__ == '__main__':
    ideal()
