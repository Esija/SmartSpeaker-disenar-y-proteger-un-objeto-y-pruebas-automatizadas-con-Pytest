# Lab 2 SmartSpeaker: pruebas automatizadas con Pytest

## Relación de requisitos comprobados.

Estan comprobadas en el test_altavoz.py: 

    (taskflow2) PS C:\Todo PC\Taskflow2> uv run pytest
    ============================================================================================== test session starts ===============================================================================================
    platform win32 -- Python 3.14.7, pytest-9.2.0, pluggy-1.7.0
    rootdir: C:\Todo PC\Taskflow2
    configfile: pyproject.toml
    collected 8 items                                                                                                                                                                                                 

    tests\test_altavoz.py ........                                                                                                                                                                              [100%]

    =============================================================================================== 8 passed in 0.06s ================================================================================================
    (taskflow2) PS C:\Todo PC\Taskflow2> 

## Descripción de los principales casos de prueba

Son para principalmente verificar que con el pytest tenemos bien creada la parte de alatavoz.py, pongo algunos ejemplos:

    def test_altavoz_se_crea_con_nombre():
        altavoz = Altavoz("Salón", 30)

        assert altavoz.nombre == "Salón"
    ------------------------------------------------
    def test_altavoz_se_crea_con_volumen_inicial():
        altavoz = Altavoz("Salón", 30)

        assert altavoz.volumen == 30
    ------------------------------------------------
    def test_altavoz_se_crea_con_estado_inicial_apagado():
        altavoz = Altavoz("Salón", 30)

        assert altavoz.encendido == "Apagado"
    ------------------------------------------------
    def test_nombre_altavoz_no_puede_ser_vacio():
        try:
            altavoz = Altavoz("", 30)
        except ValueError as e:
            assert str(e) == "El título no puede estar vacío"
        else:
            assert False, "Se esperaba un ValueError"
    ------------------------------------------------

Casos básicos que como explico dan una idea de como estamos verificando que esté todo correcto

## Ejemplo de una prueba que haya fallado al introducir un error deliberadamente

Aqui he modificado el test del volumen entre 0 y 100 para que se vea que al poner un digito fuera de ese rango el test falle:

    (taskflow2) PS C:\Todo PC\Taskflow2> uv run pytest
    ================= test session starts =====================================
    platform win32 -- Python 3.14.7, pytest-9.2.0, pluggy-1.7.0
    rootdir: C:\Todo PC\Taskflow2
    configfile: pyproject.toml
    collected 8 items                                                                                                                                                                                                 

    tests\test_altavoz.py .....F..                                                                                                                                                                              [100%]

    ======================= FAILURES =================================================================================
    _______ test_volumen_altavoz_debe_ser_numero_entre_0_y_100_ambos_incluidos ____________________________________________________

        def test_volumen_altavoz_debe_ser_numero_entre_0_y_100_ambos_incluidos():
    >       altavoz = Altavoz("Salón", 101)
                    ^^^^^^^^^^^^^^^^^^^^^

    tests\test_altavoz.py:33: 
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
    src\taskflow2\altavoz.py:4: in __init__
        self.volumen = volumen
        ^^^^^^^^^^^^
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    self = <taskflow2.altavoz.Altavoz object at 0x000001241F6A3E30>, nuevo_volumen = 101

        @volumen.setter
        def volumen(self, nuevo_volumen):
            if not isinstance(nuevo_volumen, int) or isinstance(nuevo_volumen, bool):
                raise ValueError("El volumen debe ser un número entero")
        
            if nuevo_volumen < 0 or nuevo_volumen > 100:
    >           raise ValueError("El volumen debe estar entre 0 y 100")
    E           ValueError: El volumen debe estar entre 0 y 100

    src\taskflow2\altavoz.py:31: ValueError
    ============================= short test summary info ================================
    FAILED tests/test_altavoz.py::test_volumen_altavoz_debe_ser_numero_entre_0_y_100_ambos_incluidos - ValueError: El volumen debe estar entre 0 y 100
    =================================== 1 failed, 7 passed in 0.15s ===========================================
    (taskflow2) PS C:\Todo PC\Taskflow2> 


## Reflexión sobre las sugerencias de la IA: cuáles has incorporado y cuáles has descartado, justificando las decisiones.

Sobre la IA el cambio mas grande ha sido saber como usar el pytest.raises() (junto con lo visto en el ejemplo del LAB), ya que sin ello me estaba viendo perdido (sin que me de la IA el codigo).

De diseño me ha dado la opción del test de comprobar el numero decimal en el volumen que no tenia indicado

