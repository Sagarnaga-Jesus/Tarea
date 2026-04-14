import flet as ft

def LoginView(page, auth_controller):
    email_input = ft.TextField(label="Correo Electrónico", width=350, border_radius=10)
    pass_input = ft.TextField(label="Contraseña", width=350, password=True, can_reveal_password=True)
    
    def login_click(e):
        user, msg = auth_controller.login(email_input.value, pass_input.value)
        if user:
            page.session.set("user", user) # Guardar el usuario en la sesión
            page.go("/dashboard")
        else:            
            page.snackbar = ft.Snackbar(ft.Text(msg))
            page.snackbar.open = True
            page.update()
        
        return ft.View("/login", [
            ft.AppBar(title=ft.Text("SIGE - Login"), bgcolor = ft.Color.BLUE_GREY_900, color="white"),
            ft.Column([
                ft.Icon(ft.Icons.LOCK_PERSON, size=50, color=ft.Color.BLUE),
                ft.Text("Acceso al sistema ", size=24, weight="bold"),
                email_input,
                pass_input,
                ft.ElevatedButton("Entrar", on_click=login_click, width=350),
                ft.TextButton("Crear cuenta", on_click=lambda e: page.go("/register"))
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER,
                )
        ])