import pytest
from src.core.track import Track


@pytest.fixture
def track_instancia():
    return Track("lorem ipsum", 100, 5)

def testa_volume_maior_que_maximo_deve_retornar_127(track_instancia: Track):
    track_instancia.volume = 130

    assert track_instancia.volume == 127


def testa_volume_negativo_deve_retornar_0(track_instancia: Track):
    track_instancia.volume = -100

    assert track_instancia.volume == 0


def testa_oitava_maior_que_9_deve_permancer_na_oitava_original(track_instancia: Track):
    oitava_original = track_instancia.oitava
    track_instancia.oitava = 10

    assert track_instancia.oitava == oitava_original


def testa_oitava_maior_que_9_apos_mudanca_na_oitava_deve_voltar_oitava_original(track_instancia: Track):
    oitava_original = track_instancia.oitava
    track_instancia.oitava = 2
    track_instancia.oitava = 10

    assert track_instancia.oitava == oitava_original


def testa_oitava_menor_que_0_deve_permanecer_na_oitava_original(track_instancia: Track):
    oitava_original = track_instancia.oitava
    track_instancia.oitava = -2

    assert track_instancia.oitava == oitava_original

def testa_dobro_volume_deve_retornar_dobro(track_instancia: Track):
    track_instancia.volume = 50
    track_instancia.volume = track_instancia.volume * 2 
    assert track_instancia.volume == 100

def testa_dobro_que_ultrapassa_limite_deve_retornar_127(track_instancia: Track):
    track_instancia.volume = track_instancia.volume * 2
    assert track_instancia.volume == 127 

def test_multiplicacao_por_negativo_deve_zerar_volume(track_instancia: Track):
    track_instancia.volume = track_instancia.volume * -1
    assert track_instancia.volume == 0

def test_track_eh_atrasada_deve_retornar_true():
    track_ = Track("[10]TESTE", 0, 0)
    assert track_.eh_atrasado() == True

def test_track_eh_atrasado_bracket_fora_do_lugar_deve_retornar_falso():
    track_ = Track("10[Teste", 0, 0)
    assert track_.eh_atrasado() == False
