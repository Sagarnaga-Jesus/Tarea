import flet as ft
from controllers.UserController import AuthController
from controllers.TareaController import TareaController
from views.LoginView import LoginView
from views.dashboardView import DashboardView

def start(page: ft.Page):
    # instanciar controladores ua sola
    auth_ctrl = AuthController()
    task_ctrl = TareaController()
    
    def route_change(e):
        page.views.clear()
        
        if e == "/":
            page.add(ft.Text("Caso 1"))
            page.views.append(LoginView(page, auth_ctrl))
            
        elif e == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
            
        if not page.views:
            page.views.append(
                ft.View("/",[ft.Text("Error: Ruta no encontrada o vista vacia")])
            )
        
            #agregas aqui las vistas que necesites
        page.update()
    page.on_route_change = route_change

    page.go("/")
    
def main ():
    ft. app (target=start)
    
if __name__ == "__main__":
    main()