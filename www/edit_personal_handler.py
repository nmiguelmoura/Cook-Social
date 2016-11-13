import handler
import prefabs.db_query_users
import prefabs.cookie_handler
import prefabs.hash_tools
import prefabs.signup_validation


class EditPersonalHandler(handler.Handler):
    """Class that allows user to edit personal data like email and password."""

    validation = prefabs.signup_validation.SignupValidation()
    cookies = prefabs.cookie_handler.CookieHandler()
    query_users = prefabs.db_query_users.DBQueryUsers()
    hashs = prefabs.hash_tools.HashTools()

    def get(self):
        # Get user id stored in cookies.
        log_info = self.cookies.get_loginfo_cookie(self)

        if log_info:
            # If user is logged in, get user entity from db.
            user_data = self.query_users.search_user_by_id(log_info)

            # Render page with current email info.
            self.render("edit_personal_data.html", email=user_data.email)
        else:
            # If user is not logged in, redirect to login page.
            self.render("login.html")

    def post(self):
        # Get user id stored in cookies.
        log_info = self.cookies.get_loginfo_cookie(self)

        # Get user entity from db.
        user_data = self.query_users.search_user_by_id(log_info)

        # Get data posted by user.
        email = self.request.get('email')
        password = self.request.get('password')
        verify = self.request.get('verify')

        # Check if new email is valid.
        email_validation = self.validation.email_verify(email)

        # Object to store password validation data. This allows to have a
        # response status ok in cases where user didn't changed password.
        password_validation = {"response": "ok", "info": ""}

        if password:
            # If password was changed, check if its valid.
            password_validation = self.validation.test_password(password,
                                                                verify)

        if email_validation["response"] and password_validation["response"]:
            # If email is valid and password is valid, store the new data.
            self.store_data(user_data, email, password)
        else:
            # If email or password isn't valid, render page with corresponding
            # error messages.
            self.render("edit_personal_data.html", email=email,
                        error_email=email_validation["info"],
                        error_password=password_validation["info"])

    def store_data(self, user_data, email, password):
        if email:
            # Store email.
            user_data.email = email

        if password:
            # If password was chenged, hash it and store.
            user_data.password = self.hashs.make_secure_password(
                user_data.username, password)

        # Put new user data in db.
        user_data.put()

        # Redirect user to kitchen page.
        self.redirect("/kitchen")
