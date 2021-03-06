import sys
import os
import datetime
#from datetime import datetime
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
        # render templates
        self.url_map.append(Rule("/about", endpoint='about'))
        self.url_map.append(Rule("/index",endpoint='daliySearch'))
        self.url_map.append(Rule("/search", endpoint='search'))
        self.url_map.append(Rule("/daliySearch", endpoint='daliySearch'))
        self.url_map.append(Rule("/monthlySearch", endpoint='monthlySearch'))
        self.url_map.append(Rule("/policy", endpoint='policy'))
        self.url_map.append(Rule("/tasklist", endpoint='tasklist'))
        self.url_map.append(Rule("/resources", endpoint='resources'))
        self.url_map.append(Rule("/updatePolicyPage", endpoint='updatePolicyPage'))
        self.url_map.append(Rule("/daliyBillDetail", endpoint='daliyBillDetail'))
        self.url_map.append(Rule("/monthlyBillDetail", endpoint='monthlyBillDetail'))
        self.url_map.append(Rule("/rankingList", endpoint='rankingList'))
        #Bills api
        self.url_map.append(Rule("/searchMonthlyBill", endpoint='searchMonBill'))
        self.url_map.append(Rule("/searchDailyBill", endpoint='searchDaiBill'))
        self.url_map.append(Rule("/dailyTaskDetail", endpoint='getDaidetail'))
        self.url_map.append(Rule("/monthlyBill", endpoint='getMonbill'))
        self.url_map.append(Rule("/dailyBill", endpoint='getDaibill'))
        self.url_map.append(Rule("/searchByImages", endpoint='seachByImages'))
        #Resources api
        self.url_map.append(Rule("/getMachine", endpoint='getMachine'))
        self.url_map.append(Rule("/getResources", endpoint='getResource'))
        #Policies api
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

    def daliyBillDetail(self, request):
        return self.render_template('daliyBillDetail.html', error=None, url=None)

    def rankingList(self, request):
        return self.render_template('rankingList.html', error=None, url=None)

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
                po['monPrice'] = row.monPrice
                po['aftPrice'] = row.aftPrice
                po['nigPrice'] = row.nigPrice
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
            if 'mon' in request.args.keys():
                mon = request.args['mon']
                item = self.session.query(MainPolicy).\
                       filter(MainPolicy.cpu_norm==cpu, MainPolicy.mem_norm==mem).\
                       update({'basePrice':basePrice, 'monPrice':mon})
            if 'aft' in request.args.keys():
                aft = request.args['aft']
                item = self.session.query(MainPolicy).\
                       filter(MainPolicy.cpu_norm==cpu, MainPolicy.mem_norm==mem).\
                       update({'basePrice':basePrice, 'aftPrice':aft})
            if 'nig' in request.args.keys():
                nig = request.args['nig']
                item = self.session.query(MainPolicy).\
                       filter(MainPolicy.cpu_norm==cpu, MainPolicy.mem_norm==mem).\
                       update({'basePrice':basePrice, 'nigPrice':nig})
            self.session.commit()
            return 'Operation Success'
        else:
            return "Opreation Error"

    @response
    def getMonbill(self, request):
        ret = ''
        if request.method == 'GET':
            mon = request.args['month']
            content = json.load(open("./json/monthlyBilling.json"))
            content['Cycle'] = mon
            ret = json.dumps(content)
        return ret

    def checkMon(self, start_time, end_time):
        ret = []
        today = datetime.datetime.now()
        cur_year = str(today).split('-')[0]
        cur_mon = str(today).split('-')[1]
        cur_day = str(today).split(' ')[0].split('-')[2]
        s_year, s_mon = start_time.split('-')
        e_year, e_mon = end_time.split('-')
        ss_year = int(s_year)
        ss_mon = int(s_mon)
        se_year = int(e_year)
        se_mon = int(e_mon)
        if int(e_year) > int(cur_year):
            se_year = int(cur_year)
            se_mon = int(cur_mon)
        if int(s_year) < int(cur_year):
            ss_year = int(cur_year)
            ss_mon = 1
        if int(e_year) < int(cur_year):
            return None
        if int(s_year) > int(cur_year):
            return None
        if int(ss_mon) >= int(cur_mon):
            return None
        if int(se_mon) >= int(cur_mon):
            se_mon = int(cur_mon) - 1
        for i in range(ss_mon, se_mon + 1):
            ret.append('%s-%s'%(str(cur_year), str(i)))
        return ret

    def checkDay(self, begin_date, end_date):
        date_list = []
        b_year, b_mon, b_day = begin_date.split("-")
        e_year, e_mon, e_day = end_date.split("-")

        boundary_date = datetime.datetime.now() - datetime.timedelta(days=90)
        bo_year, bo_mon, bo_day = str(boundary_date).split(" ")[0].split("-")
        if (datetime.datetime(int(b_year), int(b_mon), int(b_day), 12, 0, 0) - datetime.datetime(int(bo_year), int(bo_mon), int(bo_day), 12, 0, 0)).total_seconds() < 0:
            begin_date = str(boundary_date).split(" ")[0]
        begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        print begin_date
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        while begin_date <= end_date:
            date_str = begin_date.strftime("%Y-%m-%d")
            date_list.append(date_str)
            begin_date += datetime.timedelta(days=1)
        return date_list
            
    @response
    def searchMonBill(self, request):
        ret = ''
        if request.method =='GET':
            type = request.args['type']
            if type =='date':
                start_mon = request.args['start_mon']
                end_mon = request.args['end_mon']
                month = self.checkMon(start_mon, end_mon)
                if not month:
                    return "None data\n"
                #content = json.load(open('./json/mon_list.json'))
                #for item in content:
                #    item['Month'] = mon
                #    item['Total_Billing'] = random.randint(1010, 3030)
                i = 1
                content = []
                for mon in month:
                    content.append({"type":"M", "Month":mon, "ID":i, "Name":"TOTORO", "Total_Billing":random.randint(1100, 3030)})
                    i+=1
                ret = json.dumps(content)
                return ret
            if type =='job':
                self.zero.connect(backEnd)
                jobs = self.zero.get_jobs()
                job_ret = []
                for job in jobs:
                    job_info = {}
                    job_info["job_name"] = job
                    job_info["task_num"] = random.randint(1,5)
                    job_info["job_cost"] = random.randint(12, 40)
                    job_ret.append(job_info)
                ret = json.dumps(job_ret)
                return ret

    @response
    def searchDaiBill(self, request):
        ret = ''
        if request.method =='GET':
            type = request.args['type']
            if type == 'date':
               begin_time = request.args['start_date']
               end_time = request.args['end_date']
               ret = self.checkDay(begin_time, end_time)
               content = []
               i = 1
               for day in ret:
                   content.append({"type":"D", "Date":day, "ID":i, "Name":"TOTORO", "total":random.randint(15, 99)})
                   i+=1
               ret = json.dumps(content)
               return ret
            if type == 'job':
                self.zero.connect(backEnd)
                jobs = self.zero.get_jobs()
                job_ret = []                
                for job in jobs:
                    job_info = {}
                    job_info["job_name"] = job
                    job_info['task_num'] = random.randint(1, 5)
                    job_info["job_cost"] = random.randint(12, 40)
                    job_ret.append(job_info)
                ret = json.dumps(job_ret)
                return ret
    """
    can not make searchs from image_name to job_name
    """
    @response
    def seachByImages(self, request):
        ret = ''
        if request.method == 'GET':
            image_name = request.args['image']
            self.zero.connect(backEnd)
            jobs = self.zero.get_jobs()
            job_ret = []
            for job in jobs:
                job_info = {}
                job_info["job_name"] = job
                job_info['task_num'] = random.randint(1, 5)
                job_info["job_cost"] = random.randint(12, 40)
                job_ret.append(job_info)
            ret = json.dumps(job_ret)
            return ret


    @response
    def getDaibill(self, request):
        ret = ''
        if request.method == 'GET':
            date = request.args['date']
            content = json.load(open("./json/dailyBilling.json"))
            content['Date'] = date
            print content
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
        ret = []
        if request.method == 'GET':
            try:
                self.zero.connect(backEnd)
                jobs = self.zero.get_jobs()
                tasks = self.cass.get_taskID(jobs)
                tasks = json.loads(tasks)
                for job in jobs:
                    job_ret = {}
                    forTasks = tasks[job]
                    for item in forTasks:
                        unix_time = item['ts']['$date']
                        item['ts'] = unix_time
                    task_id = forTasks[0]['id']
                    host = self.zero.get_host(task_id)
                    for tk in forTasks:
                        tk['host'] = host
                        tk['cpu_used_in_user'] = 14800000
                        tk['cpu_used_in_ker'] = 28600000
                        tk['cpu_total_used'] = 3602000000
                        tk['mem_used_percentage'] = 0.7
                    job_ret['job_name'] = job
                    job_ret["job_info"] = forTasks
                    ret.append(job_ret)
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
