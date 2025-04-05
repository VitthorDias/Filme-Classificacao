import flet as ft
from main import pesquisa_tmdb

def tela_pesquisa(page: ft.Page):
    def button_select(id_filme = int):
        filmes_selecionados.append(id_filme)
        print(filmes_selecionados)

    def button_search(e):
        txt.value = label_pesquisa.value
        result = pesquisa_tmdb(txt.value)

        while container_lista.controls:
            container_lista.controls.pop()

        # Container Resultados da Pesquisa de Filmes
        for item in result:
            dados = item["Filme"]

            botao_selecionar = ft.ElevatedButton(
                "Selecionar Filme",
                on_click = lambda e, id_f = dados["id"]: button_select(id_f),
            )

            lista = ft.Container(
                content = ft.Row(
                    [
                        # Imagem fica à esquerda
                        ft.Image(
                            src = f"https://image.tmdb.org/t/p/w300{dados['imagem']}",
                            width = 200,
                            height = 300,
                            fit = ft.ImageFit.COVER,
                            border_radius = 20,
                        ),
                        ft.Column(
                            [
                                ft.Text(dados['titulo'], size = 25, weight = "bold", selectable = True),
                                ft.Text(dados['avaliacao'], size = 15, color = "green", selectable = True),
                                ft.Text(dados['sinopse'], size = 15, selectable = True),
                                botao_selecionar
                            ],
                            spacing = 10,
                            alignment = "start",
                            expand = True,
                        ),
                    ],
                    spacing = 20,
                    alignment = 'start',
                ),
                padding = 10,
                bgcolor = "#1F2326",
                border_radius = 20,
                width = page.width * 0.85,
            )
            container_lista.controls.append(lista)
            container_lista.update()

    # Variaveis extras
    filmes_selecionados = []

    page.title = "Pesquisar Filmes"

    # Título
    titulo = ft.Text("PESQUISAR FILME",
                     size = 30,
                     weight = "bold",
                     color = "white",
                     text_align = "center",
                     )

    container_titulo = ft.Container(
        content = titulo,
        alignment = ft.alignment.top_center,
        padding = ft.padding.only(top=20),
    )

# PopupMenu
    menu_popup = ft.PopupMenuButton(
        items = [
            ft.PopupMenuItem(
                icon = ft.Icons.ARROW_BACK,
                text = "Voltar",
                on_click = lambda _: page.go("/"),
            ),
            #ft.PopupMenuItem(icon = ft.Icons.MENU, text="Teste"),
        ],
        icon = ft.Icons.MENU,
    )

    container_menu_popup = ft.Container(
        content = menu_popup,
        alignment = ft.alignment.top_right,
        padding = ft.padding.only(top=20, right=20),
    )

    # Bloco para pesquisar filme
    txt = ft.Text()
    label_pesquisa = ft.TextField(
        label = "Pesquisa",
        hint_text = "Digite o nome do filme",
        icon = ft.Icons.VIDEO_CAMERA_FRONT,
        bgcolor = "white",
        border = ft.InputBorder.UNDERLINE,
        filled = True,
        color = "black",
    )
    btn_pesquisa = ft.ElevatedButton(
        text = "Pesquisar",
        on_click = button_search,
    )

    container_pesquisa = ft.Container(
        content = label_pesquisa,
        padding = ft.padding.only(top=20),
        width = page.width * 0.5,
    )

    # Container responsável por mostrar o resultado dos filmes pesquisados
    container_lista = ft.Column()

    # Header com titulo e menu
    header = ft.Stack(
        controls = [
            container_titulo,
            container_menu_popup,
        ],
        width = page.width,
    )

    # Container principal
    container_main = ft.Container(
        content = ft.Column(
            controls = [
                header,
                container_pesquisa,
                btn_pesquisa,
                container_lista,
            ],
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = "center",
        ),
        alignment = ft.alignment.center
    )

    container_stack = ft.Stack(
        controls = [
            ft.Image(
                src = f"/imagens/bg_cinema.jpg",
                fit = ft.ImageFit.COVER,
                opacity = 0.1,
                expand = True
            ),
            container_main,
        ],
        expand = True,
    )

    return ft.View(
        route = "/pesquisar",
        controls=[
            container_stack,
        ],
        horizontal_alignment = "center",
        scroll = "auto",
    )