# -*- coding: utf-8 -*-

import re


class RecipeValidation:
    """Class that validates recipes."""

    def __init__(self):
        pass

    def validate_title(self, title):
        if title == "":
            # If title hasn't been passed return error message
            return {"response": None,
                    "info": "Por favor dê um nome a esta receita."}
        else:
            # If title has been passed, return title on response.
            return {"response": title, "info": ""}

    def is_number(self, s):
        # Function similar as the one seen in
        # http://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float-in-python
        # Check if a given value is a number.
        try:
            # If value is a number, return True.
            int(s)
            return True
        except ValueError:
            # If not number, catch error and return False.
            return False

    def validate_prep_time(self, prep_time):
        if self.is_number(prep_time):
            # If prep_time is a number, return prep_time in response.
            return {"response": prep_time, "info": ""}
        else:
            # If prep_time is not a number, return error message.
            return {"response": None, "info": "Por favor introduza um número válido."}

    def list_length_validation(self, list_to_validate, string):
        if len(list_to_validate) > 0:
            # If given list has 1 or more elements, return list on response.
            return {"response": list, "info": ""}
        else:
            # If a given list is empty, return error message with given string.
            return {"response": None,
                    "info": "Por favor indique pelo menos um %s." % string}
