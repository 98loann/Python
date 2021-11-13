# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


cigar=int(input("Ola fumante, quantos cigarros voce fuma por dia? "))
anos=int(input("A quanto tempo voce fuma? "))

reducao= anos*365 * cigar * 10

reducao_tot=reducao/(24*60)

print("Voce ja perdeu %.2f"% reducao_tot," dias de vida")