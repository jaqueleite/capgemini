import math

def questao1(lista):
    lista.sort()
    return lista[len(lista) // 2]


def questao2(lista, intervalo):
    memo = []
    for i in range(1, len(lista)):
        pont = lista[i]
        for j in range(len(lista)):
            if lista[j] - pont == intervalo or pont - lista[j] == intervalo:
                l = [lista[j], pont]
                l.sort()
                if l not in memo:
                    memo.append(l)
    return len(memo)

def questao3(texto):
    texto = texto.replace(' ', '')
    text_len = math.ceil(math.sqrt(len(texto)))

    grid = []

    for i in range(text_len):
        grid.append('')
    
    counter = 0
    for letra in texto:
        grid[counter] = grid[counter] + letra
        counter += 1
        if counter > text_len - 1:
            counter = 0

    return ' '.join(grid)

