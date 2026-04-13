import flet as ft
from src.controllers.UserController import AuthController
from src.controllers.UserController import TareaController
from src.views.LoginView import LoginView
from src.views.dashboard import DashboardView

def main(page: ft.Page):
    # instanciar controladores ua sola
    auth_ctrl = AuthController()
    task_ctrl = TareaController()
    
    def route_change(route):
        page.views.clear()
        if route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
            #agregas aqui las vistas que necesites
        page.update()
    page.on_route_change = route_change

    page.go("/")
    
if __name__ == "__main__":
    ft.app(target=main)