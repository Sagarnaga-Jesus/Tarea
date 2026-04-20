import flet as ft

def LoginView(page, auth_controller):
    email_input = ft.TextField(label="Correo Electrónico", width=350, border_radius=10, keyboard_type=ft.KeyboardType.EMAIL)
    pass_input = ft.TextField(label="Contraseña", width=350, password=True, can_reveal_password=True, border_radius=10)
    
    def login_click(e):
        if not email_input.value or not pass_input.value:
            page.snackbar = ft.Snackbar(ft.Text("Por favor, complete todos los campos"))
            page.snackbar.open = True
            page.update()
            return
        
        user, msg = auth_controller.login(email_input.value, pass_input.value)
        if user:
            page.session.set("user", user) # Guardar el usuario en la sesión
            page.go("/dashboard")
        else:            
            page.snackbar = ft.Snackbar(ft.Text(msg))
            page.snackbar.open = True
            page.update()
        
        login_button = ft.ElevatedButton("Entrar", on_click=login_click, width=350, bgcolor="blue", color="white")
        
        pass_input.on_submit = login_click
        
        return ft.View(
            route="/", 
            verical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            appbar=ft.AppBar(title=ft.Text("SIGE - Login"), bgcolor = ft.Colors.BLUE_GREY_900, color="white"),
            controls=[
                ft.Column([
                    ft.Text("Acceso al sistema ", size=24, weight="bold"),
                    email_input,
                    pass_input,
                    login_button,
                    ft.ElevatedButton("Entrar", on_click=login_click, width=350),
                    ft.TextButton("Crear cuenta", on_click=lambda e: page.go("/registro"))
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
                tigtht=True
            )
        ]
    )