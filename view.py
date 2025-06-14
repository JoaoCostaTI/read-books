import json

with open('livros.json', 'r', encoding='utf-8') as arquivo:
    livros = json.load(arquivo)

# Impressão formatada
print(f'\n{"Título":<30} {"Autor":<20} {"Gênero":<15} {"Páginas":<8} {"Status":<12}')
print('-' * 90)

for livro in livros:
    print(f'{livro["Título"]:<30} {livro["Autor"]:<20} {livro["Gênero"]:<15} {livro["Páginas"]:<8} {livro["Status"]:<12}')