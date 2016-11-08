import re

class RecipeValidation:
    def __init__(self):
        pass

    def validate_title(self, title):
        if title == "":
            return {"response": None, "info": "Please insert a title for this recipe."}
        else:
            return {"response": title, "info": ""}

    def is_number(self, s):
        # Function similar as the one seen in http://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float-in-python
        try:
            int(s)
            return True
        except ValueError:
            return False

    def validate_prep_time(self, prep_time):
        if self.is_number(prep_time):
            return {"response": prep_time, "info": ""}
        else:
            return {"response": None, "info": "Please insert a valid number."}

    def list_length_validation(self, list_to_validate, string):
        if len(list_to_validate) > 0:
            return {"response": list, "info": ""}
        else:
            return {"response": None, "info": "Please insert at least one %s." % string}
