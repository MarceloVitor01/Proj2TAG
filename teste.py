def gale_shapley(homens, mulheres, preferencias_homens, preferencias_mulheres):
    homem_para_mulher = {}
    mulher_para_homem = {}
    homens_livres = list(homens)
    
    while homens_livres:
        homem = homens_livres.pop(0)
        preferencias_homem = preferencias_homens[homem]
        
        for mulher in preferencias_homem:
            namorado_atual = mulher_para_homem.get(mulher)
            
            if namorado_atual is None:
                homem_para_mulher[homem] = mulher
                mulher_para_homem[mulher] = homem
                break
            else:
                preferencias_mulher = preferencias_mulheres[mulher]
                if preferencias_mulher.index(namorado_atual) > preferencias_mulher.index(homem):
                    homem_para_mulher[homem] = mulher
                    mulher_para_homem[mulher] = homem
                    homens_livres.append(namorado_atual)
                    break
    
    return homem_para_mulher


# Exemplo de uso
homens = ['H1', 'H2', 'H3']
mulheres = ['M1', 'M2', 'M3']
preferencias_homens = {
    'H1': ['M1', 'M2', 'M3'],
    'H2': ['M1', 'M3', 'M2'],
    'H3': ['M3', 'M1', 'M2']
}
preferencias_mulheres = {
    'M1': ['H2', 'H1', 'H3'],
    'M2': ['H1', 'H3', 'H2'],
    'M3': ['H1', 'H2', 'H3']
}

matches = gale_shapley(homens, mulheres, preferencias_homens, preferencias_mulheres)
print("Casais formados:")
for homem, mulher in matches.items():
    print(f"{homem} e {mulher}")
