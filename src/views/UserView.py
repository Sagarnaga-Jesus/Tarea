import flet as ft
import shutil
import os
from datetime import datetime
from controllers.UserController import AuthController

def UserView(page, auth_controller):
    page.update()
    page.title = "Perfil"
    user = getattr(page, "user_data")
    apellido = ft.Text(f"Apellido: {user['apellido'] if user else 'Usuario'}", size=20)
    telefono = ft.Text(f"Telefono: {user['telefono'] if user else 'Usuario'}", size=20)
    registro = ft.Text(f"Se registro el: {user['fecha_registro'] if user else 'Usuario'}", size=20)
    ultimo = ft.Text(f"Ultimo conectado: {user['ultimo_ingreso'] if user else 'Usuario'}", size=20)
    
    imagen = user['foto']
    
    foto = ft.Image(src=f"assets/{imagen}", width=150, height=150)
    
    modificar_btn = ft.ElevatedButton("Modificar Perfil", on_click=lambda _: page.go("/modificar"))
    

    return ft.View(
        route="/perfil",
        controls=[
            ft.AppBar(
                title=ft.Text(f"Nombre del usuario: {user['nombre'] if user else 'Usuario'}", size=40),
                
                actions=[
                    modificar_btn,
                    ft.IconButton(ft.Icons.BOOK, on_click=lambda _: page.go("/dashboard")),
                    ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda _: page.go("/"))
                ],
            ),
            ft.Container(
                ft.Column([
                        ft.Row([foto]),
                        ft.Divider(thickness=8,          
                                    color=ft.Colors.BLUE,
                                    ),
                        ft.Row([apellido]),
                        ft.Row([telefono]),
                        ft.Row([registro]),
                        ft.Row([ultimo])
                        
                ], expand=True),
                padding=20,expand=True
            ),
        ]
    )

def ModificarView(page, user):
    async def seleccionar_archivo(e):

        archivos = await file_picker.pick_files(
            allow_multiple=False
        )

        if archivos:
            archivo = archivos[0]
            
            
            page.foto_nueva_path = archivo.path
            page.foto_nueva_name = archivo.name

    file_picker = ft.FilePicker()

    boton = ft.ElevatedButton(
        "Seleccionar archivo",
        on_click=seleccionar_archivo
    )
    
    def guardar_cambios(e):
        if not telefono_nuevo.value or not apellido_nuevo.value or not nombre_nuevo.value:
            page.show_dialog(ft.SnackBar(ft.Text("Complete los campos")))
            return False
            
        else:
            destino = os.path.join(
                "assets",
                page.foto_nueva_name
            )

            shutil.copy(
                page.foto_nueva_path,
                destino
            )
            success= AuthController().modificar(
                user['id_usuario'],
                nombre_nuevo.value,
                apellido_nuevo.value,
                telefono_nuevo.value,
                page.foto_nueva_name
            )
            if success:
                page.show_dialog(ft.SnackBar(ft.Text("Perfil actualizado correctamente")))
                user['nombre'] = nombre_nuevo.value
                user['apellido'] = apellido_nuevo.value
                user['telefono'] = telefono_nuevo.value
                user['foto'] = page.foto_nueva_name

                page.user_data = user
                page.go("/perfil")
                page.update()
            else:
                page.show_dialog(ft.SnackBar(ft.Text("Error al actualizar perfil")))
    
    nombre_nuevo = ft.TextField(label="Nuevo Nombre", icon=ft.Icons.BADGE)
    apellido_nuevo = ft.TextField(label="Nuevo Apellido", icon=ft.Icons.BADGE)
    telefono_nuevo = ft.TextField(label="Nuevo Telefono", icon=ft.Icons.CALL)
    guardar_btn = ft.ElevatedButton("Guardar Cambios", on_click=guardar_cambios)
    salir = ft.ElevatedButton("Salir", on_click=lambda _: page.go("/perfil"))
    
    return ft.View(
        route="/modificar",
        controls=[
            ft.Column(
                [
                    ft.Icon(ft.Icons.ACCOUNT_BOX, size=50, color=ft.Colors.BLUE),
                    ft.Text("Registro de usuario", size=30, weight="bold"),
                    ft.Row([nombre_nuevo,apellido_nuevo,],ft.CrossAxisAlignment.CENTER,),
                    telefono_nuevo,
                    ft.Row([boton],ft.CrossAxisAlignment.CENTER,),
                    ft.Row([guardar_btn,salir],ft.CrossAxisAlignment.CENTER,),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                tight=True 
            )
        ])