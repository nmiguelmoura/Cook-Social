import handler
import prefabs.cookie_handler


class LogoutHandler(handler.Handler):
    cookie = prefabs.cookie_handler.CookieHandler()

    def get(self):
        self.cookie.clear_loginfo_cookie(self)
        self.redirect("/")
