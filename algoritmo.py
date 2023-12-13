def emparelhamento_estavel(alunos, projetos):
    alunos_disponiveis = list(alunos.keys())

    while alunos_disponiveis:
        aluno = alunos_disponiveis.pop(0) #Pegar o próximo aluno disponível
        preferencias_aluno = alunos[aluno]['preferencias']

        for projeto_preferido in preferencias_aluno:
            projeto = projetos[projeto_preferido]

            if len(projeto['alunos']) < len(projeto['vagas']):
                   #Adicionar aluno ao projeto se houver vaga disponível
                   projeto['alunos'].append(aluno)
                   break
            
            else:
                #Verificar se a nota do aluno é melhor do que a de algum aluno no projeto
                for aluno_existente in projeto['alunos']:
                    if alunos[aluno]['nota'] > alunos[aluno_existente]['nota']:
                        projeto['alunos'].remove(aluno_existente)
                        alunos_disponiveis.append(aluno_existente) #Aluno removido volta pra lista de alunos disponíveis

                        projeto['alunos'].append(aluno)
                        break

    return projetos