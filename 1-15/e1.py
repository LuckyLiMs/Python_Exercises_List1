# 1- Crie uma lista com 5 nomes de cidades e use um laço for para imprimir cada nome.
cities = ["Cachoeira", "Canas", "Lorena", "Guaratinguetá", "Aparecida"]

def impress(cities):
    for city in cities:
        print(f"{city}\n")

print(f"Nomes de 5 cidades da região do Vale do Paraíba: \n")
impress(cities)