import flet as ft

from dto.ServerInfoDto import ServerInfoDto
import distro
from component.ServerCard import ServerCard


def main(page: ft.Page):
    def add_connection(e):
        print(f"Adding {e}")
        ...

    page.title = "SSH Connection Manager"
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.DEEP_PURPLE)

    if not f"{distro.name()} {distro.version()}".startswith("Fedora Linux 42"):
        print("This program only works on Fedora Linux 42")
        page.add(
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
        exit(1)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=add_connection
    )

    servers = [
        {
            "server": "saskia-laptop",
            "user": "saskia",
            "password": "asd",
        },
        {
            "server": "localhost",
            "user": "hax0r",
            "password": "idk"
        }
    ]

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Text("Connect to SSH", theme_style=ft.TextThemeStyle.TITLE_LARGE),
                                ft.Text("Choose a connection from down below",
                                        theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                            ]
                        ),
                        alignment=ft.alignment.top_left,
                        padding=ft.padding.only(left=10, top=10, right=10),
                    ),
                    ft.Column(
                        [
                            ServerCard(ServerInfoDto(**server))
                            for server in servers
                        ]
                    )
                ],
                expand=True,
                spacing=20,
            ),
            expand=True,
        )
    )


ft.app(main)
