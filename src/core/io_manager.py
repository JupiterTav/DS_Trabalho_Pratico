import tkinter.filedialog as filedialog
import pathlib

class IOManager:
    @staticmethod
    def carrega_texto():
        filepath =filedialog.askopenfilename(
            title="Selecionar arquivo texto",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        return pathlib.Path(filepath)
    
    @staticmethod
    def salvar_arq():
        filepath = filedialog.asksaveasfilename(
            title="salvar texto",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        return pathlib.Path(filepath)

    @staticmethod
    def get_output_path() -> pathlib.Path:
        filepath = filedialog.asksaveasfilename(
            title="Salvar saída",
            defaultextension=".wav",
            filetypes=[("wav", "*.wav")])
    
        return pathlib.Path(filepath)
