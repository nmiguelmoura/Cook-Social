# -*- coding: utf-8 -*-

import re


class SignupValidation:
    """Class that performs validation over signup data using regular
    expressions."""

    def __init__(self):
        pass

    def username_verify(self, username):
        # Verify if username string has more than 3 characters and less than 20.
        # Verify if username string has only alphanumeric values, not spaces
        # and special characters.
        # If username valid, return it, else return error message.
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        response = USER_RE.match(username)
        info = "" if response else u"Nome de utilizador inválido. Por favor insira um nome de utilizador com pelo menos 4 caractéres e sem espaços."
        return {"response": response, "info": info}

    def check_password(self, password):
        # Verify if password string has more than 3 characters and less than 20.
        # If password is valid, return it, else return error message.
        PASS_RE = re.compile(r"^.{3,20}$")
        if password != "":
            response = PASS_RE.match(password)
            return {"response": response,
                    "info": "" if response else u"Palavra-passe inválida."}

        return {"response": None, "info": u"Palavra-passe inválida."}

    def compare_password(self, password, verify):
        if (password == verify):
            # If password and verification password match, return True
            # in response.
            return {"response": True, "info": ""}

        # If password and verification password don't match, return
        # error message.
        return {"response": False, "info": u"As palavras-passe não coincidem."}

    def test_password(self, password, verify):
        # Check if password is valid.
        check_val = self.check_password(password)

        if check_val["response"]:
            # If password is valid, compare password to verification password.
            comparison = self.compare_password(password, verify)
            return {"response": comparison["response"],
                    "info": comparison["info"]}

        return {"response": False, "info": check_val["info"]}

    def email_verify(self, email):
        # Verify if given email is in form character@character.character.
        # If email is valid, return it, else return error message.
        EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
        response = EMAIL_RE.match(email)
        info = "" if response else u"Email inválido."
        return {"response": response, "info": info}
