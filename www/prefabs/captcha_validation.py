# -*- coding: utf-8 -*-

import urllib
import json
import secret_codes
from google.appengine.api import urlfetch

class CaptchaValidation():
    secret = secret_codes.SecretCode()

    def __init__(self):
        pass

    def validate(self, handler, user_response):
        data = data = {
            "secret": self.secret.get_recaptcha_code(),
            "response": user_response
        }

        # Assemble data to send to post method.
        recaptcha_validation = {
            "response": False,
            "info": "Por favor assinale a caixa acima."
        }

        try:
            # Try to post data and wait for response
            form_data = urllib.urlencode(data)
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(
                url='https://www.google.com/recaptcha/api/siteverify',
                payload=form_data,
                method=urlfetch.POST,
                headers=headers)

            # Json loading.
            validation = json.loads(result.content)
            if validation["success"]:
                # If answer is True, pass it to recaptcha_validation and
                # erase message
                recaptcha_validation = {
                    "response": True,
                    "info": ""
                }

            return recaptcha_validation

        except urlfetch.Error:
            # If can't validate recaptcha answer
            handler.redirect("/messagetouser?id=unexpected_error")
            return





