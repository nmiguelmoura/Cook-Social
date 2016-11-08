import handler
import prefabs.db_query_users
import prefabs.cookie_handler
import prefabs.hash_tools
import prefabs.signup_validation


class EditPersonalHandler(handler.Handler):
    validation = prefabs.signup_validation.SignupValidation()
    cookies = prefabs.cookie_handler.CookieHandler()
    query_users = prefabs.db_query_users.DBQueryUsers()
    hashs = prefabs.hash_tools.HashTools()

    def get(self):
        log_info = self.cookies.get_loginfo_cookie(self)
        if log_info:
            user_data = self.query_users.search_user_by_id(log_info)
            self.render("edit_personal_data.html", email=user_data.email)
        else:
            self.render("login.html")

    def post(self):
        log_info = self.cookies.get_loginfo_cookie(self)
        user_data = self.query_users.search_user_by_id(log_info)

        email = self.request.get('email')
        password = self.request.get('password')
        verify = self.request.get('verify')

        email_validation = self.validation.email_verify(email)

        password_validation = {"response": "ok", "info": ""}
        if password:
            password_validation = self.validation.test_password(password, verify)

        if email_validation["response"] and password_validation["response"]:
            self.store_data(user_data, email, password)
        else:
            self.render("edit_personal_data.html", email=email, error_email=email_validation["info"], error_password=password_validation["info"])

    def store_data(self, user_data, email, password):
        if email:
            user_data.email = email

        if password:
            user_data.password = self.hashs.make_secure_password(user_data.username, password)

        user_data.put()
        self.redirect("/kitchen")
