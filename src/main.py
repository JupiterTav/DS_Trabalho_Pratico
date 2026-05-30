# TODO: Escrever a classe track (antiga voz) [x]
# TODO:  - Parametros e metodos associados aos parametros
# TODO:  - Metodos associados as tracks do midi (tocar nota, mudar instrumento, silencio)

from campo_texto import CampoTexto
from gerador_vozes import GeradorVozes
from gerenciador_midi import GerenciadorMidi
from eventos_midi import EventosMidi

def main():
    texto = CampoTexto()
    texto.le_texto()

    gerador_vozes = GeradorVozes()
    vozes = gerador_vozes.gerar_vozes(texto)

    evento_midi = EventosMidi()
    gerenciador_arq = GerenciadorMidi()
    gerenciador_arq.gerarArquivo("build/musica")

    for i, voz in enumerate(vozes):
        track = gerenciador_arq.criaTrack(track_name=f'voz {i}')
        track.append(evento_midi.define_volume(channel=i, volume=voz.volume))

        for j, char in enumerate(voz.texto_track):

            if char in evento_midi._notas_midi:
                track.extend(evento_midi.interpretaEventoMidi(char, channel=i, voz=voz))

            elif evento_midi._gm_intruments or 'abcdefgh':
                track.append(evento_midi.interpretaEventoMidi(char, channel=i, voz=voz))

            elif char.isnumeric():
                track.append(evento_midi.interpretaEventoMidi(voz.texto_track[j-1], channel=i, voz=voz))

    gerenciador_arq.salvaArquivo()

if __name__ == "__main__":
    main()
