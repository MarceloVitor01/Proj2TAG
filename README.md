# Projeto de Emparelhamento Máximo Estável

Este projeto implementa um algoritmo de emparelhamento máximo estável para a alocação de alunos a projetos acadêmicos, seguindo os critérios e requisitos definidos.

## Descrição

O programa lê um arquivo de entrada `entradaProj2TAG.txt`, que contém informações sobre projetos disponíveis, número de vagas, requisitos de notas e preferências dos alunos.

O algoritmo implementado realiza iterações de emparelhamento em um loop, exibindo os resultados e as trocas realizadas até a alocação final. O objetivo é maximizar a quantidade de alunos alocados em projetos, levando em consideração as preferências dos alunos e as vagas disponíveis em cada projeto.

## Arquivos do Projeto

- `tratamento_dados.py`: Módulo para o tratamento dos dados de entrada.
- `emparelhamento_estavel.py`: Módulo que realiza os emparelhamentos.
- `Projeto2_TAG.py`: Módulo principal que executa o algoritmo com iterações de emparelhamento.
- `entradaProj2TAG.txt`: Arquivo de entrada contendo os dados dos projetos e alunos.
- `README.md`: Este arquivo, fornecendo informações sobre o projeto.

## Como Executar

Certifique-se de ter o Python instalado em seu ambiente.

1. Clone o repositório para sua máquina local.
2. Certifique-se de ter o arquivo `entradaProj2TAG.txt` na mesma pasta do código.
3. Execute o arquivo `Projeto2_TAG.py`.

#Para Windows:
```bash
python Projeto2_TAG.py

#Para macOS e Linux:
```bash
python3 Projeto2_TAG.py