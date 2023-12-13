#Módulo que realiza os emparelhamentos

def emparelhamento_estavel(alunos, projetos):
    #Cria uma lista inicial com todos os alunos
    alunos_disponiveis = list(alunos.keys())
    #Cria uma lista das trocas realizadas
    trocas_realizadas = []

    #Percorre a lista de alunos disponíveis
    while alunos_disponiveis:
        #Pega o próximo aluno disponível
        aluno = alunos_disponiveis.pop(0)

        #Armazena as preferências do aluno
        preferencias_aluno = alunos[aluno]['preferencias']

        #Percorre cada projeto presente nas preferências do aluno
        for projeto_preferido in preferencias_aluno:
            projeto = projetos[projeto_preferido]

            #Verifica se a quantidade de vagas já foi preenchida
            if len(projeto['alunos']) < projeto['vagas']:
                if aluno not in projeto['alunos'] and alunos[aluno]['nota'] >= projeto['nota']:
                    #Adiciona o aluno ao projeto se houver vaga disponível e a nota for suficiente
                    projeto['alunos'].append(aluno)
                    break
            
            else:
                #Percorre todos os alunos do projeto
                for aluno_existente in projeto['alunos']:
                    #Verifica se a nota do aluno é maior do que a de algum outro aluno no projeto
                    if alunos[aluno]['nota'] > alunos[aluno_existente]['nota'] and aluno not in projeto['alunos']:
                        #Se sim, remove o aluno de menor nota
                        projeto['alunos'].remove(aluno_existente)
                        #O aluno removido volta pra lista de alunos disponíveis
                        alunos_disponiveis.append(aluno_existente)

                        #Adiciona o aluno de maior nota ao projeto
                        projeto['alunos'].append(aluno)

                        #Formata a informação da troca
                        troca_realizada = f'No projeto {projeto_preferido}, {aluno_existente} saiu e {aluno} entrou'

                        #Adiciona a troca realizada na lista
                        trocas_realizadas.append(troca_realizada)

                        break

    #Retorna o emparelhamento e as trocas realizadas
    return projetos, trocas_realizadas