# Lucas dos Santos Siqueira
# 40 -  Crie um dicionário com 5 nomes de frutas e suas cores. Use um laço  for para adicionar uma nova fruta com sua cor. 

fruits={
    "Tomate" : "Vermelho",
    "Banana" : "Amarela",
    "Uva" : "Roxa",
    "Laranja" : "Laranja",
    "Limão" : "Verde"
}

print("\nFrutas:\n")
for data in fruits:
    print(f"{data} : {fruits[data]}")

new_fruit = input("Digite um nome para adicionar uma nova fruta.")
new_color = input("Digite uma cor para a nova fruta adicionada.")
fruits[new_fruit] = new_color

print("\nFrutas Atualizadas:\n")
for data in fruits:
    print(f"{data} : {fruits[data]}")
# Lucas dos Santos Siqueira