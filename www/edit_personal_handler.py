import handler

class EditPersonalHandler(handler.Handler):
    def get(self):
        self.render("edit_personal_data.html")
