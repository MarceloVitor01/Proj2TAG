#Módulo que realiza o tratamento dos dados presentes no arquivo: 'entradaProj2TAG.txt'

def tratar_alunos(entrada_alunos):
    #Dicionário que representa os alunos no formato: codigo_aluno: {'preferencias': [], 'nota': X}
    alunos = {}
    
    for aluno in entrada_alunos:
        #Remove os caracteres inúteis para o algoritmo
        aluno = aluno.replace('(', '').replace(')', '').replace('\n', '').replace(', ', ',')
        
        #Divide os dados em codigo_aluno e dados_aluno
        codigo_aluno, dados_aluno = aluno.split(':')

        #Divide os dados em preferências e nota
        preferencias, nota = dados_aluno.split(' ')

        #Converte a nota em inteiro
        nota = int(nota)

        #Lista as preferências
        preferencias = preferencias.split(',')

        #Popula o dicionário com as informações correspondentes ao aluno
        alunos[codigo_aluno] = {'preferencias': preferencias, 'nota': nota}

    #Retorna o dicionário de alunos
    return alunos

def tratar_projetos(entrada_projetos):
    #Dicionário que representa os projetos no formato: codigo_projeto: {'vagas': X, 'nota': Y, 'alunos': []}
    projetos = {}

    for projeto in entrada_projetos:
        #Remove os caracteres inúteis para o algoritmo
        projeto = projeto.replace('(', '').replace(')', '').replace('\n', '').replace(' ', '')
        
        #Divide os dados em codigo_projeto, mumero_vagas e nota
        codigo_projeto, numero_vagas, nota = projeto.split(',')

        #Converte o numero de vagas e a nota em inteiros
        numero_vagas = int(numero_vagas)
        nota = int(nota)

        #Popula o dicionário com as informações correspondentes ao projeto
        projetos[codigo_projeto] = {'vagas': numero_vagas, 'nota': nota, 'alunos': []}

    #Retorna o dicionário de projetos
    return projetos