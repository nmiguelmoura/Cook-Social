import os
import webapp2
import main_handler
import login_handler
import signup_handler
import edit_personal_handler
import edit_comment_handler
import forgot_password_handler
import contact_handler
import top_handler
import news_handler

# Defines de routers.
app = webapp2.WSGIApplication([
    ("/", main_handler.MainHandler),
    ("/login", login_handler.LoginHandler),
    ("/signup", signup_handler.SignupHandler),
    ("/editpersonaldata", edit_personal_handler.EditPersonalHandler),
    ("/editcomment", edit_comment_handler.EditCommentHandler),
    ("/forgotpassword", forgot_password_handler.ForgotPasswordHandler),
    ("/contact", contact_handler.ContactHandler),
    ("/top", top_handler.TopHandler),
    ("/news", news_handler.NewsHandler)
], debug=True)
