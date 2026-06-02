import customtkinter as ctk

class PianoKey(ctk.CTkFrame):
    def __init__(self, master, note: str, bind_key: str, on_click, on_release=None, is_black: bool = False, width: int = 40, height: int = 120):
        super().__init__(master, width=width, height=height, fg_color="black" if is_black else "white", border_width=1, border_color="gray")
        self.note = note
        self.bind_key = bind_key
        self.on_click = on_click
        self.on_release = on_release
        self.default_color = "black" if is_black else "white"
        self.active_color = "gray"

    def set_active(self, is_active: bool):
        if is_active:
            self.configure(fg_color=self.active_color)
        else:
            self.configure(fg_color=self.default_color)

    def _on_press(self, event=None):
        self.configure(fg_color=self.active_color)
        if self.on_click:
            self.on_click(self.note)
        
    def _on_release(self, event=None):
        self.configure(fg_color=self.default_color)
        if self.on_release:
            self.on_release(self.note)
