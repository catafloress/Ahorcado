import random 

categorias = {"Programacion": ["python","programa", "variable","funcion", "bucle"],
"Matematicas": ["entero", "fraccion", "decimal", "factorial", "suma"],
"Lenguaje": ["cadena", " palabra", "oracion", "letra", "texto"]}

print("Categorias disponibles:")
for i, cat in enumerate(categorias.keys(), start=1):
        print(f"{i}.{cat}")

while True:
    eleccion = input("Elegi una categoria(numero): ")
    if eleccion.isdigit() and 1 <= int(eleccion) <= len(categorias):
        nombre_categoria = list(categorias.keys())[int(eleccion)-1]
        break
    else:
        print("Entrada no valida. Ingresa el numero de la categoria")

palabras_disponibles = categorias[nombre_categoria]

palabras_a_jugar = random.sample(palabras_disponibles, len(palabras_disponibles))
puntaje_total = 0

print(f"\n Bienvenido al Ahorcado! Categoria: {nombre_categoria}\n")

for palabra in palabras_a_jugar:
    letras_adivinadas = []
    intentos = 6
    puntaje_palabra = 0

    while intentos > 0:
        progreso = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                progreso += letra + " "
            else: 
                progreso += "_ "
        print(progreso)

        if "_" not in progreso:
            print("Ganaste")
            puntaje_palabra += 6 
            break
        print(f"Intentos restantes: {intentos}")
        print(f"Letras usadas: {', '.join(letras_adivinadas)}")

        letra = input("Ingresá una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Entrada no válida.\n")
            continue

        if letra in letras_adivinadas:
            print("Ya usaste esa letra.\n")
        elif letra in palabra:
            letras_adivinadas.append(letra)
            print("¡Bien! Esa letra está en la palabra.\n")
        else:
            letras_adivinadas.append(letra)
            intentos -= 1
            puntaje_palabra -= 1  # cada letra incorrecta resta 1 punto
            print("Esa letra no está en la palabra.\n")

    else:  # Si se termina el while sin adivinar
        print(f"¡Perdiste! La palabra era: {palabra}")
        puntaje_palabra = 0

    puntaje_total += puntaje_palabra
    print(f"Puntaje actual: {puntaje_total}\n{'-'*30}\n")

print(f"Juego terminado. Puntaje total: {puntaje_total}")
        