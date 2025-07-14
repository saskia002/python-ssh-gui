import flet as ft

from dto.ConnectionInfoDto import ConnectionInfoDto
from ssh import fedora_ssh


class ConnectionCard(ft.Card):
    def __init__(self, dto: ConnectionInfoDto):
        self.connectionInfoDto = dto
        super().__init__(
            ft.Container(
                ft.Row(
                    [
                        ft.Row(
                            [
                                ft.Text(f"{self.connectionInfoDto.user}@{self.connectionInfoDto.server}", theme_style=ft.TextThemeStyle.TITLE_MEDIUM)
                            ],
                            expand=True,
                            vertical_alignment=ft.alignment.center

                        ),
                        ft.IconButton(icon=ft.Icons.KEYBOARD_DOUBLE_ARROW_RIGHT, on_click=self._handle_connect, icon_size=28),
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                padding=ft.padding.all(16),
            ),
            width=500,
            height=80,

        )

    def is_isolated(self):
        return True

    def _handle_connect(self, e):
        fedora_ssh.connect(self.connectionInfoDto.server, self.connectionInfoDto.user, self.connectionInfoDto.password)
