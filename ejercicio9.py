from functools import total_ordering


inver = float(input("Ingrese una cantidad para empezar a invertir: "))
inte = float(input("De cuanto desea el interes anual: "))
periodo = int(input("Cuanto tiempo desea hacer la inversion en años: "))

total = str (((inver * inte/100))*periodo)
print("El total de intereses generados en ", periodo, "años es de: ", total)