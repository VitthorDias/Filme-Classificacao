import flet as ft
from main import pesquisa_plataforma
import webbrowser
import json

def tela_lista(page: ft.Page):
    # Ler o arquivos com os filmes
    with open("base/filmes.json", 'r', encoding = 'UTF-8') as file:
       try:
           filmes = json.load(file)
       finally:
            print(f"Filmes recuperados{filmes}")
    
    bg_containers = "#1F2326"

    # 👉 Define o background apenas nesta tela
    page.decoration = ft.BoxDecoration(
        image=ft.DecorationImage(
            src="imagens/bg_lista.jpg",
            fit=ft.ImageFit.COVER,
            opacity=0.7
        )
    )
    page.bgcolor = ft.Colors.with_opacity(0.0, "white")
    page.window.always_on_top = True
    page.title = "Lista de Filmes"

    # -----------------------------------------------------------
    # Container header
    # Titulo
    titulo = ft.Text(
            "LISTA DE FILMES ADICIONADOS",
            size = 30,
            weight = "bold",
            text_align = "center",
            color = "white"
        )
    
    container_titulo = ft.Container(
        content = titulo,
        alignment = ft.alignment.top_center,
        padding = ft.padding.only(top = 20)
    )
    
    # Menu
    menu_popup = ft.PopupMenuButton(
        items = [
            ft.PopupMenuItem(
                icon = ft.Icons.ARROW_BACK,
                text = "Voltar",
                on_click = lambda e: page.go("/"),
            ),
            ft.PopupMenuItem(
                icon = ft.Icons.SCREEN_SEARCH_DESKTOP_OUTLINED,
                text = "Pesquisar",
                on_click = lambda e: page.go("/pesquisar"),
            )
        ],
        icon = ft.Icons.MENU,
    )

    container_menu = ft.Container(
        content = menu_popup,
        alignment = ft.alignment.top_right,
        padding = ft.padding.only(top = 20, left = 20)
    )

    # Juntando titulo e o menu
    header = ft.Stack(
        controls = [
            container_titulo,
            container_menu
        ],
        width = page.width,
    )

    # -------------------------------------------------------------
    # Container com a lista de filmes já adicionados
    imagens_filmes = ft.GridView(
        expand = True,
        max_extent = 200,
        child_aspect_ratio = 150 / 227,
        spacing = 10,
        run_spacing = 10,
    )

    for filme_id, dados in filmes.items():
        # Pesquisar as plataformas
        plataformas = pesquisa_plataforma(filme_id)

        linha_img = ft.Row(
            alignment = "center",
            wrap = True
        )

        for plat in plataformas["streams"]:
            nome = list(plat.keys())[0]
            valor = list(plat.values())[0]

            if nome != "Indisponível":
                plataforma = ft.Image(
                    src = f"https://image.tmdb.org/t/p/w300{valor}",
                    fit = ft.ImageFit.COVER,
                    width = 30,
                    height = 30,
                )
            else:
                plataforma = ft.Container(
                    content = ft.Text(nome.upper(), size = 11, italic = True, color = "white"),
                    bgcolor = "black",
                    padding = 10,
                    border_radius = ft.border_radius.only(bottom_left = 10, bottom_right = 10),
                )
            linha_img.controls.append(plataforma)
        
        container_linha_plat = ft.Container(
            content = linha_img,
            height = 40,
            expand = True,
            alignment = ft.alignment.center,
            padding = 5,
            # bgcolor = ft.colors.with_opacity(0.9, "black"),
            gradient = ft.LinearGradient(
                begin= ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#AA000000", "black"]
            ),
        )

        # Imagem do poster do filme
        imagem_filme = ft.Image(
                src = f"https://image.tmdb.org/t/p/w300{dados['poster']}",
                fit = ft.ImageFit.CONTAIN,
                repeat = ft.ImageRepeat.NO_REPEAT,
                border_radius = ft.border_radius.all(10),
            )
        
        stack_filme = ft.Stack(
            controls = [
                imagem_filme,
                ft.Container(
                    container_linha_plat,
                    alignment = ft.alignment.bottom_center,
                )
            ],
            expand = True,
            width = 150,
            height = 200,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS
        )

        container_imagem_filme = ft.Container(
            content = stack_filme,
            border_radius = 10,
            ink = True,
            on_click = lambda e, link = plataformas["link"]: webbrowser.open(link),
        )
        
        imagens_filmes.controls.append(container_imagem_filme)
    
    container_filmes = ft.Container(
        content = imagens_filmes,
        margin = ft.margin.only(top = 50, left = 30, right = 30),
        expand = True,
        height = page.height,
    )

    # -------------------------------------------------------------
    # Container principal
    # Junta todos containeirs
    container_main = ft.Container(
        content =ft.Column(
            controls = [
                header,
                container_filmes
            ],
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = "center",
        ),
        alignment = ft.alignment.center
    )



    return ft.View(
        route="/lista",
        controls=[container_main],
        scroll=ft.ScrollMode.AUTO,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor = ft.Colors.with_opacity(0.7, "black"),
        decoration = page.decoration
    )