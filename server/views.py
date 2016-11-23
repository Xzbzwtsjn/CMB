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
        self.url_map.append(Rule("/monthlyBill", endpoint='getMonbill'))
        self.url_map.append(Rule("/api/monthlyBill", endpoint='api_getMonbill'))
        self.url_map,append(Rule("/dailyBill", endpoint='getDailybill'))
	self.url_map.append(Rule("/api/dailyBill", endpoint='api_getDailybill'))
        self.url_map.append(Rule("/getMachine", endpoint = 'getMachine'))
	self.url_map.append(Rule("/api/getMachine", endpoint = 'api_getMachine'))
        self.url_map.append(Rule("/updatePolicy", endpoint = 'updatePolicy'))
	self.url_map.append(Rule("/api/updatePolicy", endpoint = 'api_updatePolicy'))
        self.url_map.append(Rule("/getPolicy", endpoint = 'getPolicy'))
	self.url_map.append(Rule("/api_getPolicy", endpoint = 'api_getPolicy'))

        self.session = getSession()
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),  autoescape=True)

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def about(self, request):
        print "hello world\n"
        return Response("{'a':'hello'}",mimetype='text/plain')

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
        error= ''
        url = ''
        if request.method == 'GET':
            print request.args.keys()
            mon = request.args['keyword']
            type = request.args['type']
            if type == 'date':
                content = json.load(open("test.json"))
                print content
                ret = json.dumps(content)
        return self.render_template('resources.html', error=None, url=None)
#       return ret

    @response
    def getDailybill(self, request):
        ret = ''
        if request.method =='GET':
            date = request.args['keyword']
            type = request.args['type']
            if type == 'date':
                content = json.load(open("dailyBilling.json"))
                ret = json.dumps(content)
            return ret

    @response
    def getMachine(self, request):
        ret = ''
        leader = CurrentLeader()
        if request.method == 'GET':
            ret = getHttpConnection(leader, MesosMasterPort, '/slaves')
            print ret
        return ret
