segundos = int(input("Ingrese la cantidad de segundos: " ))

horas = segundos // 3600
resto = segundos % 3600

minutos = resto // 60 
segundos_final = resto % 60 

print("Horas: ", horas)
print("Minutos: ", minutos)
print("Segundos: ", segundos_final)