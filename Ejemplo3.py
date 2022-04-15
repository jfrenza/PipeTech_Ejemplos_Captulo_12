'''
Capítulo 12: Ejemplos Strings - Ejemplo 3

En el tercer ejemplo vamos a crear una función
que tomará una palabra como argumento. La función
debe regresar esa palabra escrita de forma inversa.

'''
def palabra_inversa(palabra):
    palabra_invertida = ""
    for i in range(len(palabra)-1, -1, -1):
        palabra_invertida += palabra[i]
    return palabra_invertida

print(palabra_inversa('Python'))
