#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging
from os.path import join, dirname
import sys

from django.conf import settings
import webapp2

#class MainHandler(webapp2.RequestHandler):
#    def get(self):
#        self.response.write('Hello world!')
#
#app = webapp2.WSGIApplication([
#    ('/', MainHandler)
#], debug=True)


# add local modules
sys.path.insert(0, join(dirname(__file__), 'python'))

logging.getLogger().setLevel(logging.DEBUG)

# Django Settings
settings.configure(TEMPLATE_DIRS=(join(dirname(__file__), 'templates'),))

### Variables
handlers = []

### Main
app = webapp2.WSGIApplication([
    webapp2.Route(r'/api/todos/<id_:\d+>', 'todo_api.Handler'),
    webapp2.Route(r'/api/todos', 'todo_api.Handler'),
    webapp2.Route(r'/api/channel/<client_id:.*>', 'channel_api.Handler'),
    webapp2.Route(r'/api/channel', 'channel_api.Handler'),
    webapp2.Route(r'/_ah/channel/connected/', 'channel_api.OnConnect'),
    webapp2.Route(r'/_ah/channel/disconnected/', 'channel_api.OnDisconnect'),

    webapp2.Route(r'/', 'index_html.Handler')
], debug=True)
