from taskflow2.altavoz import Altavoz


def main() -> None:
    altavoz = Altavoz("Salón", 30)

    print(altavoz.nombre)
    print(altavoz.volumen)
    print(altavoz.encendido)

    altavoz.nombre = "   pepe"
    altavoz.volumen = 50
    altavoz.encendido = True

    print(altavoz.nombre)
    print(altavoz.volumen)
    print(altavoz.encendido)


if __name__ == "__main__":
    main()