import handler

class LoginHandler(handler.Handler):
    def get(self):
        self.render("login.html")
