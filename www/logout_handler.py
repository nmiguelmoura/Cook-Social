import handler
import prefabs.cookie_handler


class LogoutHandler(handler.Handler):
    """Class that allows a user to logout."""

    cookie = prefabs.cookie_handler.CookieHandler()

    def get(self):
        # Clear cookie from system.
        self.cookie.clear_loginfo_cookie(self)

        # Redirect to index page.
        self.redirect("/")
