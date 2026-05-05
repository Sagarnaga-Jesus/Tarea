import flet as ft
from controllers.UserController import AuthController

def ModificarView(page, user):
    
    def guardar_cambios():
        success = AuthController().modificar(
            user['id_usuario'],
            nombre_nuevo.value,
            apellido_nuevo.value,
            telefono_nuevo.value,
            
        )

        if success:
            page.show_dialog(ft.SnackBar(ft.Text("Perfil actualizado correctamente")))
            page.go("/perfil")
        else:
            page.show_dialog(ft.SnackBar(ft.Text("Error al actualizar perfil")))
    
    nombre_nuevo = ft.TextField(label="Nuevo Nombre", icon=ft.Icons.BADGE)
    apellido_nuevo = ft.TextField(label="Nuevo Apellido", icon=ft.Icons.BADGE)
    telefono_nuevo = ft.TextField(label="Nuevo Telefono", icon=ft.Icons.CALL)
    guardar_btn = ft.ElevatedButton("Guardar Cambios", on_click=guardar_cambios)
    
    return ft.View(
        route="/modificar",
        controls=[
            ft.Column(
                [
                    ft.Icon(ft.Icons.ACCOUNT_BOX, size=50, color=ft.Colors.BLUE),
                    ft.Text("Registro de usuario", size=30, weight="bold"),
                    ft.Row([nombre_nuevo,apellido_nuevo,],ft.CrossAxisAlignment.CENTER,),
                    telefono_nuevo,
                    guardar_btn
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                tight=True 
            )
        ])