from taskflow2.altavoz import Altavoz

def pruebas_manuales():
    
    #Pruebas Válidas:
    
    #Creamos un altavoz con nombre "Salón" y volumen 30
    altavoz = Altavoz("Salón", 30)

    print(altavoz.nombre)
    print(altavoz.volumen)
    print(altavoz.encendido)

    #Consultamos el nombre del altavoz
    print(altavoz.nombre)
    
    #Consultamos el volumen del altavoz
    print(altavoz.volumen)
    
    #Consultamos el estado inicial del altavoz
    print(altavoz.encendido)
    
    #Cambiamos el volumen a 50 y se acepta
    altavoz.volumen = 50
    print(altavoz.volumen)
    
    #Cambiamos el volumen a 0 y se acepta
    altavoz.volumen = 0
    print(altavoz.volumen)
    
    #Cambiamos el volumen a 100 y se acepta
    altavoz.volumen = 100
    print(altavoz.volumen)
    
    #Ejecutamos encender y se acepta
    altavoz.encender()
    print(altavoz.encendido)
    
    #Ejecutamos apagar y se acepta
    altavoz.apagar()
    print(altavoz.encendido)
    
    #Creamos un altavoz con nombre "  Cocina" y devuelve "Cocina"
    altavoz = Altavoz("     Cocina", 77)
    
    print(altavoz.nombre)
    print(altavoz.volumen)
    
    #Pruebas Inválidas:
        
    #Creamos un altavoz con nombre "" y da error
    #altavoz = Altavoz("", 20)
    
    #print(altavoz.nombre)
    
    #Creamos un altavoz con nombre "     " y da error
    #altavoz = Altavoz("    ", 20)
    
    #print(altavoz.nombre)
    
    #Creamos un altavoz con nombre 25 y da error
    #altavoz = Altavoz(25, 20)
    
    #print(altavoz.nombre)
    
    #Creamos un altavoz con volumen -1 y da error
    #altavoz = Altavoz("Prueba", -1)
    
    #print(altavoz.volumen)
    
    #Creamos un altavoz con volumen 101 y da error
    #altavoz = Altavoz("Prueba", 101)
    
    #print(altavoz.volumen)
    
    #Asignamos a altavoz.volumen el valor 25.5 y da error
    #altavoz.volumen = 25.5
    
    #print(altavoz.volumen)
    
    #Asignamos a altavoz.volumen el valor "alto" y da error
    #altavoz.volumen = "alto"
    
    #print(altavoz.volumen)
    
    #Asignamos a altavoz.estado el valor "encendido" y da error
    #altavoz.encendido = "encendido"
    
    #print(altavoz.encendido)
    
    
    
    
    
if __name__ == "__main__":
    pruebas_manuales()
    
    
