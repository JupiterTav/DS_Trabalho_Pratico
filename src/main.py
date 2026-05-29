# TODO: classe campo_texto para leitura do texto (linhas) do usuario (posteriormente parte da GUI) [x]
# TODO: main: classe mixer (GerenciadorDeMusica) -> chama gerenciador_vozes e gerenciador_midi além de outras tarefas operacionais [x]
# TODO: Escrever a classe track (antiga voz) [x]
# TODO:  - Parametros e metodos associados aos parametros
# TODO:  - Metodos associados as tracks do midi (tocar nota, mudar instrumento, silencio)

from campo_texto import CampoTexto
from gerenciador_vozes import GerenciadorVozes
from gerenciador_midi import GerenciadorMidi


texto = CampoTexto()
texto.le_texto()

gerenciador_de_vozes = GerenciadorVozes()
vozes = gerenciador_de_vozes.gerar_vozes(texto)

gerenciador_arq = GerenciadorMidi()

gerenciador_arq.gerarArquivo("build/musica")
