# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


km=float(input("Quantos KM foram percorridos com o carro? "))
dias=int(input("Por quantos dias o carro ficou alugado? "))

dias_tot= dias*60
km_tot=km*0.15

print("O total a pagar sera de ", dias_tot+km_tot)
