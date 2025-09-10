import flet as ft
import numpy as np

def modulo1_intro_view(page: ft.Page):
    def create_card(title, example, result):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(title, size=18, weight="bold"),
                        ft.Text(f"Exemplo: {example}", size=16, color=ft.colors.BLACK87),
                        ft.Text(f"Resultado: {result}", size=16, color=ft.colors.BLUE_700),
                    ],
                    spacing=6,
                ),
                padding=12,
            ),
            elevation=3,
            margin=ft.margin.all(8),
        )

    return ft.Column(
        [
            ft.Text("📘 Módulo 1 - Arrays Básicos", size=24, weight="bold"),
            ft.Text(
                "NumPy é uma biblioteca para computação numérica em Python.\n"
                "O elemento principal do NumPy é o 'array', que é uma coleção de elementos do mesmo tipo.",
                size=16,
            ),
            create_card("➡️ Criando arrays a partir de listas", "np.array([1, 2, 3, 4])", np.array([1, 2, 3, 4])),
            create_card("➡️ Arrays zerados", "np.zeros(3)", np.zeros(3)),
            create_card("➡️ Arrays de uns", "np.ones(3)", np.ones(3)),
            create_card("➡️ Arrays aleatórios", "np.random.rand(3)", np.random.rand(3)),
        ],
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.START,
    )
