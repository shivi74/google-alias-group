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
import webapp2
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class LogSenderHandler(InboundMailHandler):
    def receive(self, mail_message):
        logging.info("Received a message from: " + mail_message.sender)
        msg = email.message_from_string(self.request.body)
        html_bodies = message.bodies('text/html')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    (LogSenderHandler.mapping())
], debug=True)
