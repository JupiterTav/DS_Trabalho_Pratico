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
        track.append(evento_midi.define_tempo(bpm=gerador_vozes.bpm_global))
        for j, char in enumerate(voz.texto_track):

            if char in evento_midi._notas_midi or evento_midi._gm_intruments or 'abcdefgh' or char.isnumeric():
                evento_midi.interpretaEventoMidi(voz.texto_track[j], channel=i, voz=voz, track=track)

            elif char in voz.track_event:
                if char in '?.':
                    voz.oitava += 1
                elif char in 'V':
                    voz.oitava -= 1
            else:
                if voz.texto_track[j-1] in evento_midi._notas_midi:
                    track.extend(evento_midi.interpretaEventoMidi(voz.texto_track[j-1], channel=i, voz=voz))
                else:
                    track.append(evento_midi.silencia(channel=i))


    gerenciador_arq.salvaArquivo()

if __name__ == "__main__":
    main()
