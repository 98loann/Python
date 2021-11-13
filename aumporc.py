# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


sal = float(input("Qual o seu salario atual? "))
porc = float(input("Qual a porcentagem de aumento? "))

novoSalario = sal + ((sal*porc)/100)
aumento = novoSalario - sal

print ("Novo salário: R$", novoSalario)
print ("Aumento de: R$", aumento)