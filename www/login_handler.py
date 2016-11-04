import handler
import pre_cookie_handler
import pre_hash_tools
import db_query_users

class LoginHandler(handler.Handler):
    hashs = pre_hash_tools.HashTools()
    cookies = pre_cookie_handler.CookieHandler()
    query_users = db_query_users.DBQueryUsers()

    def get(self):
        if self.cookies.get_loginfo_cookie(self):
            self.redirect("/kitchen")
        else:
            self.render("login.html")

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")

        existing_user = self.query_users.search_user(username)

        if existing_user:
            if self.verify_password(existing_user, password):
                self.cookies.set_loginfo_cookie(self, str(existing_user.key().id()))
                self.redirect("/kitchen")
                return
        self.render('login.html', username=username, error_message="Invalid username or password.")


    def verify_password(self, existing_user, given_password):
        return self.hashs.check_secure_password(existing_user.username, given_password, existing_user.password)
