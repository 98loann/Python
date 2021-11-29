# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


print("faça já seu cadastro:")
usuario=str(input("usuário--> "))
senha=str(input("senha-->"))
while usuario==senha:
	print("ERRO: o usuário não pode ser igual a senha, tente novamente")
	usuario=str(input("usuário--> "))
	senha=str(input("senha-->"))
else:
	print("cadastrado efetuado com sucesso")