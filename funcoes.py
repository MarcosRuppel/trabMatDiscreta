# Função para realizar a operação de união
def uniao(conjunto1, conjunto2):
    return list(set(conjunto1 + conjunto2))


# Função para realizar a operação de interseção
def intersecao(conjunto1, conjunto2):
    return list(set(conjunto1) & set(conjunto2))


# Função para realizar a operação de diferença
def diferenca(conjunto1, conjunto2):
    resultado = list(set(conjunto1) - set(conjunto2))
    resultado += list(set(conjunto2) - set(conjunto1))
    return resultado


# Função para realizar a operação de produto cartesiano
def produto_cartesiano(conjunto1, conjunto2):
    resultado = []
    for elem1 in conjunto1:
        for elem2 in conjunto2:
            resultado.append((elem1, elem2))
    return resultado
