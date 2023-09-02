# PUCPR - Bacharelado em Ciência da Computação
# Disciplina - Resolução de Problemas de Natureza Discreta
# Autores do código: Diogo C. Guimarães, Hiann W. Padilha e Marcos P. Ruppel - turma 2U (Noite)
# Atividade somativa - Avaliação 1 - Operações em conjuntos
# Versão 1.0.0

from funcoes import *

# Lista de nomes de arquivos
nomes_arquivos = ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']

# Loop sobre os arquivos
for nome_arquivo in nomes_arquivos:
    print(f'Resultados para {nome_arquivo}:\n')

    # Ler o arquivo de entrada
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    # Converter as linhas do arquivo em operações
    num_operacoes = int(linhas[0])
    linhas = [linha.strip() for linha in linhas[1:]]
    operacoes = []

    for i in range(0, len(linhas), 3):
        operacao = linhas[i]
        conjunto1 = linhas[i + 1].split(', ')
        conjunto2 = linhas[i + 2].split(', ')
        operacoes.append((operacao, conjunto1, conjunto2))

    # Executar as operações
    for operacao, conjunto1, conjunto2 in operacoes:
        if operacao == 'U':
            resultado = uniao(conjunto1, conjunto2)
            nome_operacao = 'União'
        elif operacao == 'I':
            resultado = intersecao(conjunto1, conjunto2)
            nome_operacao = 'Interseção'
        elif operacao == 'D':
            resultado = diferenca(conjunto1, conjunto2)
            nome_operacao = 'Diferença'
        elif operacao == 'C':
            resultado = produto_cartesiano(conjunto1, conjunto2)
            nome_operacao = 'Produto Cartesiano'

        # Exibir o resultado da operação
        print(f'{nome_operacao}: Conjunto 1: [{", ".join(conjunto1)}], Conjunto 2: [{", ".join(conjunto2)}]. Resultado: {resultado}')

    print('\n')
