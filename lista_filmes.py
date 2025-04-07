import flet as ft

def tela_lista(page: ft.Page):
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

    container_opcao2 = ft.Container(
        content=ft.Text(
            "LISTA DE FILMES ADICIONADOS",
            size=18,
            text_align="center",
            color="white"
        ),
        border_radius=10,
        bgcolor=bg_containers,
        padding=20,
        width=page.width * 0.8,
        height=300,
        ink=True,
        on_click=lambda e: page.go("/"),
        alignment=ft.alignment.center
    )

    return ft.View(
        route="/lista",
        controls=[container_opcao2],
        scroll=ft.ScrollMode.AUTO,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor = ft.Colors.with_opacity(0.3, "black"),
        decoration = page.decoration
    )