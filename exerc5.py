# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
primeiro = int(input("Primeiro numero: "))
segundo = int(input("Segundo numero : "))
terceiro = int(input("Terceiro numero: "))

maior = primeiro

if (segundo > maior):
        maior = segundo
if (terceiro > maior):
        maior = terceiro

print("Maior: ",maior)

menor = primeiro

if (segundo < menor):
        menor = segundo
if (terceiro < menor):
        menor = terceiro
print("Menor: ",menor)