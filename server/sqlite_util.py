import sys
import os
import simplejson as json
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf import *
from modules import *

def initDB():
    engine = create_engine(dbPath)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    content = json.load(open("./json/db_init.json"))
    au = content['author']
    op = content['opType']
    inv = content['invalid']
    print content
    for po in content['data']:
        session.add(MainPolicy(author=au, \
                               opType=op, \
                               invalid=inv, \
                               cpu_norm=po['cpu_norm'], \
                               mem_norm=po['mem_norm'], \
                               basePrice=po['basePrice'], \
                               monPrice=po['monPrice'], \
                               aftPrice=po['aftPrice'], \
                               nigPrice=po['nigPrice']))
    session.commit()
    session.close()
    
