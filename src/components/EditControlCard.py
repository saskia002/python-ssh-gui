import flet as ft


class EditControlCard(ft.Card):
    EDIT_ON_TOOLTIP = "Edit connections"
    EDIT_OFF_TOOLTIP = "Stop editing connections"

    def __init__(
            self,
            on_click: callable = None,
    ):
        self.on_click = on_click
        self.edit_last_state = False

        # self.icon_button_tooltip = ft.Tooltip(message=self.EDIT_ON_TOOLTIP)

        self.icon_button = ft.IconButton(
            icon=ft.Icons.EDIT_OUTLINED,
            on_click=self._edit_connection,
            icon_size=24,
            # tooltip=self.icon_button_tooltip,
        )

        super().__init__(
            ft.Container(
                content=self.icon_button,
                expand=True,
                alignment=ft.alignment.center,
                padding=ft.padding.only(top=16, right=16, bottom=12, left=16),
            ),
            expand=True,
            surface_tint_color=ft.Colors.GREEN,
        )

    def _edit_connection(self, e: ft.ControlEvent):
        self.edit_last_state = not self.edit_last_state
        self.icon_button.icon = ft.Icons.EDIT_OFF if self.edit_last_state else ft.Icons.EDIT_OUTLINED
        # self.icon_button_tooltip.message = self.EDIT_OFF_TOOLTIP if self.edit_last_state else self.EDIT_ON_TOOLTIP
        self.icon_button.update()

        if self.on_click:
            self.on_click(e)
