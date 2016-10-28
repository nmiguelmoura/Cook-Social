import handler

class ContactHandler(handler.Handler):
    def get(self):
        self.render("contact.html")
