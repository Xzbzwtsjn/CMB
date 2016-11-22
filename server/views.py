import sys
import os
import simplejson as json
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Request, Response
from views_util import response, getHttpConnection, CurrentLeader
from conf import *
class Views:
    def __init__(self, request):
        self.url_map = []
        self.url_map.append(Rule("/about", endpoint = 'about'))
        self.url_map.append(Rule("/monthlyBill", endpoint ='getMonbill'))
        self.url_map.append(Rule("/dailyBill", endpoint = 'getDailybill'))
        self.url_map.append(Rule("/getMachine", endpoint = 'getMachine'))
        self.url_map.append(Rule("/updatePolicy", endpoint = 'updatePolicy'))

    def about(self, request):
        print "hello world\n"
        return Response("{'a':'hello'}",mimetype='text/plain')

    @response
    def getMonbill(self, request):
        ret = ''
        if request.method == 'GET':
            print request.args.keys()
            mon = request.args['keyword']
            type = request.args['type']
            if type == 'date':
                content = json.load(open("test.json"))
                print content
                ret = json.dumps(content)
        return ret

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
