import pytest
from src.track import Track


@pytest.fixture
def track_instancia():
    return Track("lorem ipsum", 100, 5)


def testa_volume_maior_que_maximo_deve_retornar_127(track_instancia):
    track_instancia.volume = 130

    assert track_instancia.volume == 127


def testa_volume_negativo_deve_retornar_0(track_instancia):
    track_instancia.volume = -100

    assert track_instancia.volume == 0


def testa_oitava_maior_que_9_deve_permancer_na_oitava_original(track_instancia):
    oitava_original = track_instancia.oitava
    track_instancia.oitava = 10

    assert track_instancia.oitava == oitava_original


def testa_oitava_maior_que_9_apos_mudanca_na_oitava_deve_voltar_oitava_original(track_instancia):
    oitava_original = track_instancia.oitava
    track_instancia.oitava = 2
    track_instancia.oitava = 10

    assert track_instancia.oitava == oitava_original


def testa_oitava_menor_que_0_deve_permanecer_na_oitava_original(track_instancia):
    oitava_original = track_instancia.oitava
    track_instancia.oitava = -2

    assert track_instancia.oitava == oitava_original
