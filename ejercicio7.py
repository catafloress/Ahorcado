entrada = input("Ingrese palabras separadas por espacio: ")

palabras = entrada.split()

resultado = []

for palabra in palabras:
    if len(palabra) > 3:
        resultado.append(palabra)

oracion = " ".join(resultado)

print("Oracion:", oracion)
