# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from calendar import isleap

ano = int(input("Digite o ano: "))
if isleap(ano):
    print('É bissexto')
else:
    print('Não é bissexto')
