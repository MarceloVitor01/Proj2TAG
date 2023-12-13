'''Módulo para tratamento dos dados'''

def tratar_alunos(entrada_alunos):
    #Estrutura para representar os alunos
    alunos = {}
    
    for aluno in entrada_alunos:
        aluno = aluno.replace('(', '').replace(')', '').replace('\n', '').replace(', ', ',')
        
        codigo_aluno, dados_aluno = aluno.split(':')

        preferencias = dados_aluno.split(' ')

        nota = int(preferencias.pop(-1))

        print(preferencias)

        alunos[codigo_aluno] = {'preferencias': preferencias, 'nota': nota}

    return alunos

def tratar_projetos(entrada_projetos):
    #Estrutura para representar os projetos
    projetos = {}

    for projeto in entrada_projetos:
        projeto = projeto.replace('(', '').replace(')', '').replace('\n', '').replace(' ', '')
        
        codigo_projeto, numero_vagas, nota = projeto.split(',')

        numero_vagas = int(numero_vagas)
        nota = int(nota)

        projetos[codigo_projeto] = {'vagas': numero_vagas, 'nota': nota, 'alunos': []}

    return projetos