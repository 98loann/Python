# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


preco = float(input("Qual o valor da mercadoria? "))
porc = float(input("Qual a porcentagem de desconto? "))

porc= porc /100
desconto = preco * porc
desconto_total = preco - desconto

print("O valor descontado sera de R$ ",desconto)
print("O valor final da compra sera de R$ ", desconto_total)
