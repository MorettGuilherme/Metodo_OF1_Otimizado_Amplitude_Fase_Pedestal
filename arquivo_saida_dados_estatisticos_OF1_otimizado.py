# EXPERIMENTO ATLAS - Reconstrução de sinal - Método do Filtro Ótimo Otimizado Sem a Restrição do Pedestal (Optimal Filtering - OF1 Otimizado).
# Autor: Guilherme Barroso Morett.
# Data: 18 novembro de 2024.

# Objetivo do código: geração de arquivos de saída baseados nos dados estatísticos dos histogramas do erro de estimação da amplitude, fase ou pedestal pelo método OF1 otimizado.

""" 
Organização do Código:

Importação de arquivos.
Método OF1 otimizado para a estimação da amplitude, fase ou pedestal: metodo_OF1_otimizado.py

Funções presentes:

1) Função para o cálculo dos dados estatísticos do erro de estimação pelo método OF1 otimizado.
Entrada: lista com o erro de estimação para a amplitude, fase ou pedestal.
Saída: a média, a variância e o desvio padrão do erro de estimação para a amplitude, fase ou pedestal.

2) Instrução para salvar os dados estatísticos do erro de estimação da amplitude, fase ou pedestal para determinada ocupação em um arquivo de saída pelo método OF1 otimizado.
Entrada: parâmetro, número de ocupação, número de janelamento, a média, a variância e o desvio padrão do erro de estimação para a amplitude, fase ou pedestal.
Saída: nada.

3) Instrução principal do código.
Entrada: nada.
Saída: nada.
"""

# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import os
from tqdm import tqdm
import time
from termcolor import colored

# Importação dos arquivos.
from metodo_OF1_otimizado import * 

