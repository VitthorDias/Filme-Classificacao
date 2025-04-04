import flet as ft

def main(page: ft.Page):
    page.title = "Pesquisar Filmes"
    page.vertical_alignment = "start"
    page.horizontal_alignment = "center"

    titulo = ft.Text("PESQUISAR FILME",
                     size=30,
                     weight="bold",
                     color="white",
                     text_align="center",
                     )
    page.add(titulo)

