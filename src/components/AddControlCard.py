import flet as ft

class AddControlCard(ft.Card):


    def __init__(
            self,
            on_click: callable = None,
    ):
        self.on_click = on_click
        super().__init__(
                ft.Container(

                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        on_click=self._add_connection,
                        icon_size=24,
                        # tooltip=ft.Tooltip(message="Add new connection"),
                    ),
                    expand=True,
                    alignment=ft.alignment.center,
                    padding=ft.padding.only(top=16, right=16, bottom=12, left=16),
                ),
                expand=True,
                surface_tint_color=ft.Colors.GREEN

        )


    def _add_connection(self, _e: ft.ControlEvent):
        print("child")
        self.on_click(_e)

