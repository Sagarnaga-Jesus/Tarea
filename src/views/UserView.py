import flet as ft

def UserView(page, auth_controller):
    user = getattr(page, "user_data", None)
    apellido = ft.Text(f"Apellido: {user['apellido'] if user else 'Usuario'}", size=20)
    telefono = ft.Text(f"Telefono: {user['telefono'] if user else 'Usuario'}", size=20)
    registro = ft.Text(f"Se registro el: {user['fecha_registro'] if user else 'Usuario'}", size=20)
    ultimo = ft.Text(f"Ultimo conectado: {user['ultimo_ingreso'] if user else 'Usuario'}", size=20)

    return ft.View(
        route="/perfil",
        controls=[
            ft.AppBar(
                title=ft.Text(f"Nombre del usuario: {user['nombre'] if user else 'Usuario'}", size=40),
                
                actions=[
                    ft.IconButton(ft.Icons.BOOK, on_click=lambda _: page.go("/dashboard")),
                    ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda _: page.go("/"))
                ],
            ),
            ft.Container(
                ft.Column([
                        ft.Divider(thickness=8,          
                                    color=ft.Colors.BLUE,
                                    ),
                        ft.Row([apellido]),
                        ft.Divider(thickness=6,          
                                    color=ft.Colors.BLUE,),
                        ft.Row([telefono]),
                        ft.Divider(thickness=6,          
                                    color=ft.Colors.BLUE,),
                        ft.Row([registro]),
                        ft.Divider(thickness=6,          
                                    color=ft.Colors.BLUE,),
                        ft.Row([ultimo])
                        
                ], expand=True),
                padding=20,expand=True
            ),
        ]
    )