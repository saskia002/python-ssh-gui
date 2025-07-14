from typing import Literal
from components import ConnectionCard, EditControlCard, AddControlCard
from ssh.cache import connection_cache
import flet as ft
import distro


def main(page: ft.Page):
    connections = connection_cache.load()
    action_mode: Literal["NORMAL", "EDIT"] = "NORMAL"

    # Less responsive way of wrapping elements like with flex box:
    #   ft.Row(expand=True, spacing=8, wrap=True, scroll=ft.ScrollMode.ADAPTIVE)
    #   and fix child component width
    cards_column = ft.ResponsiveRow(expand=True, spacing=8)

    def render_cards():
        cards_column.controls = [ConnectionCard(connection, action_mode) for connection in connections]
        cards_column.update()

    def add_connection(_e: ft.ControlEvent):
        print("parent")
        print(f"Adding {_e}")
        ...

    def edit_connection(_e: ft.ControlEvent):
        print("parent")
        nonlocal action_mode

        if action_mode == "EDIT":
            action_mode = "NORMAL"
        else:
            action_mode = "EDIT"

        render_cards()

    page.title = "SSH Connection Manager"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.DEEP_PURPLE)
    page.window.max_height, page.window.max_width = 1000, 520
    page.window.min_height, page.window.min_width = 0, 520
    page.window.width = 520
    # page.window.resizable = False  ## This Breaks window re-sizing for some reason Xd ????
    page.window.maximizable = False
    page.adaptive = True
    page.window.center()
    page.update()

    if not f"{distro.name()} {distro.version()}".startswith("Fedora Linux 42"):
        page.add(
            ft.SafeArea(
                ft.Container(
                    ft.Card(
                        ft.Container(
                            ft.Text(
                                "Please install Fedora Linux 42 to use the SSH Connection Manager",
                                theme_style=ft.TextThemeStyle.TITLE_MEDIUM
                            ),
                            padding=ft.padding.only(top=16, right=24, bottom=16, left=24),
                        ),
                    ),
                    expand=True,
                    alignment=ft.alignment.top_center,
                )
            )
        )
        exit(1)

    title: ft.Container = ft.Container(
        ft.Column(
            [
                ft.Text(
                    "Connect to SSH",
                    theme_style=ft.TextThemeStyle.HEADLINE_SMALL
                ),
                ft.Text(
                    "Select an existing connection below or create a new one.",
                    theme_style=ft.TextThemeStyle.LABEL_LARGE
                ),
            ]
        ),
        alignment=ft.alignment.top_left,
        padding=ft.padding.only(left=10, top=10, right=10),
    )

    cards: ft.Column = ft.Column(
        [cards_column],
        scroll=ft.ScrollMode.ADAPTIVE,
        expand=True
    )

    controls: ft.Container = ft.Container(
        ft.Row(
            [
                AddControlCard(on_click=add_connection),
                EditControlCard(on_click=edit_connection)
            ],
            spacing=8
        )
    )

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Column(
                    [
                        title,
                        ft.Container(
                            ft.Column(
                                [
                                    cards,
                                    controls,
                                ],
                                expand=True,
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            expand=True,
                        )
                    ],
                    expand=True,
                ),
                expand=True,
            ),
            expand=True,
        )
    )

    render_cards()


if __name__ == "__main__":
    ft.app(main, view=ft.AppView.WEB_BROWSER, port=8080, assets_dir="./assets", use_color_emoji=True)
