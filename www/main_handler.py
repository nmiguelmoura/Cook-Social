import handler

class MainHandler(handler.Handler):
    def get(self):
        self.render("main.html")
