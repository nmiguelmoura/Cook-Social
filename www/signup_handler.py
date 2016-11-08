import handler
import db_model_users
import prefabs.db_query_users
import prefabs.cookie_handler
import prefabs.hash_tools
import prefabs.signup_validation


class SignupHandler(handler.Handler):
    validation = prefabs.signup_validation.SignupValidation()
    hashs = prefabs.hash_tools.HashTools()
    query_users = prefabs.db_query_users.DBQueryUsers()
    cookies = prefabs.cookie_handler.CookieHandler()

    def get(self):
        if self.cookies.get_loginfo_cookie(self):
            self.redirect("/kitchen")
        else:
            self.render("sign_up.html")

    def post(self):
        username = self.request.get("username")
        email = self.request.get("email")
        password = self.request.get("password")
        verify = self.request.get("verify")

        username_validation = self.validation.username_verify(username)
        email_validation = self.validation.email_verify(email)
        password_validation = self.validation.test_password(password, verify)

        if username_validation["response"] and email_validation["response"] and password_validation["response"]:
            username_available = self.check_username_availability(username)
            if username_available:
                self.store_data(username, email, password)
            else:
                message="This username already exists. Please choose another one."
                self.render('sign_up.html', username=username, email=email, error_username=message)
        else:
            self.render('sign_up.html', username=username, email=email, error_username=username_validation["info"], error_email=email_validation["info"], error_password=password_validation["info"])

    def check_username_availability(self, username):
        user = self.query_users.search_user(username)
        return False if user else True

    def store_data(self, username, email, password):
        hashed_password = self.hashs.make_secure_password(username, password)
        users = db_model_users.UsersDBModel(username=username, email=email, password=hashed_password, pointed=[''], comments=[''])
        users.put()
        user_id = str(users.key().id())
        self.set_cookie(user_id)

        self.redirect("/kitchen")

    def set_cookie(self, user_id):
        self.cookies.set_loginfo_cookie(self, user_id)
