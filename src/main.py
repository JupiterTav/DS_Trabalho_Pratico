from .campo_texto import CampoTexto
from .gerador_vozes import GeradorVozes
from .gerenciador_midi import GerenciadorMidi

def main():
    texto = CampoTexto()
    texto.le_texto()

    gerador_vozes = GeradorVozes()
    vozes = gerador_vozes.gerar_vozes(texto.Linhas)

    gerenciador_arq = GerenciadorMidi()
    _ = gerenciador_arq.criar_arquivo("build/musica")

    gerenciador_arq.processar_arquivo(vozes, gerador_vozes)

    gerenciador_arq.salvar_arquivo()

if __name__ == "__main__":
    main()
