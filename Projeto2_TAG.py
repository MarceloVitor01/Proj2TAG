import pandas as pd
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

def tratar_projetos(entrada_projetos):
    projetos = {}

    for projeto in entrada_projetos:
        projeto = projeto.replace('(', '').replace(')', '').replace(', ', ',').replace('\n', '')

        codigo, numero_vagas, requisito = projeto.split(',')

        projetos[codigo] = (int(numero_vagas), int(requisito))

    return projetos

def tratar_alunos(entrada_alunos):
    alunos = {}

    for aluno in entrada_alunos:
        aluno = aluno.replace('(', '').replace(')', '').replace(', ', ',').replace('\n', '').replace(' ', ',')

        codigo_aluno, dados = aluno.split(':')

        preferencias = dados.split(',')
        nota = int(preferencias.pop(-1))
        
        alunos[codigo_aluno] = (preferencias, nota)

    return alunos

def geraGrafo(entrada_alunos,entrada_projetos):
    Grafo = nx.Graph()
    for projeto,especificacoes in entrada_projetos.items():
        Grafo.add_node(projeto, vagas = especificacoes[0], 
                        nota = especificacoes[1], bipartite=0)

    for aluno,atributos in entrada_alunos.items():
        Grafo.add_node(aluno, vagas = 0, 
                        nota = atributos[1], bipartite=1)
        
        notaAluno = atributos[1]
        for projetoInteresse in atributos[0]:
            if notaAluno >= Grafo.nodes[projetoInteresse]["nota"]:
                Grafo.add_edge(aluno,projetoInteresse)
    
    return Grafo

def visualizacao(grafo, titulo):
    posicao = nx.spring_layout(grafo, seed=123)

    plt.figure(figsize=(8,8))

    nx.draw_networkx_nodes(grafo, posicao, node_size=80, node_color='red')
    nx.draw_networkx_edges(grafo, posicao, alpha=0.5)
    nx.draw_networkx_labels(grafo, posicao, font_color='black')

    plt.title(titulo)

    plt.show()


# Lógica para ler o arquivo e utilizar as funções acima
entrada = open('entradaProj2TAG.txt', '+r').readlines()
entrada_projetos = entrada[3:53]
entrada_alunos = entrada[56:259]

projetos = tratar_projetos(entrada_projetos)
alunos = tratar_alunos(entrada_alunos)

Grafo = geraGrafo(alunos, projetos)

visualizacao(Grafo, 'TESTE')