import flet as ft
import search_tela as sh

bg_principal = "#090B0D"
txt_color = "#E1F0EB"
bg_containers = "#1F2326"

def main(page: ft.Page):
    page.title = "Menu Principal"
    page.vertical_alignment = "start"
    page.horizontal_alignment = "center"

    # Container do Titulo
    titulo = ft.Text(
        "Sessão Cinema - V e S ❤️",
        size = 30,
        weight = "bold",
        color = "white",
        text_align = "center",
        )

    container_titulo = ft.Container(
        content = titulo,
        padding = ft.padding.only(top=20),
    )
    page.add(container_titulo)

    # Primeiro container
    container_opcao1 = ft.Container(
        content = ft.Text("PESQUISAR FILME",
                          size = 18,
                          text_align = "center",
                          color = "white"),
        border_radius = 10,
        bgcolor = bg_containers,
        margin = ft.margin.only(top=50, bottom=20),
        padding = 20,
        width = page.width * 0.6,
        ink = True,
        on_click = lambda e: page.go("/"),
    )
    page.add(container_opcao1)

    # Segundo Container
    container_opcao2 = ft.Container(
        content = ft.Text("LISTA DE FILMES ADICIONADOS",
                          size = 18,
                          text_align = "center",
                          color = "white"
                          ),
        border_radius = 10,
        bgcolor = bg_containers,
        padding = 20,
        width = page.width * 0.6,
        ink = True,
        on_click = lambda e: print("Listando"),
    )
    page.add(container_opcao2)

if __name__ == '__main__':
    ft.app(main)