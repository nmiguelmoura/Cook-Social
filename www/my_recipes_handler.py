import handler

class MyRecipesHandler(handler.Handler):
    def get(self):
        self.render("my_recipes.html")
