'''Faça uma função chamada acima_da_media que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram
acima da média.'''



def maiores(n_inteiro,n):
    '''A função  retorna outra lista, que contenha todos os números da
       lista original maiores que n, ordenados em ordem crescente'''
    if n not in n_inteiro:
        n_inteiro.append(n)
    n_inteiro.sort()
    indice= list.index(n_inteiro, n)
    return n_inteiro[indice+1:]

def acima_da_media(n):
    '''A função retorna uma lista ordenada com as notas que ficaram
       acima da média.'''
    w= sum(n)/len(n)
    p= maiores(n,w)
    return p
