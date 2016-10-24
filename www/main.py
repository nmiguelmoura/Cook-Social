import os
import webapp2
import main_handler

# Defines de routers.
app = webapp2.WSGIApplication([("/", main_handler.MainHandler),
                               ],debug=True)