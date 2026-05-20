from leitorTexto import LeitorTexto
from gerenciadorVozes import GerenciadorVozes


# Gerenciador Musica
campoTexto = LeitorTexto()

campoTexto.get_texto()

gerenciador_vozes = GerenciadorVozes()
gerenciador_vozes.criar_vozes(campoTexto)

gerenciador_vozes.get_vozes()
