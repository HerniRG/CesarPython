def cesar(cadena, codificacion):
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ "
    cifrado_realizado = ""
    long_alfabeto = len(alfabeto)

    for caracter in cadena:
        if caracter in alfabeto:
            indice = alfabeto.index(caracter)
            indice_cifrado = (indice + codificacion) % long_alfabeto
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
        return cesar(cadena, d * -1)
    return cifrador_interno, descifrador_interno


