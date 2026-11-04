import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ModelContactos:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL"),
                os.environ.get("SUPABASE_KEY")
            )
        except Exception as error:
            print(f"ERROR 100: {error.args[0]}")

    def obtenerContactos(self):
        # SELECT * FROM contactos;
        response = self.supabase.table("contactos").select("*").execute()
        return response.data

    def buscarContacto(self, id_contacto: int):
        response = self.supabase.table("contactos").select("*").eq("id_contacto", id_contacto).execute()
        return response.data

    def InsertarContacto(self, nombre: str, email: str, telefono: str):
        datos = {
            "nombre": nombre, 
            "email": email,
            "telefono": telefono
        }
        response = self.supabase.table("contactos").insert(datos).execute()
        return response.data 

    def BorrarContacto(self, id_contacto: int):
        response = self.supabase.table("contactos").delete().eq("id_contacto",id_contacto).execute()
        return response.data

    def actualizarContacto(self, id_contacto: int, nombre: str, email: str, telefono: str):
        datos ={
            "nombre": nombre,
            "email": email,
            "telefono": telefono
        }

        response = self.supabase.table("contactos").update(datos).eq("id_contacto", id_contacto).execute()
        return response.data


if __name__ == "__main__":
    model_contactos = ModelContactos()
    print(model_contactos.obtenerContactos())
    print(model_contactos.buscarContacto(4))
    print(model_contactos.InsertarContacto("jacob","jacob@email.com","6666666"))
    print(model_contactos.BorrarContacto(4))
    print(model_contactos.actualizarContacto(8, "juan", " juan@email.com","999999999"))

