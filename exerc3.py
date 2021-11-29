# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


pesoLimite = 50
peso = float(input("Digite a quantidade de kgs de peixe que Joao trouxe: "))
if peso > pesoLimite:
    excesso = peso - pesoLimite
    multa = excesso * 4.00
    print ("Multa foi de " + str(multa) + " reais")
else:
        print("Nao ultrapassou o limite")
