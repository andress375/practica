import string
# abc= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

alfabeto = list(string.ascii_lowercase)
# alfabeto.insert(14,"ñ") # Este sirve igual
alfabeto.insert(alfabeto.index("o"), "ñ")
print(alfabeto)
# Esta funcion recibe un texto y lo cifra


def cifrado_cesar(alfabeto, n, texto):
    texto_cifrado = ""
    for letra in texto:
        if letra in alfabeto:
            indice_actual = alfabeto.index(letra)
            indice_cesar = indice_actual + n
            if indice_cesar > 25:
                indice_cesar -= 26
            texto_cifrado += alfabeto[indice_cesar]
        else:
            texto_cifrado += letra
    return texto_cifrado


cifrar = input("Introduce un texto para cifrar: ")
saludo_cifrado = cifrado_cesar(alfabeto, 3, cifrar)
print(saludo_cifrado)


# Este trozo recibe un texto cifrado y lo descifra
def descifrado_cesar(alfabeto, n, text):
    texto_descifrado = ""
    for letra in text:
        if letra in alfabeto:
            indice_actual = alfabeto.index(letra)
            indice_cesar = indice_actual - n
            if indice_cesar > 25:
                indice_cesar -= 26
            texto_descifrado += alfabeto[indice_cesar]
        else:
            texto_descifrado += letra
    return texto_descifrado


descifrar = input("Introduce un texto que desees descifrar: ")
saludo_descifrado = descifrado_cesar(alfabeto, 3, descifrar)
print(saludo_descifrado)
print("andy trabaja mas en tu codigo")
