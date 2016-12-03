import sys
import os
import time
import datetime
import zerorpc
import simplejson as json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf import *
from util import *
import threading
from threading import Thread

class FetchInfo(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.res_pool = []
        self.jobs = []
        self.jobName = []
        self.tasks = {}
        self.client = zerorpc.Client()
        self.session = getSession()

    def fetchMesosInfo(self):
        for address in MesosMasterAddress:
            ans = getHttpConnection(address, MesosMasterPort,'/slaves')
            data = json.loads(ans)
            if data['slaves'] is not None:
                for item in data['slaves']:
                    host = {}
                    host['hostname'] = item['hostname']
                    host['pid'] = item['pid']
                    host['active'] = item['active']
                    host['id'] = item['id']
                    #print item['resources'],type(item['resources'])
                    res = item['resources']
                    host['cpus'] = res['cpus']
                    host['mem'] = res['mem']
                    host['disk'] = res['disk']
                    self.res_pool.append(host)
                break

    def dumpRes(self):
        for host in self.res_pool:
            ret = self.session.query(Resource).filter(Resource.host_id==host['id']).all()
            if not ret :
                self.session.add(Resource(hostName=host['hostname'],\
                                           pid=host['pid'],\
                                           active=host['active'],\
                                           host_id=host['id'],\
                                           host_cpus=host['cpus'],\
                                           host_mem=host['mem'],\
                                           host_disk=host['disk']))
            else:
                self.session.query(Resource).filter(Resource.host_id==host['id']).update({'host_cpus':host['cpus'], \
                                                                                          'host_mem':host['mem'], \
                                                                                          'host_disk':host['disk']})
            self.session.commit()

    def dumpJobs(self):
        #print self.jobs
        for job in self.jobs:
            ret = self.session.query(Job).filter(Job.job_name==job['name']).all()
            if not ret:
                shell = 0
                if job['shell'] is True:
                    shell = 1
                self.session.add(Job(job_name=job['name'], \
                                     job_command=job['command'], \
                                     job_shell=shell, \
                                     job_owner=job['owner'], \
                                     job_ownerName=job['ownerName'], \
                                     job_successCount=job['successCount'], \
                                     job_errorCount=job['errorCount'], \
                                     job_lastSuccess=job['lastSuccess'], \
                                     job_lastError=job['lastError'], \
                                     job_cpus=job['cpus'], \
                                     job_disk=job['disk'], \
                                     job_mem=job['mem'], \
                                     job_constraints=str(job['constraints']), \
                                     job_schedule=job['schedule']))
            else:
                self.session.query(Job).filter(Job.job_name==job['name']).update({'job_name':job['name'], \
                                                                                  'job_command':job['command'], \
                                                                                  'job_shell':job['shell'], \
                                                                                  'job_successCount':job['successCount'], \
                                                                                  'job_errorCount':job['errorCount'], \
                                                                                  'job_lastSuccess':job['lastSuccess'], \
                                                                                  'job_lastError':job['lastError'], \
                                                                                  'job_schedule':str(job['schedule'])})
            self.session.commit()

    def dumpTasks(self):
        for item in self.jobs:
            job_name = item['name']
            self.jobName.append(job_name)
        ans = self.fetchUserTasks(self.jobName)
        ans = json.loads(ans)
        self.tasks = ans

    def outputTasks(self):
        return self.tasks #return a dict
        '''
        for item in self.jobName:
            toTask = ans[item]
            for re in toTask:
                #objs = self.session.query(Task).filter(Task.task_id==re['id']).all()
                #if not objs:
                self.session.add(Task(task_state=re['task_state'], \
                                      task_id=re['id'], \
                                      task_ts=str(re['ts']), \
                                      job_name=re['job_name']))
                #else:
                #    self.session.query(Task).filter(Task.task_id==re['id']).update({'task_id':re['id'], \
                #                                                                    'task_state':re['task_state'], \
                #                                                                    'task_ts':re['ts'], \
                #                                                                    'job_name':re['job_name']})
                self.session.commit()
        '''
    def fetchUserJobs(self):
        ans = getHttpConnection(ChronosMaster, ChronosPort, '/scheduler/jobs')
        ans = json.loads(ans)
        for re in ans:
            self.jobs.append(re)

    def fetchUserTasks(self, jobName):
        self.client.connect("tcp://%s:%s"%(Cassandra, CassandraListenPort))
	result = self.client.get_taskID(jobName)
	return result

    def fetchHost(self, taskID):
        #slaveID = obtain_Slave_ID(taskID)
        #print slaveID
        slaveHost = obtain_Slave_IP_PORT(taskID)
        return slaveHost

    def run(self):
        while True:
            self.fetchMesosInfo()
            self.dumpRes()
            time.sleep(10)
            self.fetchUserJobs()
            self.dumpJobs()
            time.sleep(10)
'''
class Interface(object):
    def __init__(self):
        passx
    def add(self, a, b):
        return "The result is %d"%(a + b)
'''
if __name__ == '__main__':
    initDB()
    fetch = FetchInfo()
    
    #fetch.fetchHost('ct:1479283558330:0:test-11-16-22:')
    #fetch.fetchUserJobs()
    #fetch.dumpJobs()
    #fetch.dumpTasks()
    #fetch.start()
    #fetch.join()
    service = zerorpc.Server(FetchInfo())
    service.bind("tcp://0.0.0.0:4243")
    service.run()
