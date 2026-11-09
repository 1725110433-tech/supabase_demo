import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render("mvc/views", base="template")

class InsertarContacto:
    def GET(self):
        return render.insertar_comntacto()

    def POST(self):
        formulario = web.input()
        nombre = formulario['nombre']
        email = formulario['email']
        telefono = formulario['telefono']

        print(f"Nombre: {nombre}")
        print(f"Email: {email}")
        print(f"Teléfono: {telefono}")

        model_contactos = ModelContactos()
        datos = model_contactos.InsertarContacto(nombre, email, telefono)

        html = """
        <h1>Contacto almacenado correctamente</h1>
        <a href='/contactos'>Regresar</a>
        """
        return html