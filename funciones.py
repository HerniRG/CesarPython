def cesar(cadena: str, codificacion: int) -> str:
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ "
    cifrado_realizado = ""
    long_alfabeto = len(alfabeto)

    for caracter in cadena.upper():
        if caracter in alfabeto:
            indice = alfabeto.index(caracter)
            indice_cifrado = (indice + codificacion) % long_alfabeto # si es mayor de long alfabeto se hace modulo para saber el sobrante y empezar de nuevo 
            cifrado_realizado += alfabeto[indice_cifrado]
        else:
            cifrado_realizado += caracter
    return cifrado_realizado


def crea_cifrador(d: int) -> callable:
    def cifrador_interno(cadena):
        return cesar(cadena, d)
    return cifrador_interno


def crea_par_cesar(d: int) -> tuple:
    def cifrador_interno(cadena):
        return cesar(cadena, d)
    def descifrador_interno(cadena):
        return cesar(cadena, -d)
    return cifrador_interno, descifrador_interno



class Cifrador:
    def __init__(self, d) -> None:
        self.d = d
        self.cifrados_pendientes = 5
    
    def cifrar(self, mensaje) -> str:

        if self.cifrados_pendientes == 0:
            return "Compre en cifrados Pepe!"

        self.cifrados_pendientes -= 1

        return cesar(mensaje, self.d)

   
ana = Cifrador(4)
print(ana.cifrados_pendientes)
print(ana.cifrar("Hola"))