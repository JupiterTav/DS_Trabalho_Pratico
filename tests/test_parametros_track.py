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

