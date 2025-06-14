import json
import genero

dados = {}
livros = []

while True:
    dados['Título'] = str(input('Nome do livro: '))
    print('--'*15)
    dados['Autor'] = str(input('Nome do autor: '))
    print('--'*15)
    print('Qual genero do livro? ')

    for i, gen in enumerate(genero.genero()):
        print(f'{i} - {gen}')
    
    gen = int(input('>>> '))
    print('--'*15)
    dados['Gênero'] = genero.genero()[gen]
    
    dados['Páginas'] = int(input('Quantidade de páginas: '))
    print('--'*15)
    dados['Status'] = str(input('Status: [LENDO, PAUSADO, CONCLUÍDO, ABANDONADO]: ')).upper()

    livros.append(dados.copy())
    dados.clear()

    op = input('Continuar? [S/N] ').strip().lower()
    if op == 'n':
        break

#--- Salvar os dados em JSON ---

with open('livros.json', 'w', encoding='utf-8') as arquivo:
    json.dump(livros, arquivo, ensure_ascii=False, indent=1)

print('\nDados foram salvos com sucesso no arquivo "livros.json"')

"""
# Impressão formatada
print(f'\n{"Título":<30} {"Autor":<20} {"Gênero":<15} {"Páginas":<8} {"Status":<12}')
print('-' * 90)

for livro in livros:
    print(f'{livro["Título"]:<30} {livro["Autor"]:<20} {livro["Gênero"]:<15} {livro["Páginas"]:<8} {livro["Status"]:<12}')

"""