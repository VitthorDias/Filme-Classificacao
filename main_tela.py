import flet as ft
from search_tela import tela_pesquisa
from lista_filmes import tela_lista

bg_principal = "#090B0D"
txt_color = "#E1F0EB"
bg_containers = "#1F2326"

def main(page: ft.Page):
    page.title = "Menu Principal"
    page.vertical_alignment = "start"
    page.horizontal_alignment = "center"

    bg_img = ft.BoxDecoration(
        image = ft.DecorationImage(
            src = "imagens/bg_main.jpg",
            fit = ft.ImageFit.COVER,
            opacity=0.7,
        )
    )

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
    # page.add(container_titulo)

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
        on_click = lambda e: page.go("/pesquisar"),
    )
    # page.add(container_opcao1)

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
        on_click = lambda e: page.go("/lista"),
    )
    # page.add(container_opcao2)

    # Rotas para trocas de telas
    def route_change(route):
        # Tela principal
        if page.route == "/":
            page.views.clear()
            page.views.append(
                ft.View(
                    route = "/",
                    controls = [
                        container_titulo,
                        container_opcao1,
                        container_opcao2,
                    ],
                    horizontal_alignment = "center",
                    decoration = bg_img,
                    bgcolor = ft.Colors.with_opacity(0.7, "black")
                )
            )

        # Tela de Pesquisa
        elif page.route == "/pesquisar":
            page.views.append(tela_pesquisa(page))
        elif page.route == "/lista":
            page.views.append(tela_lista(page))

        page.update()

    page.on_route_change = route_change
    page.go("/")

if __name__ == '__main__':
    ft.app(target=main, assets_dir=".")