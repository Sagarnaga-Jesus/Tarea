import flet as ft
from controllers.UserController import AuthController
from controllers.UserController import TareaController
from views.LoginView import LoginView
from views.dashboard import DashboardView

def main(page: ft.Page):
    # instanciar controladores ua sola
    auth_ctrl = AuthController()
    task_ctrl = TareaController()
    
    def route_change(route):
        page.views.clear()
        
        if route == "/":
            page.add(ft.Text("Caso 1"))
            page.views.append(LoginView(page, auth_ctrl))
            
        elif route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
            
        if not page.views:
            page.views.append(
                ft.View("/",[ft.Text("Error: Ruta no encontrada o vista vacia")])
            )
        
            #agregas aqui las vistas que necesites
        page.update()
    page.on_route_change = route_change

    page.go("/")
    
if __name__ == "__main__":
    ft.app(target=main)