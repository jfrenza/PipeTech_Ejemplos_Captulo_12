'''
Capítulo 12: Ejemplos Strings - Ejemplo 4

En este cuarto ejemplo vamos a crear una función
que tomará una palabra como argumento. La función
debe validar si nuestra palabra tiene al menos 10
carácteres. De ser así la función regresará la palabra
de lo contrario debe añadir signos de exclamación hasta
completar los 10 carácteres y por último regresar la palabra.

'''

def adicionar_exclamacion(palabra):
    while(len(palabra) < 10):
        palabra += '!'
    return palabra

print(adicionar_exclamacion('Juan Felipe'))
