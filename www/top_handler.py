import handler

class TopHandler(handler.Handler):
    def get(self):
        self.render("top.html")