# Impressão de uma linha que representa o início do programa.
print("\n----------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Geração de arquivos de saída baseados nos dados estatísticos dos histogramas do erro de estimação da amplitude, fase, ou pedestal pelo método Optimal Filtering (OF1 Otimizado):\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### --- 1) FUNÇÃO PARA O CÁLCULO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO DA AMPLITUDE, FASE OU PEDESTAL PELO MÉTODO OF1 OTIMIZADO --- ###

# Definição da função para o cálculo dos dados estatísticos do erro de estimação da amplitude, fase ou pedestal pelo método OF1 otimizado.
def dados_estatisticos_erro_estimacao_parametro_OF1_otimizado(lista_erro_estimacao_parametro):
    
    # A lista do erro de estimação da amplitude, fase ou pedestal é convertida para o tipo numpy array.
    vetor_erro_estimacao_parametro = np.array(lista_erro_estimacao_parametro)

    # Cálculo da média do erro de estimação da amplitude, fase ou pedestal.
    media_erro_estimacao_parametro = np.mean(vetor_erro_estimacao_parametro)

    # Cálculo da variância do erro de estimação da amplitude, fase ou pedestal.
    var_erro_estimacao_parametro = np.var(vetor_erro_estimacao_parametro)

    # Cálculo do desvio padrão do erro de estimação da amplitude, fase ou pedestal.
    desvio_padrao_erro_estimacao_parametro = np.std(vetor_erro_estimacao_parametro)
    
    # A função retorna a média, a variância e o desvio padrão dos dados do erro de estimação da amplitude, fase ou pedestal.
    return media_erro_estimacao_parametro, var_erro_estimacao_parametro, desvio_padrao_erro_estimacao_parametro
    
### --------------------------------------------------------------------------------------------------------------------------------- ###

### --- 2) INSTRUÇÃO PARA A IMPRESSÃO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO DA AMPLITUDE, FASE OU PEDESTAL EM UM ARQUIVO DE SAÍDA PELO MÉTODO OF1 OTIMIZADO --- ###

# Definição da instrução para a impressão em um arquivo de saída, os dados estatísticos do erro de estimação do parâmetro pelo método OF1 otimizado.
def arquivo_saida_dados_estatisticos_erro_estimacao_parametro_OF1_otimizado(parametro, n_ocupacao, n_janelamento, media_erro_estimacao_parametro, var_erro_estimacao_parametro, desvio_padrao_erro_estimacao_parametro):

    # Definição do título presente no arquivo de saída.
    titulo_arquivo_saida = "Oc,media_erro,var_erro,desvio_padrao_erro\n"

    # Definição da pasta em que contém o arquivo de saída.
    pasta_saida = f"Dados_Estatisticos_OF1_Otimizado_{parametro}_OC"

    # Caso a pasta não exista.
    if not os.path.exists(pasta_saida):
        # Criação da pasta de saída.
        os.makedirs(pasta_saida)

    # Nome do arquivo de saida.
    arquivo_saida = f"dados_estatisticos_OF1_otimizado_{parametro}_janelamento_{n_janelamento}.txt"

    # Caminho completo para o arquivo de saída.
    caminho_arquivo_saida = os.path.join(pasta_saida, arquivo_saida)

    # Comando para tentar realizar uma operação.
    try:
        
        # Abre o arquivo presente no endereço caminho_arquivo_saida como a variável arquivo_saida_dados_estatisticos no modo leitura.
        with open(caminho_arquivo_saida, 'r') as arquivo_saida_dados_estatisticos:
            
            # A variável primeiro_caractere recebe o primeiro elemento presente no arquivo_saida_dados_estatisticos.
            primeiro_caractere = arquivo_saida_dados_estatisticos.read(1)
            
            # Caso não haja nada na variável primeiro_caractere.
            if not primeiro_caractere:
                
                # Abre o arquivo presente no endereço caminho_arquivo_saida como file no modo acrescentar.
                with open(caminho_arquivo_saida, 'a') as file:
                    
                    # Escreve o título no arquivo file.
                    file.write(titulo_arquivo_saida)
                    
    # Excessão de erro ao encontrar o arquivo no caminho fornecido.                
    except FileNotFoundError:
        
        # Abre o arquivo presente no endereço caminho_arquivo_saida como file no modo escrita.
        with open(caminho_arquivo_saida, 'w') as file:
            
            # Escreve o título no arquivo file.
            file.write(titulo_arquivo_saida)

    # Comando para tentar realizar uma operação.
    try:
        
        # Abre o arquivo presente no endereço caminho_arquivo_saida como arquivo_saida_dados_estatisticos no modo acrescentar.
        with open(caminho_arquivo_saida, "a") as arquivo_saida_dados_estatisticos:
            
            # Escrita dos dados de interesse no arquivo_saida_dados_estatisticos.
            arquivo_saida_dados_estatisticos.write(f"{n_ocupacao},{media_erro_estimacao_parametro},{var_erro_estimacao_parametro},{desvio_padrao_erro_estimacao_parametro}\n")
        
    # Excessão.
    except Exception as e:
        
        # Impressão de mensagem de alerta.
        print("Ocorreu um erro ao atualizar o arquivo de saída dos dados estatísticos:", str(e))

### --------------------------------------------------------------------------------------------------------------------------------- ###

### ----------------------------------- 3) INSTRUÇÃO PRINCIPAL DO CÓDIGO ------------------------------------------------------------ ###

# Definição da instrução principal do código.
def principal_arquivo_saida_dados_estatisticos_OF1_otimizado():
    
    # A variável valor_pedestal_referencia armazena a quantidade de referência do pedestal.
    valor_pedestal_referencia = 30
    
    # A variável valor_minimo_amplitude_processo_fase recebe o valor mínimo para a amplitude que é de cerca de 4,5 ADC Count (três vezes o valor do desvio padrão do ruído eletrônico).
    valor_minimo_amplitude_processo_fase = 4.5
    
    # A variável ocupacao_inicial armazena o valor inicial da ocupação que é 0.
    ocupacao_inicial = 0
    
    # A variável ocupacao_final armazena o valor final da ocupação que é 100.
    ocupacao_final = 100
    
    # A variável incremento_ocupacao armazena o valor de incremento entre as ocupações.
    incremento_ocupacao = 10
    
    # A variável n_janelamento_inicial armazena o valor inicial do janelamento que é 7.
    n_janelamento_inicial = 7
    
    # A variável n_janelamento_final armazena o valor final do janelamento que é 19.
    n_janelamento_final = 19
    
    # A variável incremento_janelamento armazena o valor do incremento entre os janelamentos.
    incremento_janelamento = 2
    
    # A variável parametro_amplitude recebe a string "amplitude".
    parametro_amplitude = "amplitude"
    
    # A variável parametro_fase_amplitude_estimada recebe a string "fase_amplitude_estimada".
    parametro_fase_amplitude_estimada = "fase_amplitude_estimada"
    
    # A variável parametro_fase_amplitude_referencia recebe a string "fase_amplitude_referencia".
    parametro_fase_amplitude_referencia = "fase_amplitude_referencia"
    
    # A variável parametro_pedestal recebe a string "pedestal".
    parametro_pedestal = "pedestal"
    
    # Para o número de janelamento inicial de 7 até 19 com incremento de 2.
    for n_janelamento in tqdm(range(n_janelamento_inicial, n_janelamento_final+1, incremento_janelamento)):
    
        # Para o número de ocupação inicial de 0 até 100 com incremento de 10.
        for n_ocupacao in tqdm(range(ocupacao_inicial, ocupacao_final+1, incremento_ocupacao)):
    
            # Chamada ordenada das funções.
    
            Matriz_Dados_OC = leitura_dados_ocupacao(n_ocupacao)
            
            Matriz_Dados_OC_Sem_Pedestal = retirada_pedestal(Matriz_Dados_OC)
    
            vetor_amostras_pulsos, vetor_amplitude_referencia, vetor_fase_referencia = amostras_pulsos_e_referencia(Matriz_Dados_OC_Sem_Pedestal)
            
            Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento)
            Matriz_Pulsos_Sinais_Janelado, vetor_fase_referencia_janelado = amostras_janelamento(vetor_amostras_pulsos, vetor_fase_referencia, n_janelamento)
            vetor_pedestal_referencia_janelado = valor_pedestal_referencia*np.ones(len(Matriz_Dados_OC)-n_janelamento+1)
            
            Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_amplitude_referencia_treino_janelado, vetor_amplitude_referencia_teste_janelado = dados_treino_teste_histograma(Matriz_Pulsos_Sinais_Janelado, vetor_amplitude_referencia_janelado)
            Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_fase_referencia_treino_janelado, vetor_fase_referencia_teste_janelado = dados_treino_teste_histograma(Matriz_Pulsos_Sinais_Janelado, vetor_fase_referencia_janelado)
            Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_pedestal_referencia_treino_janelado, vetor_pedestal_referencia_teste_janelado = dados_treino_teste_histograma(Matriz_Pulsos_Sinais_Janelado, vetor_pedestal_referencia_janelado)
    
            lista_erro_estimacao_amplitude = metodo_OF1_otimizado(parametro_amplitude, n_janelamento, Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_amplitude_referencia_teste_janelado, valor_minimo_amplitude_processo_fase = None, vetor_amplitude_referencia_treino_janelado = None)
            lista_erro_estimacao_fase_amplitude_estimada = metodo_OF1_otimizado(parametro_fase_amplitude_estimada, n_janelamento, Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_fase_referencia_teste_janelado, valor_minimo_amplitude_processo_fase, vetor_amplitude_referencia_treino_janelado = None)
            lista_erro_estimacao_fase_amplitude_referencia = metodo_OF1_otimizado(parametro_fase_amplitude_referencia, n_janelamento, Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_fase_referencia_teste_janelado, valor_minimo_amplitude_processo_fase, vetor_amplitude_referencia_treino_janelado)
            lista_erro_estimacao_pedestal = metodo_OF1_otimizado(parametro_pedestal, n_janelamento, Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_pedestal_referencia_teste_janelado, valor_minimo_amplitude_processo_fase = None, vetor_amplitude_referencia_treino_janelado = None)
            
            media_erro_estimacao_amplitude, var_erro_estimacao_amplitude, desvio_padrao_erro_estimacao_amplitude = dados_estatisticos_erro_estimacao_parametro_OF1_otimizado(lista_erro_estimacao_amplitude)
            media_erro_estimacao_fase_amplitude_estimada, var_erro_estimacao_fase_amplitude_estimada, desvio_padrao_erro_estimacao_fase_amplitude_estimada = dados_estatisticos_erro_estimacao_parametro_OF1_otimizado(lista_erro_estimacao_fase_amplitude_estimada)
            media_erro_estimacao_fase_amplitude_referencia, var_erro_estimacao_fase_amplitude_referencia, desvio_padrao_erro_estimacao_fase_amplitude_referencia = dados_estatisticos_erro_estimacao_parametro_OF1_otimizado(lista_erro_estimacao_fase_amplitude_referencia)
            media_erro_estimacao_pedestal, var_erro_estimacao_pedestal, desvio_padrao_erro_estimacao_pedestal = dados_estatisticos_erro_estimacao_parametro_OF1_otimizado(lista_erro_estimacao_pedestal)
    
            arquivo_saida_dados_estatisticos_erro_estimacao_parametro_OF1_otimizado(parametro_amplitude, n_ocupacao, n_janelamento, media_erro_estimacao_amplitude, var_erro_estimacao_amplitude, desvio_padrao_erro_estimacao_amplitude)
            arquivo_saida_dados_estatisticos_erro_estimacao_parametro_OF1_otimizado(parametro_fase_amplitude_estimada, n_ocupacao, n_janelamento, media_erro_estimacao_fase_amplitude_estimada, var_erro_estimacao_fase_amplitude_estimada, desvio_padrao_erro_estimacao_fase_amplitude_estimada)
            arquivo_saida_dados_estatisticos_erro_estimacao_parametro_OF1_otimizado(parametro_fase_amplitude_referencia, n_ocupacao, n_janelamento, media_erro_estimacao_fase_amplitude_referencia, var_erro_estimacao_fase_amplitude_referencia, desvio_padrao_erro_estimacao_fase_amplitude_referencia)
            arquivo_saida_dados_estatisticos_erro_estimacao_parametro_OF1_otimizado(parametro_pedestal, n_ocupacao, n_janelamento, media_erro_estimacao_pedestal, var_erro_estimacao_pedestal, desvio_padrao_erro_estimacao_pedestal)

# Chamada da instrução principal do código.
principal_arquivo_saida_dados_estatisticos_OF1_otimizado()

### --------------------------------------------------------------------------------------------------------------------------------- ###

# Impressão de uma linha que representa o fim do programa.
print("\n----------------------------------------------------------------------------------------------------------------------------\n")   


            
            