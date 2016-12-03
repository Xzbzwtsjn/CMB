#! /usr/bin/env python
#-*-coding:utf-8-*-
import sys
import os
import httplib
import urllib
import json

class SlaveOutput(object):
    """
    Input  Chronos的JobName
    Output JobName's stdout and stderr in container
    """
    def __init__(self, arg):
        super(SlaveOutput, self).__init__()
        #self.Chronos_jobName = "ChronosTask:"+arg
        self.Chronos_taskID = arg
        """
        节点更新请改masterIP
        """
        self.MasterIP=['172.29.152.185:5050','172.29.152.186:5050','172.29.152.188:5050']

    def obtain_Slave_ID(self):
        """
        获取slave节点的ID
        """
        try:
            conn=httplib.HTTPConnection(self.MasterIP[0])
            conn.request("GET", "/master/tasks.json?limit=400")
            r1 = conn.getresponse()
        except Exception,e:
            print 'get http failed\n'

        if r1.status == 200:
            raw = r1.read() #str
            data=json.loads(raw)
            for item in data["tasks"]:
                if item["id"] == self.Chronos_taskID:
                    #print item['slave_id']
                    conn.close()
                    return item['slave_id']
            return None
            conn.close()
        else:
            return None
            conn.close()


    def obtain_Slave_IP_PORT(self):
        """
        根据slaveID, 获取slave节点的IP
        """
        slaveID=self.obtain_Slave_ID()
        #print slaveID
        if slaveID == None:
            return None
        try:
            conn=httplib.HTTPConnection(self.MasterIP[0])
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

    def obtain_container_path(self):
        """
        获取容器对应的日志绝对路径
        """
        slave=self.obtain_Slave_IP_PORT()
        print "slaveID: ",slave
        if slave == None:
            return None
        try:
            conn=httplib.HTTPConnection(slave)
            conn.request("GET", "/state.json")
            r1=conn.getresponse()
        except Exception,e:
            print 'get http failed\n'

        if r1.status==200:
            raw=r1.read()
            data=json.loads(raw)
            #print data
            for item in data['frameworks']:
                if item['name']=="chronos-2.4.0":
                    for executors in item['executors']:
                        for task in executors['tasks']:
                            if task['id'] == self.Chronos_taskID:
                                return executors['directory'],slave
                                conn.close()
                    for executors in item['completed_executors']:
                        for task in executors['completed_tasks']:
                            if task['id'] == self.Chronos_taskID:
                                return executors['directory'],slave
                                conn.close()

            for item in data['completed_frameworks']:
                if item['name']=="chronos-2.4.0":
                    for completed_executors in item['completed_executors']:
                        for task in completed_executors['completed_tasks']:
                            if task['id']==self.Chronos_taskID:
                                return completed_executors['directory'],slave
                                conn.close()
            return None
            conn.close()
        else:
            return None
            conn.close()

    def obtain_Log_stderr(self):
        """
        获取stderr日志
        """
        if self.obtain_container_path()!= None:
            directory,slave = self.obtain_container_path()
        else:
            return -1
        #print directory,slave
        path='/files/download?path='+directory+'/stderr'
        try:
            conn=httplib.HTTPConnection(slave)
            conn.request("GET", path)
            r1=conn.getresponse()
        except Exception,e:
            print 'get http failed\n'

        if r1.status==200:
            return r1.read()
            conn.close()
        else:
            return -1
            conn.close()

    def obtain_Log_stdout(self):
        """
        获取stdout日志
        """
        if self.obtain_container_path() !=None:
            directory,slave = self.obtain_container_path()
        else:
            return -1
        path='/files/download?path='+directory+'/stdout'
        try:
            conn=httplib.HTTPConnection(slave)
            conn.request("GET", path)
            r1=conn.getresponse()
        except Exception,e:
            print 'get http failed\n'

        if r1.status==200:
            return r1.read()
            conn.close()
        else:
            return -1
            conn.close()

if __name__ == '__main__':
    """
    测试
    主要调用obtain_Log_stderr()获取stderr日志,
    调用obtain_Log_stdout()获取stdout日志,
    其它函数不用管
    """
    #jobID=sys.argv[1]
    jobID="ct:1479283556402:0:test-11-16-0:"
    test=SlaveOutput(jobID)
    #print test.obtain_Log_stderr()
    print "~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~~*~*~*~*~*~*"
    print test.obtain_Log_stdout()
    #test.obtain_Log_stdout()
