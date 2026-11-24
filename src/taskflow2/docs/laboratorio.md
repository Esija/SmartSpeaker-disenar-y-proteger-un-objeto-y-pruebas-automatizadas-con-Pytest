# Lab 2 SmartSpeaker: diseñar y proteger un objeto

## Las reglas de negocio identificadas.

|   Elemento    |                            Regla que debe cumplir                        |        Ejemplo inválido            |
|---------------|--------------------------------------------------------------------------|------------------------------------|
|   Nombre      |    Debe ser una cadena de texto no vacía ni formada solo por espacios    |            ""                      |
|   Volumen     |	 Debe ser un número entero entre 0 y 100, ambos incluidos              |            -5                      |
|   Estado      |    Solo puede representar si el altavoz está encendido o apagado         |        "quizá"                     |
|   Encendido   |    Debe cambiarse mediante una operación del objeto                      |    altavoz.encendido = True        |

## Diseño de la interfaz pública.

|          Elemento          |      ¿Público o interno?     |        ¿Cómo debería utilizarse?              |
|----------------------------|------------------------------|-----------------------------------------------|
|   Nombre del altavoz       |       Esta interna           |   Consultar y modificar con validación        |
|   Volumen                  |	     Esta interna           |   Consultar y modificar con validación        |
|   Estado de encendido      |       Esta interna           |   Consultar, pero no modificar directamente   |
|   Operación para encender  |       Esta interna           |   Cambiar el estado                           |
|   Operación para apagar    |       Esta interna           |   Cambiar el estado                           |


## Una explicación de las propiedades utilizadas.

He usado en todas la opcion de que se almacene internamente e inlcuso el @setter para controlar las modificaciones, excepto en las opcion de apagar o encender que tan solo un @propierty para que asi tan solo se pueda consultar el dato mediante una interfaz pública

## Los resultados de las pruebas válidas e inválidas.

Los resultados de las pruebas están demostradas en el fichero pruebas_manuales.py

## Dos recomendaciones de la IA y la decisión tomada sobre ellas.
A continuación adjunto las 2 recomendaciones de la IA:

Errores de validación

Error 1: Permites decimales en el volumen
Actualmente tienes:

    if not isinstance(nuevo_volumen, (int, float)): 
    
        raise ValueError("El volumen debe ser un número")


El problema es que aceptas tanto int como float.

Por ejemplo, estos valores serían aceptados:

        altavoz = Altavoz("Sony", 50.5)

        altavoz = Altavoz("Sony", 75.8)


Pero el requisito establece que el volumen debe ser un entero.

Corrección recomendada:

        if not isinstance(nuevo_volumen, int):    
            raise ValueError("El volumen debe ser un número entero")


Hay un pequeño detalle adicional: en Python, bool es una subclase de int.

Por tanto, True y False también superarían esa comprobación.

Si quieres evitarlo:

    if not isinstance(nuevo_volumen, int) or isinstance(nuevo_volumen, bool): 

        raise ValueError("El volumen debe ser un número entero")



Error 2: Mensajes de error

En la validación del nombre utilizas:

    raise ValueError("El título debe ser una cadena de texto")


Y:

    raise ValueError("El título no puede estar vacío")

No es un error de funcionamiento, pero estás desarrollando una clase Altavoz, así que sería más coherente utilizar la palabra nombre en lugar de título


**De los dos erorres detectados, el segundo es tema de gustos y tal, y el primero si es verdad que lo he modificado y me ha ayudado en esa parte que no me di cuenta**


## Una reflexión final: ¿qué ventajas tiene que la clase controle sus propias reglas?

Al fin y al cabo que tenga sus propias reglas le da un control y un diseño muy firme a la clase, y no hacerla simple y que cualquier error puede afectar sin pruebas previas

