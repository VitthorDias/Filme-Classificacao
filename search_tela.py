import flet as ft

def tela_pesquisa(page: ft.Page):
    page.title = "Pesquisar Filmes"

    titulo = ft.Text("PESQUISAR FILME",
                     size = 30,
                     weight = "bold",
                     color = "white",
                     text_align = "center",
                     )

    container_titulo = ft.Container(
        content = titulo,
        padding = ft.padding.only(top=20)
    )

    container_main = ft.Container(
        content = ft.Column(
            [
                container_titulo,
            ],
            alignment = "center",
            horizontal_alignment = "center",
        ),
        alignment = ft.alignment.center
    )

    container_stack = ft.Stack(
        controls = [
            ft.Image(src=f"/imagens/bg_cinema.jpg", fit=ft.ImageFit.COVER, opacity=0.1),
            container_main,
        ],
    )

    return ft.View(
        route = "/pesquisar",
        controls=[
            container_stack,
        ],
        horizontal_alignment = "center",
    )