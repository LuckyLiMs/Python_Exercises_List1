# Lucas dos Santos Siqueira
# 37 - Use um laço for para verificar se o valor 'Python' existe em algum valor de um dicionário, onde as chaves são nomes de cursos e os valores são as linguagens usadas.

courses={
    "Ciência da Computação" : "Python",
    "Engenharia de Software" : "Java",
    "Análise e Desenvolvimento de Sistemas" : "C#",
    "Sistemas para Internet" : "JavaScript",
    "Engenharia da Computação" : "C/C++",
}

for data in courses:
    if courses[data].lower() == "python":
        print(f"Existe Python em: \n{data} : {courses[data]}")
# Lucas dos Santos Siqueira