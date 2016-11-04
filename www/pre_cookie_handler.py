import pre_hash_tools

class CookieHandler:
    hashs = None

    def __init__(self):
        self.hashs = pre_hash_tools.HashTools()
        pass

    def get_loginfo_cookie(self, handler):
        log_info = handler.request.cookies.get("loginfo")

        id = None
        if log_info:
            id = self.hashs.check_cookie_val(log_info)

        return id

    def set_loginfo_cookie(self, handler, user_id):
        handler.response.headers["Content-Type"] = "text/html"
        handler.response.headers.add_header("Set-Cookie", "loginfo = %s" % self.hashs.make_secure_value(user_id))

    def clear_loginfo_cookie(self, handler):
        handler.response.headers["Content-Type"] = "text/html"
        handler.response.headers.add_header("Set-Cookie", "loginfo=; path=/;")
