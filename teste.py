def tratar_projetos(entrada_projetos):
    projetos = {}

    for projeto in entrada_projetos:
        projeto = projeto.replace('(', '').replace(')', '').replace(', ', ',').replace('\n', '')

        codigo, numero_vagas, requisito = projeto.split(',')

        projetos[codigo] = {
            'vagas': int(numero_vagas),
            'requisito': int(requisito),
            'alunos_atribuidos': [],
            'preferencias_alunos': [],
            'preferencias_atuais': []
        }

    return projetos

def tratar_alunos(entrada_alunos):
    alunos = {}

    for aluno in entrada_alunos:
        aluno = aluno.replace('(', '').replace(')', '').replace(', ', ',').replace('\n', '').replace(' ', ',')

        codigo_aluno, dados = aluno.split(':')

        preferencias = dados.split(',')
        nota = int(preferencias.pop(-1))
        
        alunos[codigo_aluno] = {
            'preferencias': preferencias,
            'nota': nota,
            'projeto_atribuido': None
        }

    return alunos

def algoritmo_gale_shapley(projetos, alunos):
    for projeto in projetos:
        projetos[projeto]['preferencias_alunos'] = list(alunos.keys())

    while True:
        alguem_aceito = False

        for aluno, info_aluno in alunos.items():
            if info_aluno['projeto_atribuido'] is None and len(info_aluno['preferencias']) > 0:
                projeto_preferido = info_aluno['preferencias'][0]

                if alunos[aluno]['nota'] >= projetos[projeto_preferido]['requisito']:
                    projetos[projeto_preferido]['preferencias_atuais'].append(aluno)

                    if len(projetos[projeto_preferido]['alunos_atribuidos']) < projetos[projeto_preferido]['vagas']:
                        projetos[projeto_preferido]['alunos_atribuidos'].append(aluno)
                        alunos[aluno]['projeto_atribuido'] = projeto_preferido
                        del alunos[aluno]['preferencias'][0]
                        alguem_aceito = True
                    else:
                        alunos_existentes = projetos[projeto_preferido]['alunos_atribuidos']
                        aluno_troca = projetos[projeto_preferido]['preferencias_atuais'].index(aluno)
                        for aluno_existente in alunos_existentes:
                            if projetos[projeto_preferido]['preferencias_atuais'].index(aluno_existente) > aluno_troca:
                                alunos[aluno_existente]['projeto_atribuido'] = None
                                projetos[projeto_preferido]['alunos_atribuidos'].remove(aluno_existente)
                                projetos[projeto_preferido]['alunos_atribuidos'].append(aluno)
                                alunos[aluno]['projeto_atribuido'] = projeto_preferido
                                del alunos[aluno]['preferencias'][0]
                                alguem_aceito = True
                                break

        if not alguem_aceito:
            break

# Lendo o arquivo 'entradaProj2TAG.txt'
with open('entradaProj2TAG.txt', 'r') as file:
    linhas = file.readlines()
    entrada_projetos = linhas[3:53]
    entrada_alunos = linhas[56:259]

# Tratando os dados de entrada
projetos = tratar_projetos(entrada_projetos)
alunos = tratar_alunos(entrada_alunos)

# Chamada da função principal
algoritmo_gale_shapley(projetos, alunos)

# Exibindo os resultados
for projeto, info_projeto in projetos.items():
    print(f"Projeto {projeto}: {info_projeto['alunos_atribuidos']}")
