import sys
import os
import time
import datetime
import zerorpc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf import *
from util import *
from fetchInfo import *

class Interface(object):
    def __init__(self):
	self.session = getSession()
	self.fetch = FetchInfo()

    def get_jobs(self, owner=''):
	job_list = []
	ret = self.session.query(Job).filter(Job.job_owner==owner).all()
	for item in ret:
	    job_list.append(item.job_name)
	return job_list

    def get_host(self, task_id):
	ret = self.fetch.fetchHost(task_id)
	return ret

if __name__=='__main__':
    s = zerorpc.Server(Interface())
    s.bind("tcp://0.0.0.0:4242")
    s.run()
	
