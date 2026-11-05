import web

from ..models.Model_contactos import ModelContactos

render = web.template.render("mvc/views/", base="template")

class contactos: 

    def GET(self):

        model_contactos = ModelContactos()

        print(model_contactos.obtenerContactos())
        return render.contactos()