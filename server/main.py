import sys
import os
import urlparse
import simplejson as json
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.serving import run_simple
from views import Views

#views = views()
#url_map = Map(views.url_map)

def application(environ, start_response):
    request = Request(environ)
    view = Views(request)
    url_map = Map(view.url_map)
    adapter = url_map.bind_to_environ(request.environ)
    try:
        endpoint, values = adapter.match()
        handler = getattr(view, endpoint)
        response = handler(request, **values)
        print endpoint,values
    except HTTPException, e:
        return e(envrion, start_response)
    return response(environ, start_response)

def create_app():
    app = application
    return app

if __name__ == '__main__':
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)