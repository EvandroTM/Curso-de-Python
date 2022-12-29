import os

# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'C:\\Users\\evand\\OneDrive\\Documentos\\GitHub\\Curso-de-Python\\Aulas\\'
caminho_arquivo += 'aula116.txt'
# print(caminho_arquivo)


# arquivo  = open(caminho_arquivo, 'w')
#
# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     print(type(arquivo))
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('Lendo...')
#     print()
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print()
#     print('READLINES')
#     for linha in arquivo.readlines():
#         print(linha.strip())
#         print()
   

# print('-=-' * 5)
# print()

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())


#     # print('Olá mundo')
#     # print('Arquivo vai ser fechado')


###################### a VAI ADICIONAR ################
# with open(caminho_arquivo, 'a+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )


################### b MODO BINARIO ###################
# with open(caminho_arquivo, 'b') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )

with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# os.unlink(caminho_arquivo) # remove o arquivo
# os.remove(caminho_arquivo) # remove o arquivo
# os.rename(caminho_arquivo, 'aula116-2.txt') # renomeia ou move o arquivo