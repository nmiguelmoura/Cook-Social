import handler

class PublishHandler(handler.Handler):
    def get(self):
        self.render("publish.html")
