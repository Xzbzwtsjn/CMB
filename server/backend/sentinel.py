import sys
import os
import json
import httplib
import urllib
import datetime
import time
import threading
from threading import Thread
from util import *

sets = set()
mutex = threading.Lock()
session = getSession()

class Moniter(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.Port = 2375
        self._running = True
#        self.containers = []

    def getDockers(self):
        try:
            conn = httplib.HTTPConnection('172.29.152.181:2375')
            conn.request("GET","/containers/json?all=1")
            r1 = conn.getresponse()
        except Exception,e:
            print Exception,e
        raw = r1.read()
        data = json.loads(raw)
        for key in data:
            containerID = key['Id']
            containerName = key['Names'][0].split('/')[1]
            contaimerImage = key['Image']
            #contaienrState = key['State']
            containerStatus = key['Status']
            command = key['Command']

            mutex.acquire(2)
            sets.add(containerID)
            mutex.release()

        for item in sets:
            print item
        print "========================================="

    def terminate(self):
        self._running = False

    def run(self):
        while self._running:
            self.getDockers()
            time.sleep(10)

class Status(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.port = 2375
        self._running = True

    def Status(self):
        mutex.acquire(5)
        for item in sets:
            try:
                conn = httplib.HTTPConnection('172.29.152.181:2375')
                conn.request('GET',"/containers/%s/stats?stream=0"%(item))
                r2 = conn.getresponse()
            except Exception, e:
                print Exception, e
            d = json.loads(r2.read())
            systemTime = d["read"].split('.')[0]
            print "ContainerID: " , item
            print "System Time: " , systemTime
            if 'networks' in d:
                if 'eth0' in d['networks']:
                    networks = d['networks']
                    content = networks['eth0']
                    rx_bytes = content['rx_bytes']
                    tx_bytes = content['tx_bytes']
                    print "RX: ",rx_bytes
                    print "TX: ",tx_bytes
            cpu_stats = d['cpu_stats']
            cpu_usage = cpu_stats['cpu_usage']
            cpu_usage_in_user = cpu_usage['usage_in_usermode']
            cpu_total_usage = cpu_usage['total_usage']
            cpu_usage_in_kernelmode = cpu_usage['usage_in_kernelmode']

            print "CPU USERMODE: ", cpu_usage_in_user
            print "CPU KERMODE: ", cpu_usage_in_kernelmode
            print "CPU TOTAL: ", cpu_total_usage

            mem_stats = d['memory_stats']
            mem_usage = mem_stats['usage']
            #mem_limit = memory_stats['limit']

            #mem_percentage = round(float((float(mem_usage)/float(mem_limit))*100), 3)
            #mem_percentage = str(mem_precentage) + "%"

            print "MEM USAGE: ", mem_usage
            print "+++++++++++++++++++++++++++++++++++++++++++"
        mutex.release()

    def terminate(self):
        self._running = False

    def run(self):
        while self._running:
            self.Status()
            time.sleep(5)
def runs():
    m = Moniter()
    s = Status()
    m.start()
    s.start()
    #m.terminate()
    #s.terminate()
    m.join()
    s.join()
if __name__ == '__main__':
    runs()
