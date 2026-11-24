class Altavoz:
    def __init__(self, nombre, volumen):
        self.nombre = nombre
        self.volumen = volumen
        self._encendido = False

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str):
            raise ValueError("El título debe ser una cadena de texto")

        if not nuevo_nombre.strip():
            raise ValueError("El título no puede estar vacío")

        self._nombre = nuevo_nombre.strip()
    
    @property
    def volumen(self):
        return self._volumen

    @volumen.setter
    def volumen(self, nuevo_volumen):
        if not isinstance(nuevo_volumen, int) or isinstance(nuevo_volumen, bool):    
            raise ValueError("El volumen debe ser un número entero")

        if nuevo_volumen < 0 or nuevo_volumen > 100:
            raise ValueError("El volumen debe estar entre 0 y 100")

        self._volumen = nuevo_volumen

    @property
    def encendido(self):
        if self._encendido:
            return "Encendido"
        else:
            return "Apagado"
            
    def encender(self):
        self._encendido = True

    def apagar(self):
        self._encendido = False