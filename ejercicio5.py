total = 0 

while True:
    precio = float(input("Ingrese el precio del producto(0 para terminar):"))

    if precio == 0: 
        break
    total = total + precio

print("Total a pagar:", total)
