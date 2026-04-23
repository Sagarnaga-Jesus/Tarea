import flet as ft

admin="Holadmin"
admincontra="admin"

def LoginView(page, AuthController):
    admin="Holadmin"
    admincontra="admin"
    
    def ver_contra():
        contra.password = not contra.password
        contra.update()
        
    correo=(ft.TextField(label="Correo",autofocus=True, icon=ft.Icons.PERSON ))
    contra=(ft.TextField(label="Contraseña",suffix=ft.IconButton(icon=ft.Icons.VISIBILITY, on_click=ver_contra) ,password=True, autofocus=True, icon=ft.Icons.PASSWORD))
    
    def verifica():
            if admin==correo.value and admincontra==contra.value:
                page.show_dialog(ft.SnackBar(ft.Text("Has iniciado sesion correctamente")))
                inicio()
            else:
                page.show_dialog(ft.SnackBar(ft.Text("Usuario o contraseña incorrecta")))
    
    def login_click():
        if not correo.value or not contra.value:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, complete todos los campos"))
            page.snack_bar.open = True
            page.update()
            return
        user, msg = AuthController.login(correo.value, contra.value)
        if user:
            page.session.set("user", user)
            page.go("/dashboard")
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()
    
    def olvidado():
        page.show_dialog(ft.SnackBar(ft.Text("Se a enviado su contraseña al correo")))
    
    iniciar=( ft.Button("Iniciar sesion",color=ft.Colors.WHITE ,bgcolor=ft.Colors.BLUE,on_click=verifica))
    registrarse =( ft.TextButton("¿Quieres registrarte?"))
    olvidada =( ft.TextButton("¿Olvidaste la contraseña?", on_click=olvidado))
    
    def cambio_pantalla():
        
        page.controls.clear()
        
        if page.navigation_bar.selected_index == 0:
            inicio()
            
        elif page.navigation_bar.selected_index == 1:
            nuevo()
            
        elif page.navigation_bar.selected_index == 2:
            perfil()
            
        
        
    navegador =  ft.NavigationBar(
                destinations=[
                    ft.NavigationBarDestination(icon=ft.Icons.HOUSE, label="Inicio"),
                    ft.NavigationBarDestination(icon=ft.Icons.BOOK, label="Nuevo", ),
                    ft.NavigationBarDestination(icon=ft.Icons.MENU_BOOK, label="Perfil"),
                ],
                on_change=cambio_pantalla
            )
    
    def inicio():
        page.controls.clear()
        page.title="Inicio"
        
        page.add(ft.Text("Inicio",size=30, weight=ft.FontWeight.BOLD),)
        page.add(ft.Text("Has iniciado secion correctamente bienvenido",size=15, weight=ft.FontWeight.BOLD),)
        page.navigation_bar = (navegador)
        page.update()
        
    def nuevo():
        page.controls.clear()
        page.title="Nuevo"
        
        page.add(ft.Text("Nuevo",size=30, weight=ft.FontWeight.BOLD),)
        page.add(ft.Text("Nuevo se convertira en cerrar aplicacion",size=50, weight=ft.FontWeight.BOLD),)
        page.navigation_bar = (navegador)
        page.update()
        
    def perfil():
        page.controls.clear()
        page.title="Perfil"
        
        page.add(ft.Text("Perfil",size=30, weight=ft.FontWeight.BOLD),)
        page.navigation_bar = (navegador)
        page.update()
    
    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,  # corregido
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("SIGE - Login"),
            bgcolor=ft.Colors.BLUE_GREY_900,
            color="white"
        ),
        controls=[
            ft.Column(
                [
                    ft.Icon(ft.Icons.LOCK_PERSON, size=50, color=ft.Colors.BLUE),
                    ft.Text("Acceso al sistema", size=24, weight="bold"),
                    correo,
                    contra,
                    iniciar,
                    registrarse,
                    olvidada
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                tight=True 
            )
        ]
    )
    