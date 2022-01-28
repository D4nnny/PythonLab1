payasos = int(input("Ingrese la cantidad de payasos vendidos: "))
muñecas = int(input("Ingrese la cantidad de muñecas vendidas: "))
total = payasos + muñecas
peso_pay = payasos*112
peso_mu = muñecas*75


suma = peso_pay + peso_mu
print("Cantidad total de juguetes:", total)
print("El peso total del paquete es de: ", suma,"g")
