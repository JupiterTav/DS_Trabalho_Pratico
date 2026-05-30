# TODO: Escrever a classe track (antiga voz) [x]
# TODO:  - Parametros e metodos associados aos parametros
# TODO:  - Metodos associados as tracks do midi (tocar nota, mudar instrumento, silencio)

from campo_texto import CampoTexto
from gerador_vozes import GeradorVozes
from gerenciador_midi import GerenciadorMidi


def main():
    texto = CampoTexto()
    texto.le_texto()

    gerador_vozes = GeradorVozes()
    vozes = gerador_vozes.gerar_vozes(texto)

    gerenciador_arq = GerenciadorMidi()
    gerenciador_arq.gerarArquivo("build/musica")

    gerenciador_arq.processaTracks(vozes, gerador_vozes)

    gerenciador_arq.salvaArquivo()

if __name__ == "__main__":
    main()
