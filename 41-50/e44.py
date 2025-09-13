# Lucas dos Santos Siqueira
# 44 - Crie  uma  lista  de  dicionários,  onde  cada  dicionário  representa  um  livro  com titulo e autor. Use um laço for para imprimir o título de todos os livros do autor 'Machado de Assis'.

books=[
  {
      "autor": "Timothy Zahn",
      "nome": "Heir to the Empire"
  },
  {
      "autor": "Timothy Zahn",
      "nome": "Dark Force Rising"
  },
  {
      "autor": "Timothy Zahn",
      "nome": "The Last Command"
  },
  {
      "autor": "James Luceno",
      "nome": "Darth Plagueis"
  },
  {
      "autor": "Claudia Gray",
      "nome": "Bloodline"
  },
  {
      "autor": "Claudia Gray",
      "nome": "Lost Stars"
  },
  {
      "autor": "Chuck Wendig",
      "nome": "Aftermath"
  },
  {
      "autor": "Chuck Wendig",
      "nome": "Life Debt"
  },
  {
      "autor": "Chuck Wendig",
      "nome": "Empire’s End"
  },
  {
      "autor": "Alexander Freed",
      "nome": "Shadow Fall"
  },
  {
    "autor": "Machado de Assis",
    "nome": "Dom Casmurro"
  },
  {
    "autor": "Machado de Assis",
    "nome": "Memórias Póstumas de Brás Cubas"
  },
  {
    "autor": "Machado de Assis",
    "nome": "Quincas Borba"
  },
  {
    "autor": "Machado de Assis",
    "nome": "O Alienista"
  },
  {
    "autor": "Machado de Assis",
    "nome": "Esaú e Jacó"
  },
]

print(f"\nLivros de Machado de Assis\n")
for book in books:
    if book["autor"].lower() == "machado de assis":
        print(f"{book["nome"]}")

# Lucas dos Santos Siqueira