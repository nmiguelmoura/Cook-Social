import handler

class KitchenHandler(handler.Handler):
    def get(self):
        self.render("kitchen.html")
