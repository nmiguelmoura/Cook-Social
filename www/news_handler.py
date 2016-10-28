import handler

class NewsHandler(handler.Handler):
    def get(self):
        self.render("news.html")
