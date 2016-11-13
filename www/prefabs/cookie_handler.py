import hash_tools


class CookieHandler:
    """Class that handles create, read and clear cookie."""
    hashs = None

    def __init__(self):
        # Instantiate HashTools class.
        self.hashs = hash_tools.HashTools()
        pass

    def get_loginfo_cookie(self, handler):
        # Get user id stored in cookie.
        log_info = handler.request.cookies.get("loginfo")

        id = None
        if log_info:
            # Check if cookie is correct. Compare user id with hashed code
            # to check if user id is legit.
            id = self.hashs.check_cookie_val(log_info)

        # Return user id if exists or None if it doesn't.
        return id

    def set_loginfo_cookie(self, handler, user_id):
        # Store cookie with hashed user id for security purposes.
        handler.response.headers["Content-Type"] = "text/html"
        handler.response.headers.add_header("Set-Cookie",
                                            "loginfo = %s" % self.hashs.make_secure_value(
                                                user_id))

    def clear_loginfo_cookie(self, handler):
        # Clear cookie from system.
        # To be used on logout.
        handler.response.headers["Content-Type"] = "text/html"
        handler.response.headers.add_header("Set-Cookie", "loginfo=; path=/;")
