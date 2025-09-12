# Lucas dos Santos Siqueira
# 39 -  Crie um dicionário com 5 nomes de países e suas capitais. Use um laço for para encontrar e imprimir a capital do país 'Brasil'.

countries={
    "Canadá" : "Ottawa",
    "Estados Unidos" : "Washington, D.C.",
    "Japão" : "Tóquio",
    "Brasil" : "Brasília",
    "China" : "Pequim"
}

for data in countries:
    if data.lower() == "brasil":
        print(f"\nA capital do Brasil é: {countries[data]}")
# Lucas dos Santos Siqueira