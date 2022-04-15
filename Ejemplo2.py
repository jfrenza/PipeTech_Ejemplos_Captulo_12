'''
Capítulo 12: Ejemplos Strings - Ejemplo 2

En este segundo ejemplo vamos a crear una función que tomará un
argumento. La función debe recorrer la palabra ingresada y
extraer letras intermedias. La Función debe regresar un nuevo
string que esté compuesto de estas letras intermedias.

'''

def letras_intermedias(palabra):
    nueva_palabra = ""
    for letra in range(0,len(palabra), 2):
        nueva_palabra += palabra[letra]
    return nueva_palabra

print(letras_intermedias('Python'))
