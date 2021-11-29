# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

A = 80000
B = 200000
taxaA = 0.03
taxaB = 0.015

anos = 0
while A < B:
    A = A + (A * taxaA)
    B = B + (B * taxaB)
    anos = anos + 1

print ("Serao necessarios " + str(anos) + " anos para que a populacao do pais A ultrapasse ou iguale a populacao do pais B")