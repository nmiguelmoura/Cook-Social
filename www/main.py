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
import kitchen_handler
import my_recipes_handler
import recipe_handler
import new_comment_handler

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
    ("/news", news_handler.NewsHandler),
    ("/kitchen", kitchen_handler.KitchenHandler),
    ("/myrecipes", my_recipes_handler.MyRecipesHandler),
    ("/recipe", recipe_handler.RecipeHandler),
    ("/newcomment", new_comment_handler.NewCommentHandler),
], debug=True)
