import flet as ft
from main import pesquisa_tmdb
import json

def tela_pesquisa(page: ft.Page):
    def ordenar_filmes():
        with open("base/filmes.json", "rw+", encoding='utf-8') as file:
            pass


    # Função para selecionar o(s) filme(s) escolhidos
    def button_select(dados):
        filmes_selec = {}
        for chave, valor in dados.items():
            if chave != "id":
                filmes_selec[chave] = valor
        filmes[dados["id"]] = filmes_selec
        filmes_json = json.dumps(filmes, indent=4, ensure_ascii=False)

        with open("base/filmes.json", "w+", encoding='utf-8') as file:
            file.write(filmes_json)

    # Cria os containers com os resultados da pesquisa dos filmes 
    def button_search(e):
        txt.value = label_pesquisa.value
        result = pesquisa_tmdb(txt.value)

        # Limpa a lista de filmes pesquisados para mostrar nova pesquisa
        while container_lista.controls:
            container_lista.controls.pop()

        # Container Resultados da Pesquisa de Filmes
        for item in result:
            dados = item["Filme"]

            botao_selecionar = ft.ElevatedButton(
                "Selecionar Filme",
                on_click = lambda e, id_f = dados: button_select(id_f),
            )

            film_img = ft.BoxDecoration(
                image=ft.DecorationImage(
                    src=f"https://image.tmdb.org/t/p/w300{dados["capa_fundo"]}",
                    fit=ft.ImageFit.COVER,
                    opacity=0.05,
                ),
                border_radius=10,
            )

            container_classificacao = ft.Container(
                content = ft.Text(dados["classificacao"], size = 14),
                padding=ft.padding.symmetric(horizontal=6, vertical=2),
                border=ft.border.all(1, "white"),
                margin=ft.margin.only(right=5, top=-3),
            )

            lista = ft.Card(
                content = ft.Container(
                    content = ft.Row(
                        [
                            # Imagem fica à esquerda
                            ft.Image(
                                src = f"https://image.tmdb.org/t/p/w300{dados['poster']}",
                                width = 150,
                                height = 200,
                                fit = ft.ImageFit.COVER,
                                border_radius = 20,
                            ),
                            ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Text(dados['titulo'], size = 25, weight = "bold", selectable = True),
                                            ft.Text(f"({dados["lancamento"].split("-")[0]})", size = 12, selectable = True)
                                        ],
                                    ),
                                    ft.Row(
                                        [
                                            container_classificacao,
                                            ft.Text(", ".join(dados["generos"]), size = 15, selectable = True, italic = True),
                                        ],
                                    ),
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
                    foreground_decoration=film_img,
                    bgcolor = ft.Colors.with_opacity(0.0, "#1F2326"),
                    border_radius = 20,
                    width = page.width * 0.85,
                ),
                elevation = 6,
            )
            container_lista.controls.append(lista)
            container_lista.update()

    with open("base/filmes.json", 'r', encoding='UTF-8') as file:
        try:
            filmes = json.load(file)
        finally:
            print(f"Filmes recuperados: {filmes}")

    page.title = "Pesquisar Filmes"

    # --------------------------------------------------------
    # Componentes do header
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
            ft.PopupMenuItem(
                icon = ft.Icons.FEATURED_PLAY_LIST_OUTLINED,
                text = "Adicionados",
                on_click = lambda e: page.go("/lista"),
            )
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
            container_main,
        ],
        expand = True,
    )

    bg_img = ft.BoxDecoration(
        image=ft.DecorationImage(
            src="imagens/bg_cinema.jpg",
            fit=ft.ImageFit.COVER,
            opacity=0.7
        )
    )

    return ft.View(
        route = "/pesquisar",
        controls=[
            container_stack,
        ],
        horizontal_alignment = "center",
        scroll = "auto",
        decoration = bg_img,
        bgcolor = ft.Colors.with_opacity(0.7, "black")
    )