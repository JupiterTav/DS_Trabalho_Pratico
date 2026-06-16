import pathlib
import shutil
import sys
import tkinter as tk
from tkinter import messagebox
from mixer import Mixer
from ui.janela_principal import JanelaPrincipal

def verificar_dependencias():
    base_dir = pathlib.Path(__file__).parent.parent.resolve()
    caminho_local = base_dir / "fluidsynth" / "bin" / "fluidsynth.exe"
    if not caminho_local.exists() and not shutil.which("fluidsynth"):
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(
            "Dependência Ausente",
            "O executável 'fluidsynth' não foi encontrado localmente nem no PATH do sistema.\n\n"
            "Este programa requer o Fluidsynth para gerar áudio a partir do texto.\n"
            "Por favor, certifique-se de que a pasta 'fluidsynth' está presente ou instale-o no sistema."
        )
        root.destroy()
        sys.exit(1)

def main():
    verificar_dependencias()
    
    mixer = Mixer()    
    janela = JanelaPrincipal(mixer=mixer)


    janela.mainloop()
if __name__ == "__main__":
    main()
