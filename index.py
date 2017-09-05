#-*- coding:utf-8 -*-
# import django

# def app(environ, start_response):
#     status = '200 OK'
#     headers = [('Content-type', 'text/html')]
#     start_response(status, headers)
#     # body=["Welcome to Baidu Cloud!\n"]
#     body=['django version: {0} \n'.format(django.get_version())]
#     return body

# application = WSGIApplication(app)

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from bae.core.wsgi import WSGIApplication
from mysite import wsgi

application = WSGIApplication(wsgi.application)
