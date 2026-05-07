import flet as ft
from datetime import datetime
import shutil
import os

def RegistroView(page: ft.Page, auth_controller):
    
    def ver_contra():
        contra.password = not contra.password
        contra.update()
        
    correo=(ft.TextField(label="Correo",autofocus=True, icon=ft.Icons.PERSON ))
    contra=(ft.TextField(label="Contraseña",suffix=ft.IconButton(icon=ft.Icons.VISIBILITY, on_click=ver_contra) ,password=True, autofocus=True, icon=ft.Icons.PASSWORD))
    nombre=(ft.TextField(label="Nombre",icon=ft.Icons.BADGE))
    apellido=(ft.TextField(label="apellido",autofocus=True,))
    telefono=(ft.TextField(label="Telefono",autofocus=True,icon=ft.Icons.CALL))
    
    
    async def seleccionar_archivo(e):

        archivos = await file_picker.pick_files(
            allow_multiple=False
        )

        if archivos:
            archivo = archivos[0]
            
            page.foto_name = archivo.name
            page.foto_path = archivo.path
            print(archivo.name)
            print(archivo.path)

    file_picker = ft.FilePicker()

    boton = ft.ElevatedButton(
        "Seleccionar archivo",
        on_click=seleccionar_archivo
    )
    
    

    def registra(e):
        if not correo.value and not contra.value and not nombre.value and not apellido.value and not telefono.value :
            page.show_dialog(ft.SnackBar(ft.Text("Por favor, complete todos los campos")))
            return
        
        destino = os.path.join(
                "assets",
                page.foto_name
            )

        shutil.copy(
            page.foto_path,
            destino
        )
        
        hoy = datetime.now()
        fecha = hoy.strftime("%Y-%m-%d")
        
        user, msg = auth_controller.registrar_Usuario(nombre.value, apellido.value, correo.value, contra.value, telefono.value, fecha, page.foto_name)
        
        if user:
            page.go("/")
            page.show_dialog(ft.SnackBar(ft.Text(msg)))
        else:
            page.show_dialog(ft.SnackBar(ft.Text(msg)))
    
    registrar =( ft.ElevatedButton("Registrase",color=ft.Colors.BLUE, on_click=registra))
    def regresar():
        page.go("/")
        
    reversa = ( ft.ElevatedButton("Regresar a login",color=ft.Colors.RED ,on_click=regresar))
    
    return ft.View(
        route="/registro",
        vertical_alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("Registro"),
            bgcolor=ft.Colors.BLUE_GREY_900,
            color="white"
        ),
        controls=[
            ft.Column(
                [
                    ft.Icon(ft.Icons.ACCOUNT_BOX, size=50, color=ft.Colors.BLUE),
                    ft.Text("Registro de usuario", size=30, weight="bold"),
                    ft.Row([nombre,apellido,],ft.CrossAxisAlignment.CENTER,),
                    telefono,
                    correo,
                    contra,
                    boton,
                    registrar,
                    reversa
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                tight=True 
            )
        ]
    )
    