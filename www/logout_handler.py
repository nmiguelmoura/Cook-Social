# -*- coding: utf-8 -*-

import handler
import prefabs.cookie_handler


class LogoutHandler(handler.Handler):
    """Class that allows a user to logout."""

    cookie = prefabs.cookie_handler.CookieHandler()

    def get(self):
        # Get user id stored in cookie.
        user_id = self.cookie.get_loginfo_cookie(self)

        if user_id:
            # Clear cookie from system.
            self.cookie.clear_loginfo_cookie(self)

            # Redirect to index page.
            self.redirect("/")

        else:
            self.redirect("/login")
