import handler

class ForgotPasswordHandler(handler.Handler):
    def get(self):
        self.render("forgot_password.html")
