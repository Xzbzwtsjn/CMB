import sys
import os
import urlparse
import simplejson as json
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.serving import run_simple
from views import Views
from conf import *
from views_util import *
from admin_views import *

def application(environ, start_response):
    request = Request(environ)
    view = Views(request)
    admin_view = AdminViews(request)
    url_map = Map(view.url_map + admin_view.url_map)
    adapter = url_map.bind_to_environ(request.environ)
    try:
        endpoint, values = adapter.match()
        handler = getattr(view, endpoint)
        response = handler(request, **values)
    except HTTPException, e:
        return e(environ, start_response)
    return response(environ, start_response)

def create_app():
    app = application
    app = SharedDataMiddleware(app, {'/static':os.path.join(os.path.dirname(__file__),'static')})
    return app

if __name__ == '__main__':
    if not os.path.exists(dbRoot):
        from sqlite_util import initDB
        initDB()
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)
