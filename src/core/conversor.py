import subprocess

class Conversor:

    def __init__(self, sound_font_path: str):
        self.sound_font_path: str = sound_font_path

    def converter_midi_audio(self, *, input_path: str, output_path: str, volume: int) -> bool:
        #    fluidsynth [options] [ soundfonts ] [ midifiles ]
        cli_conversor_comando = [ 
                "fluidsynth",
                '-ni',
                '-r 44100',
                '-g',
                str((volume) / 100),
                '-F',
                output_path ,
                self.sound_font_path,
                input_path,
                ]
        try:
            completo = subprocess.run(cli_conversor_comando, check=True) 
            print(f"{input_path} convertido para {output_path}")
            return True
        except FileNotFoundError as e:
            print(f'{e.filename} nao encontrado\n Detalhe:\n {e.strerror}')
            return False
