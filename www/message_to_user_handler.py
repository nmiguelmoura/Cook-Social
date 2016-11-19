# -*- coding: utf-8 -*-

import handler

class MessageToUserHandler(handler.Handler):
    """Class that handles error message page."""
    def get(self):
        # Get type of message to display
        type = self.request.get("type")

        # Create variables to store title and message and
        # change them according to type passed in.
        title = None
        message = None
        if type == "contact":
            title = "Questão / sugestão enviada"
            message = "As suas questões  ou sugestões foram enviadas " \
                      "Responderemos com a maior brevidade possível. Obrigado."
        elif type == "comment_permission_error":
            title = "Acesso não autorizado"
            message = "Não está autorizado(a) a editar este comentário. " \
                      "Apenas pode editar os seus próprios comentários."
        elif type == "recipe_not_found":
            title = "Receita não encontrada"
            message = "A receita que indicou não foi encontrada!"
        elif type == "permission_error":
            title = "Acesso não autorizado"
            message = "Não está autorizado(a) a editar esta receita. " \
                      "Apenas pode editar as suas próprias receitas."
        elif type == "unexpected_error":
            title = "Erro inesperado"
            message = "Ocorreu um erro inesperado. " \
                      "Por favor tente novamente."
        else:
            title = "Página não encontrada"
            message = "A página que solicitou não existe!"

        # Render page with corresponding title and message.
        self.render("message_to_user.html", title=title, message=message)
