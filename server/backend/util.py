import sys
import os
import time
import datetime
import httplib
import urllib
import simplejson as json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf import *
from modules import *

def getSession():
    engine = create_engine(dbPath)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def getHttpConnection(ip, port, endpoint):
    ret = ''
    try:
        conn = httplib.HTTPConnection("%s:%s"%(ip, port))
        conn.request("GET","%s"%(endpoint,))
        r1 = conn.getresponse()
        ret = r1.read()
    except Exception, e:
        print e
    return ret

def initDB():
    engine = create_engine(dbPath)
    Base.metadata.create_all(engine)
    ''''Session = sessionmaker(bind=engine)
    session = Session()
    session.add(Resource(hostName='admin', \
                         host_id='zkdcos', \
                         pid='master9@172.029.152.185', \
                         active='True', \
                         host_cpus=2.0, \
                         host_mem=64.0, \
                         host_disk=1000.0))
    session.commit()
    session.close()
    '''
def CurrentLeader():
    for item in MesosMasterAddress:
        ret = getHttpConnection(item, MesosMasterPort, '/slaves')
        data = json.loads(ret)
        if data['slaves'] is not None:
            return item

def obtain_Slave_ID(Chronos_taskID):
    Curleader = CurrentLeader()
    try:
        conn = httplib.HTTPConnection("%s:%s"%(Curleader, MesosMasterPort))
        conn.request("GET", "/master/tasks.json?limit=400")
        r1 = conn.getresponse()
    except Exception,e:
        print 'get http failed\n'

    if r1.status == 200:
        raw = r1.read() #str
        data = json.loads(raw)
        for item in data["tasks"]:
            if item["id"] == Chronos_taskID:
                # print item['slave_id']
                conn.close()
                return item['slave_id']
    else:
        return None
        conn.close()

def obtain_Slave_IP_PORT(taskID):
        slaveID = obtain_Slave_ID(taskID)
        curLeader = CurrentLeader()
        if slaveID == None:
            return None
        try:
            conn=httplib.HTTPConnection("%s:%s"%(curLeader, MesosMasterPort))
            conn.request("GET", "/master/slaves")
            r1 = conn.getresponse()
        except Exception,e:
            print 'get http failed\n'

        if r1.status==200:
            raw = r1.read()
            data=json.loads(raw)
            for item in data["slaves"]:
                if item['id'] == slaveID:
                    #print item["pid"].decode('utf-8').split("@")[1]
                    return  item["pid"].decode('utf-8').split("@")[1]
                    conn.close()
                else:
                    continue
            return None
            conn.close()
        else:
            return None
            conn.close()
