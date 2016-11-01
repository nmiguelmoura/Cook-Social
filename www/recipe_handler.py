import handler

class RecipeHandler(handler.Handler):
    def get(self):
        self.render("recipe.html")
