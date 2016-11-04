import handler
import pre_cookie_handler

class LogoutHandler(handler.Handler):
    cookie = pre_cookie_handler.CookieHandler()

    def get(self):
        self.cookie.clear_loginfo_cookie(self)
        self.redirect("/")
