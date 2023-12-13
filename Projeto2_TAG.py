from tratamento_dados import  tratar_projetos, tratar_alunos
from algoritmo import emparelhamento_estavel

entrada_dados = open('entradaProj2TAG.txt', '+r', encoding = 'utf-8').readlines()
entrada_projetos = entrada_dados[3:53]
entrada_alunos = entrada_dados[56:259]

projetos = tratar_projetos(entrada_projetos)
alunos = tratar_alunos(entrada_alunos)

tratar_alunos(alunos)