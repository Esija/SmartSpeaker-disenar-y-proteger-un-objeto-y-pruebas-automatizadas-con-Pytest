import pytest
from taskflow2.altavoz import Altavoz


def test_altavoz_se_crea_con_nombre():
    altavoz = Altavoz("Salón", 30)

    assert altavoz.nombre == "Salón"


def test_altavoz_se_crea_con_volumen_inicial():
    altavoz = Altavoz("Salón", 30)

    assert altavoz.volumen == 30


def test_altavoz_se_crea_con_estado_inicial_apagado():
    altavoz = Altavoz("Salón", 30)

    assert altavoz.encendido == "Apagado"


def test_nombre_altavoz_no_puede_ser_vacio():
    with pytest.raises(ValueError):
        Altavoz("", 30)


def test_espacios_en_nombre_altavoz_al_principio_y_al_final_son_eliminados():
    altavoz = Altavoz("   Cocina   ", 30)

    assert altavoz.nombre == "Cocina"


def test_volumen_altavoz_debe_ser_numero_entre_0_y_100_ambos_incluidos():
    altavoz = Altavoz("Salón", 30)

    with pytest.raises(ValueError):
        altavoz.volumen = 150


def test_encender_altavoz_cambia_estado_a_encendido():
    altavoz = Altavoz("Salón", 30)

    altavoz.encender()

    assert altavoz.encendido == "Encendido"


def test_apagar_altavoz_cambia_estado_a_apagado():
    altavoz = Altavoz("Salón", 30)

    altavoz.encender()
    altavoz.apagar()

    assert altavoz.encendido == "Apagado"
    
def test_volumen_altavoz_no_puede_ser_un_numero_decimal():
    altavoz = Altavoz("Salón", 30)

    with pytest.raises(ValueError):
        altavoz.volumen = 25.5
        

        


