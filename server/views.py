import sys
import os
import datetime
import random
import simplejson as json
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Request, Response
from views_util import *
from conf import *
from jinja2 import Environment, FileSystemLoader
import zerorpc

class Views:
    def __init__(self, request):
        self.url_map = []
        self.zero = zerorpc.Client()

        self.url_map.append(Rule("/about", endpoint='about'))
        self.url_map.append(Rule("/index",endpoint='daliySearch'))
        #self.url_map.append(Rule("/search", endpoint='search'))
        self.url_map.append(Rule("/daliySearch", endpoint='daliySearch'))
        self.url_map.append(Rule("/monthlySearch", endpoint='monthlySearch'))
        self.url_map.append(Rule("/policy", endpoint='policy'))
        self.url_map.append(Rule("/tasklist", endpoint='tasklist'))
        self.url_map.append(Rule("/resources", endpoint='resources'))
        self.url_map.append(Rule("/updatePolicyPage", endpoint='updatePolicyPage'))
        self.url_map.append(Rule("/daliyBillDetail", endpoint='daliyBillDetail'))
        self.url_map.append(Rule("/monthlyBillDetail", endpoint='monthlyBillDetail'))

        self.url_map.append(Rule("/searchMonthlyBill", endpoint='searchMonBill'))
        self.url_map.append(Rule("/searchDailyBill", endpoint='searchDaiBill'))
        self.url_map.append(Rule("/dailyDetail", endpoint='getDaidetail'))
        self.url_map.append(Rule("/monthlyBill", endpoint='getMonbill'))
        self.url_map.append(Rule("/dailyBill", endpoint='getDaibill'))

        self.url_map.append(Rule("/getMachine", endpoint='getMachine'))
        self.url_map.append(Rule("/getResources", endpoint='getResource'))

        self.url_map.append(Rule("/updatePolicy", endpoint='updatePolicy'))
        self.url_map.append(Rule("/getPolicy", endpoint='getPolicy'))
        self.url_map.append(Rule("/invalid_policy",endpoint='invalidPolicy'))
        self.url_map.append(Rule("/setPair", endpoint = 'setPair'))

        self.session = getSession()
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),  autoescape=True)

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def about(self, request):
        print "hello world\n"
        return Response("{'a':'hello'}",mimetype='text/plain')

    def search(self, request):
        return self.render_template('search.html', error=None, url=None)

    def policy(self, request):
        return self.render_template('policy.html', error=None, url=None)

    def resources(self, request):
        return self.render_template('resources.html', error=None, url=None)

    def updatePolicyPage(self, request):
        return self.render_template('updatepolicy.html', error=None, url=None)

    def daliyBillDetail(self, request):
        return self.render_template('daliyBillDetail.html', error=None, url=None)

    def monthlyBillDetail(self, request):
        return self.render_template('monthlyBillDetail.html', error=None, url=None)

    def daliySearch(self, request):
        return self.render_template('daliySearch.html', error=None, url=None)

    def monthlySearch(self,request):
        return self.render_template('monthlySearch.html', error=None, url=None)

    def tasklist(self, request):
	return self.render_template('tasklist.html', error=None, url=None)

    @response
    def getPolicy(self, request):
        ret = []
        if request.method =='GET':
            i = 1
            for row in self.session.query(MainPolicy).order_by(MainPolicy.cpu_norm):
                po = {}
                po['id'] = row.id
                po['cpu'] = row.cpu_norm
                po['mem'] = row.mem_norm
                po['basePrice'] = row.basePrice
                po['userPrice'] = row.userPrice
                pe = {}
                pe['%s'%(i)] = po
                ret.append(pe)
                i+=1
            ret = json.dumps(ret)
            return ret

    @response
    def updatePolicy(self, request):
        ret = ''
        if request.method == 'GET':
            cpu = request.args['cpu']
            mem = request.args['mem']
            basePrice = request.args['base']
            userPrice = request.args['use']
            item = self.session.query(MainPolicy).filter(MainPolicy.cpu_norm==cpu, MainPolicy.mem_norm==mem).update({'basePrice':basePrice, 'userPrice':userPrice})
            self.session.commit()
            return 'Operation Success'
        else:
            return "Opreation Error"

    @response
    def getMonbill(self, request):
        ret = ''
        if request.method == 'GET':
            print request.args.keys()
            mon = request.args['month']
            #type = request.args['type']
            #if type == 'date':
            content = json.load(open("./json/monthlyBilling.json"))
            print content
            ret = json.dumps(content)
        return ret

    @response
    def searchMonBill(self, request):
        ret = ''
        if request.method =='GET':
            type = request.args['type']
            if type =='date':
                content = json.load(open('./json/mon_list.json'))
                ret = json.dumps(content)
                return ret
            if type =='job':
                self.zero.connect(backEnd)
                jobs = self.zero.get_jobs()
                job_info = {}
                for job in jobs:
                    job_info[job]={'cpu_in_user':random.randint(1470000,1570000), \
                                     'cpu_in_kernel':random.randint(12300000,16900000), \
                                     'cpu_total':354123000, \
                                     'mem_used_precent':0.5, \
                                     'cost':random.randint(12, 40)}
                ret = json.dumps(job_info)
                return ret

    @response
    def searchDaiBill(self, request):
        ret = ''
        if request.method =='GET':
            type = request.args['type']
            if type == 'date':
               content = json.load(open('./json/day_list.json'))
               ret = json.dumps(content)
               return ret
            if type == 'job':
                self.zero.connect(backEnd)
                jobs = self.zero.get_jobs()
                job_info = {}
                for job in jobs:
                    job_info[job]={'cpu_in_user':random.randint(1470000,1570000), \
                                   'cpu_in_kernel':random.randint(12300000,16900000), \
                                   'cpu_total':354123000, \
                                   'mem_used_precent':0.5, \
                                   'cost':random.randint(12, 40)}
                ret = json.dumps(job_info)
                return ret

    @response
    def getDaibill(self, request):
        ret = ''
        if request.method == 'GET':
            date = request.args['date']
            content = json.load(open("./json/dailyBilling.json"))
            ret = json.dumps(content)
        return ret

    @response
    def getDaidetail(self, request):
        ret = ''
        if request.method == 'GET':
            jobID = request.args['jobID']
            content = json.load(open("./json/taskDetail.json"))
            ret = json.dumps(content)
        return ret

    @response
    def searchDailyBill(self, request):
        ret = ''
        if request.method =='GET':
            type = request.args['type']
            if type == 'date':
                content = json.load(open('./json/day_list.json'))
                ret = json.dumps(content)
        return ret

    @response
    def getResource(self, request):
        ret = []
        leader = CurrentLeader()
        if request.method =='GET':
            ans = getHttpConnection(leader, MesosMasterPort,'/slaves')
            data = json.loads(ans)
            for item in data['slaves']:
                host = {}
                host['hostname'] = item['hostname']
                host['pid'] = item['pid']
                host['active'] = item['active']
                host['id'] = item['id']
                host['resources'] = item['resources']
                ret.append(host)
        ret = json.dumps(ret)
        return ret

    @response
    def getMachine(self, request):
        self.cass = zerorpc.Client()
        self.cass.connect("tcp://%s:%s"%(Cassandra, CassandraListenPort))
        ret = {}
        if request.method == 'GET':
            try:
                self.zero.connect(backEnd)
                jobs = self.zero.get_jobs()
                tasks = self.cass.get_taskID(jobs)
                tasks = json.loads(tasks)
                for job in jobs:
                    forTasks = tasks[job]
                    task_id = forTasks[0]['id']
                    print task_id
                    host = self.zero.get_host(task_id)
                    forTasks.append({'host':host, \
                                     'cpu_used_in_user':14800000, \
                                     'cpu_used_in_ker':286000000, \
                                     'cpu_total_uesd':360200000, \
                                     'mem_uesd_percentage':0.7})
                    ret[job] = forTasks
                    """
                    JobTotasks only could be showed unix time, other hosts' info can't be showed
                    """
                ret = json.dumps(ret)
                return ret
            except Exception, e:
                print e
    @response
    def invalidPolicy(self, request):
        ret = ''
        if request.method == 'GET':
            id = request.args['id']
            self.session.query(MainPolicy).filter(MainPolicy.id==id).update({'invalid':1,'opType':"cancel"})
            self.session.commit()
            return 'Operation Success'
        else:
            return 'Operation Error'

    @response
    def setPair(self, request):
        ret = ''
        if request.method == 'GET':
            key = request.args['key']
            value = request.args['value']
            self.session.query(Pair).filter(Pair.key==key).update({'value':value})
            self.session.commit()
            return 'Operation Success'
        else:
            return "Operation Error"
