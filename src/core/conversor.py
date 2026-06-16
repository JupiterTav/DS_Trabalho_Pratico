import pathlib
import subprocess


class Conversor:
    """Converte um input .mid no output desejado utilizando um sintetizador fluidsynth"""

    def __init__(self, sound_font_path: str):
        self.sound_font_path: str = sound_font_path

    def converter_midi_audio(self, *, input_path: str, output_path: str, volume: int) -> bool:
        #    fluidsynth [options] [ soundfonts ] [ midifiles ]

        base_dir = pathlib.Path(__file__).parent.parent.parent.resolve()
        caminho_local = base_dir / "fluidsynth" / "bin" / "fluidsynth.exe"
        comando = str(caminho_local) if caminho_local.exists() else "fluidsynth"

        cli_conversor_comando = [
            comando,
            '-ni',
            '-r', '44100',
            '-g',
            str((volume) / 100),
            '-F',
            output_path,
            self.sound_font_path,
            input_path,
        ]
        try:
            subprocess.run(cli_conversor_comando, check=True)
            print(f"{input_path} convertido para {output_path}")
            return True
        except FileNotFoundError as e:
            executable = e.filename if e.filename else comando
            print(f'Comando ou arquivo "{executable}" nao encontrado\n Detalhe:\n {e.strerror}')
            print("Certifique-se de que o Fluidsynth está instalado ou disponível na pasta do projeto.")
            return False
