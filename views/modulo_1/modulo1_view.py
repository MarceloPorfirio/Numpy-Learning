import flet as ft
from views.modulo_1.modulo1_intro import modulo1_intro_view
# from views.modulo_1.arrays_basicos import array_basicos_view
# from views.modulo_1.arrays_tipos import array_tipos_view
# from views.modulo_1.arrays_formas import array_formas_view

def modulo1_view(page):
    return ft.View(
        "/modulo1",
        controls=[
            ft.AppBar(title=ft.Text("📘 Módulo 1 - Arrays Básicos"), bgcolor="#1565C0"),
            modulo1_intro_view(page),
            # array_basicos_view(page),
            # array_tipos_view(page),
            # array_formas_view(page),
            ft.ElevatedButton("⬅️ Voltar ao Menu", on_click=lambda e: page.go("/menu"))
        ],
    )
