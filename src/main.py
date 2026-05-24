from leitorTexto import LeitorTexto
from gerenciadorVozes import GerenciadorVozes
from gerenciadorArquivoMidi import GerenciadorArquivoMidi
import os

# Gerenciador Musica
campoTexto = LeitorTexto()

campoTexto.get_texto()

gerenciador_vozes = GerenciadorVozes()
gerenciador_vozes.criar_vozes(campoTexto)
#TODO: 
    # Criar Interpretador(Parser) para possibilitar comunicação dos dados das vozes (texto do usuario) com midi -> usando Mido
    # Escrever arquivo midi com as vozes criadas
gerenciador_midi = GerenciadorArquivoMidi()
gerenciador_midi.criarArquivo("build/musica_gerada", gerenciador_vozes)

