import flet as ft

def modulo1_intro_view(page: ft.Page):
    def create_card(title, content):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(title, size=18, weight="bold"),
                        ft.Text(content, size=15, color=ft.colors.BLACK87),
                    ],
                    spacing=8,
                ),
                padding=14,
            ),
            elevation=3,
            margin=ft.margin.all(8),
        )

    return ft.Column(
        [
            ft.Text("📘 Introdução ao NumPy", size=24, weight="bold"),
            ft.Text(
                "Antes de mergulhar nos arrays, vamos entender o que é o NumPy e como configurá-lo no seu ambiente.",
                size=16,
                italic=True,
            ),

            create_card(
                "O que é NumPy?",
                "NumPy é uma das bibliotecas mais importantes do Python para computação numérica. "
                "Ela permite trabalhar com arrays multidimensionais e oferece funções matemáticas de alto desempenho. "
                "É a base de várias outras bibliotecas como Pandas, SciPy e Scikit-learn."
            ),

            create_card(
                "Como instalar",
                "Se você ainda não tem o NumPy instalado, pode usar o comando no terminal:\n\n"
                "👉 pip install numpy\n\n"
                "Se estiver usando Jupyter Notebook ou Google Colab, geralmente já vem instalado por padrão."
            ),

            create_card(
                "Como importar",
                "A convenção mais usada é importar o NumPy com o apelido np:\n\n"
                "👉 import numpy as np\n\n"
                "Assim você pode chamar suas funções de forma mais curta, como np.array() ou np.mean()."
            ),

            create_card(
                "Por que usar NumPy?",
                "✅ Mais rápido e eficiente que listas do Python para cálculos numéricos.\n"
                "✅ Permite trabalhar com grandes conjuntos de dados.\n"
                "✅ Base para bibliotecas de análise de dados e inteligência artificial."
            ),
        ],
        spacing=16,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        scroll=ft.ScrollMode.AUTO,
    )
