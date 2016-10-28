import handler

class SignupHandler(handler.Handler):
    def get(self):
        self.render("sign_up.html")
