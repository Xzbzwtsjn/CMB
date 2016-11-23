import sys
import os
import httplib
import urllib
import simplejson as json
from conf import *
from modules import *
from werkzeug.wrappers import Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def response(func):
    def inner(*args, **kvargs):
        ret = func(*args,**kvargs)
        if ret is not None:
            return Response(ret, mimetype = "text/plain")
        else:
            return Response("None Data", mimetype = "text/plain")
    return inner

def getHttpConnection(ip, port, endpoint):
    data = ''
    try:
        conn = httplib.HTTPConnection("%s:%s"%(ip,port))
        conn.request("GET","%s"%(endpoint,))
        r1 = conn.getresponse()
        data = r1.read()
    except Exception, e:
        print e
    return data

def CurrentLeader():
    for item in MesosMasterAddress:
        ret = getHttpConnection(item, MesosMasterPort, '/slaves')
        data = json.loads(ret)
        if data['slaves'] is not None:
            return item

def IniteDB():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

def getSession():
    engine = create_engine('sqlite:///:memory:')
    session = sessionmaker(bind=engine)
    return session
