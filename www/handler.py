# -*- coding: utf-8 -*-

import os
import webapp2
import jinja2

# Setup jinja2.
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

class Handler(webapp2.RequestHandler):
    """Class that renders and writes html pages. Copied from Udacity course."""

    # Write message on html page.
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    # Jinja2 renders template.
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    # Write html page with specified template.
    def render(self,template,**kw):
        self.write(self.render_str(template, **kw))