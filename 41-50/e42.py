# Lucas dos Santos Siqueira
# 42 - Crie um dicionário de alunos e suas notas (em uma lista). Exemplo: {'João': [8.5, 9.0], 'Maria': [7.0, 6.5]}. Use um laço for para calcular a média de cada aluno e imprimir o resultado.

students={
    "Lucas" : [8.5, 4.9, 5],
    "Eduarda" : [8.8, 9.6, 9.8],
    "Dalton" : [9.7, 10],
    "Bruna" : [7.2, 8.4, 2],
    "Paulo" : [5.1, 2.0],
}

print("\nEstudantes com suas respectivas médias:\n")
for student in students: # percorrendo cada estudante do dicionário de estudantes 
    total = 0 # variável que acumulará as notas
    count = 0 # variável que conta quantas notas cada estudante tem
    for grade in students[student]: # percorre cada nota de cada estudante do dicionário de estudantes
        total += grade # acumula as notas somando
        count += 1 # conta a quantidade de notas no boletim de cada estudante
    media = total / count # realiza o calculo da média
    print(f"Nome: {student} : {media:.2f}")
# Lucas dos Santos Siqueira