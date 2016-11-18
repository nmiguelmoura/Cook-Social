import handler
import db_model_users
import prefabs.db_query_users
import prefabs.cookie_handler
import prefabs.hash_tools
import prefabs.signup_validation
import time
import prefabs.secret_codes
import urllib
from google.appengine.api import urlfetch
import json



class SignupHandler(handler.Handler):
    """Class that allows new users to sign up."""

    validation = prefabs.signup_validation.SignupValidation()
    hashs = prefabs.hash_tools.HashTools()
    query_users = prefabs.db_query_users.DBQueryUsers()
    cookies = prefabs.cookie_handler.CookieHandler()
    secret = prefabs.secret_codes.SecretCode()

    def get(self):
        if self.cookies.get_loginfo_cookie(self):
            # If user is already logged in, redirect to kitchen.
            self.redirect("/kitchen")
        else:
            # If user is not logged in, render signup page.
            self.render("sign_up.html")

    def post(self):
        # Get posted data.
        username = self.request.get("username")
        email = self.request.get("email")
        password = self.request.get("password")
        verify = self.request.get("verify")

        # Get reCaptcha user input.
        recaptcha_user_response = self.request.get("g-recaptcha-response")

        # Assemble data to send to post method.
        data = {
            "secret": self.secret.get_recaptcha_code(),
            "response": recaptcha_user_response
        }

        recaptcha_validation = {
            "response": False,
            "info": "Please tick box above to prove you are not a robot."
        }

        try:
            # Try to post data and wait for response
            form_data = urllib.urlencode(data)
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            result = urlfetch.fetch(
                url='https://www.google.com/recaptcha/api/siteverify',
                payload=form_data,
                method=urlfetch.POST,
                headers=headers)

            # Json loading.
            validation = json.loads(result.content)
            if validation["success"]:
                # If answer is True, pass it to recaptcha_validation and erase message
                recaptcha_validation = {
                    "response": True,
                    "info": ""
                }

        except urlfetch.Error:
            # If can't validate recaptcha answer
            self.redirect("/messagetouser?id=unexpected_error")

        # Validate username.
        username_validation = self.validation.username_verify(username)

        # Validate email address.
        email_validation = self.validation.email_verify(email)

        # Validate password.
        password_validation = self.validation.test_password(password, verify)

        if username_validation["response"] and email_validation["response"] and \
                password_validation["response"] and recaptcha_validation["response"]:
            # Run if posted data is all valid.

            # Check if username is available.
            username_available = self.check_username_availability(username)

            if username_available:
                # If username is available, store data in db.
                self.store_data(username, email, password)
            else:
                # If username is unavailable, render page with error message.
                message = "This username already exists. Please choose another one."
                self.render('sign_up.html', username=username, email=email,
                            error_username=message)
        else:
            # If posted data is invalid, render page with corresponding error messages.
            self.render('sign_up.html', username=username, email=email,
                        error_username=username_validation["info"],
                        error_email=email_validation["info"],
                        error_password=password_validation["info"],
                        error_captcha=recaptcha_validation["info"])

    def check_username_availability(self, username):
        # Query users to check if username chosen is already in use and
        # return accordingly.
        user = self.query_users.search_user(username)
        return False if user else True

    def store_data(self, username, email, password):
        # Store data after validation.

        # Hash password.
        hashed_password = self.hashs.make_secure_password(username, password)

        # Create new user entity.
        users = db_model_users.UsersDBModel(username=username, email=email,
                                            password=hashed_password,
                                            pointed=[''], comments=[''])
        users.put()

        # Get user id.
        user_id = str(users.key().id())

        # Store cookie with id data.
        self.set_cookie(user_id)

        # Delay 0.2 sec before redirecting to next page to avoid errors
        # reading from db.
        time.sleep(0.2)

        # REdirect to kitchen page.
        self.redirect("/kitchen")

    def set_cookie(self, user_id):
        # Store cookie with user id info.
        self.cookies.set_loginfo_cookie(self, user_id)
