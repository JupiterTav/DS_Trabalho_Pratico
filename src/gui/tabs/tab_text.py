import customtkinter as ctk

class TabText(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.txt_editor = ctk.CTkTextbox(
            self, 
            font=("Consolas", 16),
            border_width=2,
            border_color="gray"
        )
        self.txt_editor.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        self.txt_editor.bind("<FocusIn>", self._on_focus_in)
        self.txt_editor.bind("<FocusOut>", self._on_focus_out)
        self.txt_editor.bind("<Escape>", lambda e: self.master.focus_set())

    def _on_focus_in(self, event):
        self.txt_editor.configure(border_color="#1f538d")
        
    def _on_focus_out(self, event):
        self.txt_editor.configure(border_color="gray")

    def get_text(self):
        return self.txt_editor.get("1.0", "end-1c")
        
    def set_text(self, text):
        self.txt_editor.delete("1.0", "end")
        self.txt_editor.insert("1.0", text)
        
    def append_text(self, text):
        self.txt_editor.insert("end", text + " ")
