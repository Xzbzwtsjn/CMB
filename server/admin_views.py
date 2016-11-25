import sys
import os
import datetime
import simplejson as json
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Request, Response
from jinja2 import Environment, FileSystemLoader
from views_util import *
from conf import *
import shutil


class AdminViews:
    def __init__(self, request):
        self.url_map = []
        self.url_map.append(Rule("/admin/about", endpoint='aabout'))
        self.url_map.append(Rule("/admin/deploy", endpoint='deploy'))
        self.url_map.append(Rule("/admin/load", endpoint='load'))
        self.url_map.append(Rule("/admin/reload", endpoint='reload'))
        self.url_map.append(Rule("/admin/reload_latest", endpoint='reload_latest'))
        self.url_map.append(Rule("/admin/recover", endpoint='recover'))

        self.session = getSession()
        self.jinjia_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)

    def render_template(self, template_name, **context):
        t = self.jinjia_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    @response
    def aabout(self, request):
        return "about"
