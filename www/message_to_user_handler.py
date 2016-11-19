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
            title = u"Questão / sugestão enviada"
            message = u"As suas questões  ou sugestões foram enviadas " \
                      u"Responderemos com a maior brevidade possível. Obrigado."
        elif type == "comment_permission_error":
            title = u"Acesso não autorizado"
            message = u"Não está autorizado(a) a editar este comentário. " \
                      u"Apenas pode editar os seus próprios comentários."
        elif type == "recipe_not_found":
            title = u"Receita não encontrada"
            message = u"A receita que indicou não foi encontrada!"
        elif type == "permission_error":
            title = u"Acesso não autorizado"
            message = u"Não está autorizado(a) a editar esta receita. " \
                      u"Apenas pode editar as suas próprias receitas."
        elif type == "unexpected_error":
            title = u"Erro inesperado"
            message = u"Ocorreu um erro inesperado. " \
                      u"Por favor tente novamente."
        else:
            title = u"Página não encontrada"
            message = u"A página que solicitou não existe!"

        # Render page with corresponding title and message.
        self.render("message_to_user.html", title=title, message=message)
