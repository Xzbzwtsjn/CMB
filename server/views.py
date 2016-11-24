import sys
import os
import simplejson as json
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Request, Response
from views_util import *
from conf import *
from jinja2 import Environment, FileSystemLoader

class Views:
    def __init__(self, request):
        self.url_map = []

        self.url_map.append(Rule("/about", endpoint='about'))
        self.url_map.append(Rule("/index",endpoint='search'))
        self.url_map.append(Rule("/search", endpoint='search'))
        self.url_map.append(Rule("/policy", endpoint='policy'))
        self.url_map.append(Rule("/resources", endpoint='resources'))
        self.url_map.append(Rule("/updatePolicyPage", endpoint='updatePolicyPage'))

        self.url_map.append(Rule("/searchMonthlyBill", endpoint='searchMonBill'))
        self.url_map.append(Rule("/searchDailyBill", endpoint='searchDaiBill'))
        self.url_map.append(Rule("/monthlyBill", endpoint='getMonbill'))
        self.url_map.append(Rule("/dailyBill", endpoint='getDaibill'))

        self.url_map.append(Rule("/getMachine", endpoint='getMachine'))
        self.url_map.append(Rule("/getResouces", endpoint='getResource'))

        self.url_map.append(Rule("/updatePolicy", endpoint = 'updatePolicy'))
        self.url_map.append(Rule("/getPolicy", endpoint = 'getPolicy'))


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

    @response
    def getPolicy(self, request):
        pass

    @response
    def updatePolicy(self, request):
        ret = ''
        if request.method == 'GET':
            cpu = request.args['cpu']
            mon = request.args['mem']
            basePrice = request.args['base']
            usePrice = request.args['use']
            weight = raquest.args['weight']
            item = self.session.query()

    @response
    def getMonbill(self, request):
        ret = ''
        if request.method == 'GET':
            print request.args.keys()
            mon = request.args['keyword']
            type = request.args['type']
            if type == 'date':
                content = json.load(open("./json/monthlyBilling.json"))
                print content
                ret = json.dumps(content)
        #return self.render_template('resources.html', error=None, url=None)
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
    def getDaibill(self, request):
        ret = ''
        if request.method =='GET':
            date = request.args['keyword']
            type = request.args['type']
            if type == 'date':
                content = json.load(open("./json/dailyBilling.json"))
                ret = json.dumps(content)
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
                ret.append(host)
        ret = json.dumps(ret)
        return ret

    @response
    def getMachine(self, request):
        ret = ''
        leader = CurrentLeader()
        if request.method == 'GET':
            pid = request.args['pid']
            address = pid.split('@')[1]
            ip, port = address.split(':')
            ret = getHttpConnection(ip, port, '/state')
        return ret
