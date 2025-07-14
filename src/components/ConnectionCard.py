from sys import maxsize
from typing import Literal

import flet as ft

from dto import ConnectionInfoDto
from ssh import fedora_ssh


class ConnectionCard(ft.Container):

    def __init__(self, dto: ConnectionInfoDto, action_mode: Literal["NORMAL", "EDIT", "DELETE"]):
        self.connection_info_dto = dto
        self.action_mode = action_mode

        super().__init__(
            ft.Card(
                ft.Container(
                    ft.Row(
                        [
                            ft.Row(
                                [
                                    ft.Text(
                                        f"{self.connection_info_dto.user}@{self.connection_info_dto.server}",
                                        theme_style=ft.TextThemeStyle.TITLE_MEDIUM
                                    )
                                ],
                                expand=True,
                                vertical_alignment=ft.alignment.center

                            ),
                            self._get_buttons()
                        ],
                        expand=True,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    padding=ft.padding.all(16),
                ),
                surface_tint_color=ft.Colors.BLUE
            ),
            expand=True,
            col={"xs": 12, "md": 12, "lg": 6},
        )

    def _handle_connect(self, _e: ft.ControlEvent):
        fedora_ssh.connect(self.connection_info_dto.server, self.connection_info_dto.user,
                           self.connection_info_dto.password)

    def _get_buttons(self):
        if self.action_mode == "EDIT":
            return ft.Row(
                [
                    ft.IconButton(
                        icon_color=ft.Colors.RED,
                        icon=ft.Icons.DELETE,
                        on_click=self._handle_connect,
                        icon_size=24,
                        # tooltip=ft.Tooltip(message="Delete connection", prefer_below=False),
                    ),
                    ft.IconButton(
                        icon=ft.Icons.EDIT,
                        on_click=self._handle_connect,
                        icon_size=24,
                        # tooltip=ft.Tooltip(message="Edit connection", prefer_below=False),
                    ),
                ]
            )

        return ft.IconButton(
            icon=ft.Icons.KEYBOARD_DOUBLE_ARROW_RIGHT,
            on_click=self._handle_connect,
            icon_size=24,
            # tooltip=ft.Tooltip(message="Connect", prefer_below=False),
        )
