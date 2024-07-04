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


print(cesar("HOLA", -5))
print(cesar("MUNDO", 10))

cifrador1, descifrador1 = crea_par_cesar(-5)

print(cifrador1("Hola"))