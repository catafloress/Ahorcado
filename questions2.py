import random 

categorias = {"programacion": ["python", "variable", "funcion", "bucle",]
, "basico": ["programa","cadena","entero","lista"]}

palabras_usadas = []

while True:

    print("Categorías disponibles:")
    for cat in categorias:
        print("-", cat)

    categoria = input("Elegí una categoría: ")

    if categoria not in categorias:
        print("Categoría no válida\n")
        continue

    palabras_disponibles = []
    for palabra in categorias[categoria]:
        if palabra not in palabras_usadas:
            palabras_disponibles.append(palabra)

    if len(palabras_disponibles) == 0:
        print("Ya usaste todas las palabras de esta categoría")
        break

    palabra = random.choice(palabras_disponibles)
    palabras_usadas.append(palabra)

    letras_adivinadas = []
    attempts = 6
    puntaje = 0

    print("¡Bienvenido al Ahorcado!")
    print()

    while attempts > 0:
        progress = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                progress += letra + " "
            else:
                progress += "_ "
        print(progress)

        if "_" not in progress:
            print("¡Ganaste!")
            puntaje += 6
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: ", letras_adivinadas)

        letra = input("Ingresá una letra: ")

        if len(letra) != 1 or not letra.isalpha():
            print("Entrada no valida")
            continue

        if letra in letras_adivinadas:
            print("Ya usaste esa letra.")
        elif letra in palabra: 
            letras_adivinadas.append(letra)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            letras_adivinadas.append(letra)
            attempts -= 1
            puntaje -= 1 
            print ("Incorrecto")

    if attempts == 0:
        print("Perdiste. La palabra era: ", palabra)
        puntaje = 0

    print("Puntaje: ", puntaje)

    seguir = input("Queres jugar otra ronda? (s/n):")
    if seguir != "s":
        break