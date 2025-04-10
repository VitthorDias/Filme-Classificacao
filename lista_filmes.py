import flet as ft
from main import pesquisa_plataforma
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
            src="imagens/bg_cinema.jpg",
            fit=ft.ImageFit.COVER,
            opacity=0.7
        )
    )
    page.bgcolor = ft.Colors.with_opacity(0.0, "white")
    page.window.always_on_top = True
    page.title = "Lista de Filmes"

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

    # Container principal
    # Junta todos containeirs
    

    return ft.View(
        route="/lista",
        controls=[header],
        scroll=ft.ScrollMode.AUTO,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor = ft.Colors.with_opacity(0.7, "black"),
        decoration = page.decoration
    )