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
import database
import email
import string
from google.appengine.api import mail
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

class LogSenderHandler(InboundMailHandler):
    def receive(self, message):
        logging.info("Recieved a message from: " + message.sender)
        # Get the body text from the e-mail
        bodies = message.bodies('text/plain') #generator
        #logging.info("message = %s " % message)
        #logging.info("message body = %s " % message.body)
        for content_type, body in bodies:
            logging.info(body.decode())
            body_text = body.decode().split('\n')
            #logging.info("body_text = %s " % body_text)

            # Loop through each line in the e-mail and discard a line if it is blank
            for line in body_text:
                logging.info("body_text = %s " % body_text)
                if line != ',':
                    #logging.info(line)
                    # Split the current line based on the ": " value and only let it be done once
                    splitline = line.split(': ', 1)
                    logging.info("splitline")
                    logging.info(" ".join(splitline))
                    logging.info("splitline[0]")
                    logging.info(splitline[0])
                    logging.info("splitline[1]")
                    logging.info(splitline[1])

                    # Check to see which line we now have the details for and place value into the correct variable
                    if splitline[0] == "Year":
                        user_year = splitline[1]
                    if splitline[0] == "Branch":
                        user_branch = splitline[1]
                    if splitline[0] == "Course":
                        user_course = splitline[1]
                    if splitline[0] == "Last Name":
                        user_lastname = splitline[1]
                    if splitline[0] == "First Name":
                        user_firstname = splitline[1]
                    if splitline[0] == "College":
                        user_college = splitline[1]
                    if splitline[0] == "Gmail Address":
                        user_email = splitline[1]

        values = database.Student(year = user_year,
                                  branch = user_email,
                                  course = user_course,
                                  lastname = user_lastname,
                                  firstname = user_firstname,
                                  college = user_college,
                                  email = user_email)
        values.put()
        logging("values : ")
        logging(values)

app = webapp2.WSGIApplication([LogSenderHandler.mapping()], debug=True)
