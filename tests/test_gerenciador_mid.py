import pytest
from src.gerenciador_midi import GerenciadorMidi

def testa_se_arquivo_foi_criado_diretorio_nao_existente():
    midi_file = GerenciadorMidi()
    _ = midi_file.criar_arquivo("tmp/build/test_midi")
    assert _ == 0 
    
    outro = midi_file.criar_arquivo("test/build/test2_midi")
    assert outro == 0   

