import pytest
from src.track import Track


def testa_volume_maior_que_maximo_deve_retornar_127():
    track_0 =  Track("lorem ipsum", 100, 5)
    track_0.volume = 130
    assert track_0.volume == 127

