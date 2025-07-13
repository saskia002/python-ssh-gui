import flet as ft

from dto.ServerInfoDto import ServerInfoDto
from ssh import ssh


class ServerCard(ft.Card):
    def __init__(self, dto: ServerInfoDto):
        self.serverInfoDto = dto
        super().__init__(
            ft.Container(
                content=ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text(f"Server address: {self.serverInfoDto.server}", expand=True),
                                ft.Text(f"User: {self.serverInfoDto.user}", expand=True),
                            ]
                        ),
                        ft.IconButton(
                            icon=ft.Icons.KEYBOARD_DOUBLE_ARROW_RIGHT,
                            on_click=self._handle_connect
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                padding=ft.padding.all(16),
                alignment=ft.alignment.center_right,
            ),
            width=500,
            height=100,
        )

    def is_isolated(self):
        return True

    def _handle_connect(self, e):
        ssh.connect(self.serverInfoDto.server, self.serverInfoDto.user, self.serverInfoDto.password)
