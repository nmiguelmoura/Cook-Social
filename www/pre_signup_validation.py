import re

class SignupValidation:
    def __init__(self):
        pass

    def username_verify(self, username):
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        response = USER_RE.match(username)
        info = "" if response else "Invalid username"
        return {"response": response, "info": info}

    def check_password(self, password):
        PASS_RE = re.compile(r"^.{3,20}$")
        if password != "":
            response = PASS_RE.match(password)
            return {"response": response, "info": "" if response else "Invalid password"}

        return {"response": None, "info": "Invalid password."}

    def compare_password(self, password, verify):
        if(password == verify):
            return {"response": True, "info": ""}

        return {"response": False, "info": "Verification password don't match."}

    def test_password(self, password, verify):
        check_val = self.check_password(password)
        if check_val["response"]:
            comparison = self.compare_password(password, verify)
            return {"response": comparison["response"], "info": comparison["info"]}

        return {"response": False, "info": check_val["info"]}

    def email_verify(self, email):
        EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
        response = EMAIL_RE.match(email)
        info = "" if response else "Invalid email."
        return {"response": response, "info": info}
