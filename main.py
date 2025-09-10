import flet as ft

# --- IMPORTS DAS VIEWS ---
from views.modulo_1.modulo1_view import modulo1_view  # sua view completa do módulo 1

# --- VIEWS ---

def welcome_view(page: ft.Page):
    return ft.View(
        "/",
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(
                            "Bem-vindo ao curso interativo de NumPy",
                            size=22,
                            weight="bold",
                            text_align="center",
                            color=ft.colors.WHITE,
                        ),
                        ft.Text(
                            "Aprenda NumPy com exemplos interativos e exercícios práticos.",
                            size=14,
                            text_align="center",
                            color=ft.colors.WHITE70,
                        ),
                        ft.Image(
                            src="inicio.png", width=260, height=260, fit=ft.ImageFit.CONTAIN
                        ),
                        ft.ElevatedButton(
                            "Começar",
                            on_click=lambda e: page.go("/menu"),
                            style=ft.ButtonStyle(
                                bgcolor=ft.colors.WHITE,
                                color=ft.colors.BLUE_700,
                                shape=ft.RoundedRectangleBorder(radius=16),
                                padding=20,
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=28,
                ),
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[ft.colors.BLUE_600, ft.colors.WHITE],
                ),
                alignment=ft.alignment.center,
                padding=20,
            )
        ],
    )


def menu_view(page: ft.Page):
    return ft.View(
        "/menu",
        controls=[
            ft.AppBar(title=ft.Text("📑 Menu de Módulos"), bgcolor=ft.colors.BLUE_600),
            ft.Column(
                controls=[
                    ft.ElevatedButton(
                        "📘 Módulo 1 - Arrays Básicos",
                        on_click=lambda e: page.go("/modulo1"),
                    ),
                    ft.ElevatedButton(
                        "📘 Módulo 2 - Indexação e Slicing",
                        on_click=lambda e: page.go("/modulo2"),
                    ),
                    ft.ElevatedButton(
                        "📘 Módulo 3 - Operações Matemáticas",
                        on_click=lambda e: page.go("/modulo3"),
                    ),
                    ft.ElevatedButton(
                        "📘 Módulo 4 - Broadcasting",
                        on_click=lambda e: page.go("/modulo4"),
                    ),
                    ft.ElevatedButton(
                        "📘 Módulo 5 - Manipulação de Formas",
                        on_click=lambda e: page.go("/modulo5"),
                    ),
                    ft.ElevatedButton(
                        "📘 Módulo 6 - Estatísticas",
                        on_click=lambda e: page.go("/modulo6"),
                    ),
                    ft.ElevatedButton(
                        "📘 Módulo 7 - Integração com Pandas/Matplotlib",
                        on_click=lambda e: page.go("/modulo7"),
                    ),
                    ft.TextButton("⬅️ Voltar ao Início", on_click=lambda e: page.go("/")),
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=16,
                scroll=ft.ScrollMode.AUTO,
            ),
        ],
    )


# --- MAIN ---

def main(page: ft.Page):
    page.title = "Aprendendo NumPy"
    page.on_route_change = lambda e: route_change(e, page)
    page.go("/")  # rota inicial


def route_change(e: ft.RouteChangeEvent, page: ft.Page):
    page.views.clear()

    if page.route == "/":
        page.views.append(welcome_view(page))
    elif page.route == "/menu":
        page.views.append(menu_view(page))
    elif page.route == "/modulo1":
        page.views.append(modulo1_view(page))  # usa sua view real do módulo 1
    # outros módulos podem continuar como rascunho
    elif page.route.startswith("/modulo"):
        page.views.append(
            ft.View(
                page.route,
                controls=[
                    ft.AppBar(
                        title=ft.Text(f"📘 {page.route.capitalize()}"),
                        bgcolor=ft.colors.BLUE_600,
                    ),
                    ft.Text("Conteúdo em construção...", size=16),
                    ft.ElevatedButton(
                        "⬅️ Voltar ao Menu", on_click=lambda e: page.go("/menu")
                    ),
                ],
            )
        )

    page.update()


ft.app(target=main, assets_dir="assets")
