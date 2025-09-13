# Feito por Flávio Luis

#  Crie uma lista de 10 números. Use um laço for para imprimir a tabuada de cada 
# número.



numerosParaTabuada = list(range(1, 11)) 

for numero in numerosParaTabuada:
 
    print(f"--- Tabuada do {numero} ---")
    
    for multiplicador in range(1, 11):
        
        resultado = numero * multiplicador
        
        print(f"{numero} x {multiplicador} = {resultado}")
        
  