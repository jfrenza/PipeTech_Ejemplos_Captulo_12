'''
Capítulo 12: Ejemplos Strings - Ejemplo 1

En el primer ejemplo vamos a crear una función que tome dos argumentos
el primero será una frase y el segundo una palabra. La función debe
buscar la palabra dentro de la frase y regresar "True" en caso de encontrarla
de lo contrario regresar "False"

'''

def buscar_palabra(frase, palabra):
    if palabra.lower() in frase.lower():
        return True
    return False

print(buscar_palabra('La frase contiene la palabra Felipe', 'felipe'))
