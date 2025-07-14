from components.ConnectionCard import ConnectionCard
from ssh.cache import connection_cache
import flet as ft
import distro


def main(page: ft.Page):
    def add_connection(e):
        print(f"Adding {e}")
        ...

    page.title = "SSH Connection Manager"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.PURPLE)
    page.window.max_height, page.window.max_width = 1000, 520
    page.window.min_height, page.window.min_width = 0, 520
    page.window.width = 520
    page.scroll = ft.ScrollMode.ADAPTIVE
    # page.window.resizable = False
    page.window.maximizable = False
    # page.adaptive = True
    page.window.center()
    page.update()



    if not f"{distro.name()} {distro.version()}".startswith("Fedora Linux 42"):
        page.add(
            ft.SafeArea(
                ft.Container(
                    ft.Card(
                        ft.Container(
                            ft.Text("Please install Fedora Linux 42 to use the SSH Connection Manager",
                                    theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                            padding=ft.padding.only(top=16, right=24, bottom=16, left=24),
                        ),
                    ),
                    expand=True,
                    alignment=ft.alignment.top_center,
                )
            )
        )
        exit(1)


    connections = connection_cache.load()

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Text("Connect to SSH", theme_style=ft.TextThemeStyle.HEADLINE_SMALL),
                                ft.Text("Select an existing connection below or create a new one.", theme_style=ft.TextThemeStyle.LABEL_LARGE),
                            ]
                        ),
                        alignment=ft.alignment.top_left,
                        padding=ft.padding.only(left=10, top=10, right=10),
                    ),
                    ft.Column(
                        [
                            ft.Column([ConnectionCard(connection) for connection in connections]),
                            ft.Card(
                                ft.Container(
                                    ft.Column(
                                        [
                                            ft.Text("Add new connection", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                                            ft.Container(
                                                ft.Column(
                                                    [
                                                        ft.IconButton(icon=ft.Icons.ADD, on_click=add_connection, icon_size=28)
                                                    ],

                                                ),
                                                expand=True,
                                                alignment=ft.alignment.center,
                                            )
                                        ],

                                    ),
                                    padding=ft.padding.only(top=16, right=16, bottom=12, left=16),
                                ),
                                width=500
                            )
                        ]
                    )
                ],
                expand=True,
                spacing=20,
            ),
            expand=True,
        ),
    )


ft.app(main, view=ft.AppView.WEB_BROWSER, port=8080)
