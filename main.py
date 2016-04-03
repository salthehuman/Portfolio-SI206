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
import webapp2
import jinja2
import logging
import os


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class CommonHandler(webapp2.RequestHandler):
    def get(self):
        html = self.request.path
        if html == '/':
            template = JINJA_ENVIRONMENT.get_template('templates/home.html')
            self.response.write(template.render({'title': 'HOME', 'page':'/home.html'}))    
        else:
            template = JINJA_ENVIRONMENT.get_template('templates/'+html)
            self.response.write(template.render({'title': str(html)[1:-5].upper(), 'page':str(html)}))

app = webapp2.WSGIApplication([
    ('/.*', CommonHandler)
], debug=True)
