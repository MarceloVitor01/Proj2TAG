#Módulo principal

#Importação dos módulos necessários
from tratamento_dados import  tratar_projetos, tratar_alunos
from emparelhamento_estavel import emparelhamento_estavel
import random

#Realiza a leitura do arquivo 'entradaProj2TAG.txt'
entrada_dados = open('entradaProj2TAG.txt', '+r', encoding = 'utf-8').readlines()

#Os dados referentes aos projetos iniciam-se na linha 4, porém subtraímos 1, visto que a contagem em Python começa em 0
entrada_projetos = entrada_dados[3:53]

#Os dados referentes aos alunos iniciam-se na linha 57, porém subtraímos 1, visto que a contagem em Python começa em 0
entrada_alunos = entrada_dados[56:259]

#Chama a função responsável por tratar os dados dos projetos
projetos = tratar_projetos(entrada_projetos)

#Chama a função responsável por tratar os dados dos alunos
alunos = tratar_alunos(entrada_alunos)


melhor_emparelhamento = None
maior_numero_alunos = 0

# Execute o emparelhamento estável com os alunos embaralhados em cada iteração
for i in range(10):
    print(f"{'-' * 50}\nIteração {i + 1}:")
    
    #Troca a ordem dos alunos a cada iteração
    chaves_embaralhadas = list(alunos.keys())
    random.shuffle(chaves_embaralhadas)
    #Cria um novo dicionário de alunos com as chaves embaralhadas
    alunos_novo = {chave: alunos[chave] for chave in chaves_embaralhadas}
    
    #Recebe o emparelhamento e as trocas do algoritmo
    emparelhamento, trocas = emparelhamento_estavel(alunos_novo, projetos)
    
    #Calcula a quantidade de alunos alocados
    numero_alunos_alocados = sum(len(projeto['alunos']) for projeto in emparelhamento.values() if projeto['alunos'])
    
    print(f"\nEmparelhamentos na iteração {i + 1}:")
    for projeto, alunos_alocados in emparelhamento.items():
        #Mostra os emparelhamentos realizados na iteração
        print(f"Emparelhamento: {projeto} - {alunos_alocados['alunos']}")

    print(f"\nTrocas na iteração {i + 1}:")
    for troca in trocas:
        #Mostra as trocas realizadas na iteração
        print(troca)
    
    print(f"\nTotal de alunos alocados na iteração {i + 1}: {numero_alunos_alocados}")
    
    if numero_alunos_alocados > maior_numero_alunos:
        #Verifica qual é o maior emparelhamento e sua quantidade de alunos alocados
        melhor_emparelhamento = emparelhamento
        maior_numero_alunos = numero_alunos_alocados

print(f"{'-' * 50}\nMaior Emparelhamento Encontrado:")
for projeto, alunos_alocados in melhor_emparelhamento.items():
    #Mostra os emparelhamentos do maior emparelhamento encontrado
    print(f"Emparelhamento: {projeto} - {alunos_alocados['alunos']}")

#Mostra o tamanho do maior emparelhamento
print(f"\nTamanho do maior emparelhamento: {maior_numero_alunos} alunos")