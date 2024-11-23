# EXPERIMENTO ATLAS - Reconstrução de sinal - Método do Filtro Ótimo Otimizado Sem a Restrição do Pedestal (Optimal Filtering - OF1 Otimizado).
# Autor: Guilherme Barroso Morett.
# Data: 18 de novembro de 2024.

# Objetivo do código: implementação da validação cruzada K-Fold para o método OF1 otimizado para a análise de como o valor mínimo da amplitude influencia na estimação da fase.

""" 
Organização do código:

Importação de arquivos.
Método OF1 otimizado para a estimação da amplitude, fase ou pedestal: metodo_OF1_otimizado.py

Funções presentes:

1) Instrução para salvar em arquivos os dados estatísticos pela validação cruzada k-Fold para a estimação da fase.
Entrada: número de ocupação, número do janelamento ideal para a amplitude estimada, média do dado estatístico, variância do dado estatístico, desvio padrão do dado estatístico da fase, quantidade de elementos presentes no vetor do erro de estimação, valor mínimo da amplitude, tipo de fase e o dado estatístico.
Saída: nada.

2) Instrução da validação cruzada K-Fold para a análise de como o valor da amplitude mínima adotado influencia no processo de estimação da fase.
Entrada: número de ocupação, número de janelamento ideal para a amplitude estimada, matriz com os pulsos de sinais janelado, vetor da fase de referência janelado, valor mínimo da amplitude e o vetor da amplitude de referência janelado (somente para a fase estimada por meio da amplitude de referência).
Saída: nada.

3) Instrução principal. 
Entrada: nada.
Saída: nada.
"""

# Importação de bibliotecas.
import numpy as np
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
titulo_programa = colored("Geração de arquivos de saída pela técnica de validação cruzada K-Fold para a análise do processo de estimação da fase pelo método Optimal Filtering (OF1 Otimizado):\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### --- 1) INSTRUÇÃO PARA A IMPRESSÃO DOS DADOS ESTATÍSTICOS DO ERRO DE ESTIMAÇÃO DA FASE EM UM ARQUIVO DE SAÍDA PELO MÉTODO OF1 OTIMIZADO --- ###

# Definição da instrução para a impressão em um arquivo de saída, os dados estatísticos do erro de estimação da fase pelo método OF1 otimizado.
def arquivo_saida_dados_estatisticos_erro_estimacao_fase_OF1_otimizado(n_ocupacao, n_janelamento_ideal_amplitude_estimada, media_erro_estimacao_fase, var_erro_estimacao_fase, desvio_padrao_erro_estimacao_fase, tamanho_vetor_estimacao_fase, valor_minimo_amplitude_estimada_processo_fase, tipo_fase, dado_estatistico):

    # Definição do título presente no arquivo de saída.
    titulo_arquivo_saida = f"valor_minimo_amplitude,media_erro,var_erro,desvio_padrao_erro,tamanho_vetor_estimacao\n"

    # Definição da pasta que contém o arquivo de saída.
    pasta_saida = f"K_Fold_{tipo_fase}_{dado_estatistico}_J_{n_janelamento_ideal_amplitude_estimada}"

    # Caso a pasta não exista.
    if not os.path.exists(pasta_saida):
        
        # Criação da pasta de saída.
        os.makedirs(pasta_saida)

    # Nome do arquivo de saida.
    arquivo_saida = f"k_fold_{tipo_fase}_{dado_estatistico}_OC_{n_ocupacao}.txt"

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
            arquivo_saida_dados_estatisticos.write(f"{valor_minimo_amplitude_estimada_processo_fase},{media_erro_estimacao_fase},{var_erro_estimacao_fase},{desvio_padrao_erro_estimacao_fase},{tamanho_vetor_estimacao_fase}\n")
        
    # Excessão.
    except Exception as e:
        
        # Impressão de mensagem de alerta.
        print("Ocorreu um erro ao atualizar o arquivo de saída dos dados estatísticos:", str(e))

### --------------------------------------------------------------------------------------------------------------------------------- ###

### ----------------- 2) INSTRUÇÃO PARA A VALIDAÇÃO CRUZADA K-FOLD PARA A FASE PELO MÉTODO OF1 OTIMIZADO ---------------------------- ###

# Definição da instrução da técnica de validação cruzada K-Fold para a fase pelo método OF1 otimizado.
def K_fold_OF1_otimizado_analise_fase(parametro, n_ocupacao, n_janelamento_ideal_amplitude_estimada, Matriz_Pulsos_Sinais_Janelado, vetor_fase_referencia_janelado, valor_minimo_amplitude_estimada_processo_fase, tipo_fase, vetor_amplitude_referencia_janelado):
    
    # Criação da lista vazia blocos_pulsos_sinais.
    blocos_pulsos_sinais = []

    # Criação da lista vazia blocos_fase_referencia.
    blocos_fase_referencia = []
    
    # Criação da lista vazia blocos_amplitude_referencia.
    blocos_amplitude_referencia = []

    # Criação da variável quantidade_blocos que armazena a quantidade de blocos.
    quantidade_blocos = 100

    # Definição da quantidade de elementos de cada bloco.
    quantidade_elementos_bloco = len(Matriz_Pulsos_Sinais_Janelado) // quantidade_blocos
    
    # Para i de início em zero até a quantidade de elementos de amostras com incremento igual a quantidade_elementos_bloco.
    for i in range(0, len(Matriz_Pulsos_Sinais_Janelado), quantidade_elementos_bloco):
    
        # Definição do bloco de pulsos de sinais.
        bloco_pulsos_sinais = Matriz_Pulsos_Sinais_Janelado[i:i+quantidade_elementos_bloco]
        # O bloco dos pulsos de sinais é acrescentado a lista dos blocos dos pulsos de sinais.
        blocos_pulsos_sinais.append(bloco_pulsos_sinais)
    
        # Definição do bloco dos dados da fase de referência.
        bloco_parametro_referencia = vetor_fase_referencia_janelado[i:i+quantidade_elementos_bloco]
        # O bloco da fase de referência é acrescentado a lista dos blocos das fases de referência.
        blocos_fase_referencia.append(bloco_parametro_referencia)
        
        # Caso a variável vetor_amplitude_referencia_janelado não é igual a None.
        if vetor_amplitude_referencia_janelado is not None:
        
            # Definição do bloco dos dados da amplitude de referência.
            bloco_amplitude_referencia = vetor_amplitude_referencia_janelado[i:i+quantidade_elementos_bloco]
            # O bloco da amplitude de referência é acrescentado a lista dos blocos das amplitudes de referência.
            blocos_amplitude_referencia.append(bloco_amplitude_referencia)
    
    # Definição da lista vazia lista_bloco_media_erro_estimacao_fase.
    lista_blocos_media_erro_estimacao_fase = []
    
    # Definição da lista vazia lista_bloco_var_erro_estimacao_fase.
    lista_blocos_var_erro_estimacao_fase = []
    
    # Definição da lista vazia lista_bloco_DP_erro_estimacao_fase.
    lista_blocos_DP_erro_estimacao_fase = []
    
    # Definição da lista vazia lista_tamanho_blocos_erro_estimacao_fase
    lista_tamanho_blocos_erro_estimacao_fase = []
     
    # Para indice_bloco de zero até o tamanho da matriz de dados de entrada com incremento igual a quantidade de elementos no bloco.
    for indice_teste in range(0, len(blocos_pulsos_sinais)):
        
        # Definição do bloco_teste_pulsos_sinais como sendo aquele de índice igual ao indice_teste.
        bloco_teste_pulsos_sinais = blocos_pulsos_sinais[indice_teste]
        
        # Definição do bloco_treino_pulsos_sinais como sendo aqueles de índices diferentes do indice_teste.
        bloco_treino_pulsos_sinais = blocos_pulsos_sinais[:indice_teste]+blocos_pulsos_sinais[indice_teste+1:]
        
        # Reescreve os elementos bloco_treino_pulsos_sinais em sequência, uma lista unidimensional.
        bloco_treino_pulsos_sinais = [elemento for sublista in bloco_treino_pulsos_sinais for elemento in sublista]
        
        # Definição do bloco_teste_fase_referencia como sendo aquele de índice igual ao indice_teste.
        bloco_teste_fase_referencia = blocos_fase_referencia[indice_teste]
        
        # Definição do bloco_treino_fase_referencia como sendo aqueles de índices diferentes do indice_teste.
        bloco_treino_fase_referencia = blocos_fase_referencia[:indice_teste]+blocos_fase_referencia[indice_teste+1:]
        
        # Reescreve os elementos bloco_treino_fase_referencia em sequência, uma lista unidimensional.
        bloco_treino_fase_referencia = [elemento for sublista in bloco_treino_fase_referencia for elemento in sublista]
        
        # A variável bloco_treino_amplitude_referencia recebe o valor inicial de None.
        bloco_treino_amplitude_referencia = None
        
        # Caso a variável vetor_amplitude_referencia_janelado não é igual a None.
        if vetor_amplitude_referencia_janelado is not None:
        
            # Definição do bloco_treino_amplitude_referencia como sendo aqueles de índices diferentes do indice_teste.
            bloco_treino_amplitude_referencia = blocos_amplitude_referencia[:indice_teste]+blocos_amplitude_referencia[indice_teste+1:]
        
            # Reescreve os elementos bloco_treino_amplitude_referencia em sequência, uma lista unidimensional.
            bloco_treino_amplitude_referencia = [elemento for sublista in bloco_treino_amplitude_referencia for elemento in sublista]
        
        # A variável bloco_lista_erro_estimacao_fase recebe o valor de retorno da função metodo_OF1_simples.
        bloco_lista_erro_estimacao_fase = metodo_OF1_otimizado(parametro, n_janelamento_ideal_amplitude_estimada, bloco_treino_pulsos_sinais, bloco_teste_pulsos_sinais, bloco_teste_fase_referencia, valor_minimo_amplitude_estimada_processo_fase, bloco_treino_amplitude_referencia)

        # Cálculo dos dados estatísticos de cada bloco.
        bloco_media_erro_estimacao_fase = np.mean(bloco_lista_erro_estimacao_fase)
        bloco_var_erro_estimacao_fase = np.var(bloco_lista_erro_estimacao_fase)
        bloco_DP_erro_estimacao_fase = np.std(bloco_lista_erro_estimacao_fase)
        bloco_tamanho_erro_estimacao_fase = len(bloco_lista_erro_estimacao_fase)
        
        # Adiciona essas informações em suas respectivas listas.    
        lista_blocos_media_erro_estimacao_fase.append(bloco_media_erro_estimacao_fase)
        lista_blocos_var_erro_estimacao_fase.append(bloco_var_erro_estimacao_fase)
        lista_blocos_DP_erro_estimacao_fase.append(bloco_DP_erro_estimacao_fase)
        lista_tamanho_blocos_erro_estimacao_fase.append(bloco_tamanho_erro_estimacao_fase)
        
    # Cálculo da média do tamanho de cada bloco de estimação da fase.
    media_tamanho_blocos_erro_estimacao_fase = np.mean(lista_tamanho_blocos_erro_estimacao_fase)
        
    # Cálculo dos dados estatísticos da média.
    media_media_blocos_erro_estimacao_fase = np.mean(lista_blocos_media_erro_estimacao_fase)
    var_media_blocos_erro_estimacao_fase = np.var(lista_blocos_media_erro_estimacao_fase)
    DP_media_blocos_erro_estimacao_fase = np.std(lista_blocos_media_erro_estimacao_fase)
    
    # Salva a informação dos dados estatísticos da média do erro de estimação do fase em seus respectivos arquivos de saída.
    arquivo_saida_dados_estatisticos_erro_estimacao_fase_OF1_otimizado(n_ocupacao, n_janelamento_ideal_amplitude_estimada, media_media_blocos_erro_estimacao_fase, var_media_blocos_erro_estimacao_fase, DP_media_blocos_erro_estimacao_fase, media_tamanho_blocos_erro_estimacao_fase, valor_minimo_amplitude_estimada_processo_fase, tipo_fase, dado_estatistico = "media")
    
    # Cálculo dos dados estatísticos da variância.
    media_var_blocos_erro_estimacao_fase = np.mean(lista_blocos_var_erro_estimacao_fase)
    var_var_blocos_erro_estimacao_fase = np.var(lista_blocos_var_erro_estimacao_fase)
    DP_var_blocos_erro_estimacao_fase = np.std(lista_blocos_var_erro_estimacao_fase)
    
    # Salva a informação dos dados estatísticos da variância do erro de estimação do fase em seus respectivos arquivos de saída.
    arquivo_saida_dados_estatisticos_erro_estimacao_fase_OF1_otimizado(n_ocupacao, n_janelamento_ideal_amplitude_estimada, media_var_blocos_erro_estimacao_fase, var_var_blocos_erro_estimacao_fase, DP_var_blocos_erro_estimacao_fase, media_tamanho_blocos_erro_estimacao_fase, valor_minimo_amplitude_estimada_processo_fase, tipo_fase, dado_estatistico = "var")
    
    # Cálculo dos dados estatísticos do desvio padrão.
    media_DP_blocos_erro_estimacao_fase = np.mean(lista_blocos_DP_erro_estimacao_fase)
    var_DP_blocos_erro_estimacao_fase = np.var(lista_blocos_DP_erro_estimacao_fase)
    DP_DP_blocos_erro_estimacao_fase = np.std(lista_blocos_DP_erro_estimacao_fase)
    
    # Salva a informação dos dados estatísticos do desvio padrão do erro de estimação do fase em seus respectivos arquivos de saída.
    arquivo_saida_dados_estatisticos_erro_estimacao_fase_OF1_otimizado(n_ocupacao, n_janelamento_ideal_amplitude_estimada, media_DP_blocos_erro_estimacao_fase, var_DP_blocos_erro_estimacao_fase, DP_DP_blocos_erro_estimacao_fase, media_tamanho_blocos_erro_estimacao_fase, valor_minimo_amplitude_estimada_processo_fase, tipo_fase, dado_estatistico = "DP")
    
### --------------------------------------------------------------------------------------------------------------------------------- ### 

### ---------------------------------------------- 3) INSTRUÇÃO PRINCIPAL DO CÓDIGO ------------------------------------------------- ###
  
# Definição da instrução principal do código.
def principal_K_fold_analise_fase_OF1_otimizado():
    
    # A variável n_janelamento_ideal_amplitude_estimada recebe o valor ideal para a amplitude estimada obtido pela análise gráfica do K-Fold.
    n_janelamento_ideal_amplitude_estimada = int(input("Digite o número do janelamento ideal para o parâmetro estimado desejado: "))
    
    # A variável ocupacao_inicial armazena o valor inicial da ocupação que é 10.
    # Obs.: ao considerar um valor mínimo para a amplitude, a estimação da fase para a ocupação 0 fica impossibilitada.
    ocupacao_inicial = 10
    
    # A variável ocupacao_final armazena o valor final da ocupação que é 100.
    ocupacao_final = 100
    
    # A variável incremento_ocupacao armazena o valor de incremento entre as ocupações.
    incremento_ocupacao = 10
    
    # Lista de valores mínimos considerados para a amplitude.
    lista_valores_minimos_amplitude = [1, 4.5, 10, 25, 50, 75, 100]
    
    # A variável tipo_opcao_fase armazena a escolha digitada pelo usuário para o processo de estimação da fase.
    tipo_opcao_fase = int(input("Opções para a análise do processo de estimação da fase:\nAmplitude estimada: 1\nAmplitude de referência: 2\nDigite a opção desejada:"))
    
    # A variável valores_tipo_opcao_fase é uma lista com os valores aceitáveis para o o tipo de processo de estimação da fase.
    valores_tipos_opcoes_fase = [1, 2]

    # Caso o valor digitado armazenado na variável tipo_opcao_fase não estiver presente na lista valores_tipos_opcoes_fase.
    if tipo_opcao_fase not in valores_tipos_opcoes_fase:
    
        # Exibição de uma mensagem de alerta de que a opção solicitada é inválida.
        print("Essa opção é inválida!")
        print("------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
        
    # Se a variável tipo_opcao_fase for igual a 1.
    if tipo_opcao_fase == 1:
        
        # A variável tipo_fase recebe a string "fase_analise_amplitude_minima_estimada".
        tipo_fase = "fase_analise_amplitude_minima_estimada"
        
        # A variável parametro recebe a string "fase_amplitude_estimada".
        parametro = "fase_amplitude_estimada"
        
    # Se a variável tipo_fase for igual a 2.
    elif tipo_opcao_fase == 2:
        
        # A variável tipo_fase recebe a string "fase_analise_amplitude_minima_referencia"
        tipo_fase = "fase_analise_amplitude_minima_referencia"
        
        # A variável parametro recebe a string "fase_amplitude_referencia".
        parametro = "fase_amplitude_referencia"
    
    # Para o número de ocupações de 0 até 100 com incremento de 10. 
    for n_ocupacao in tqdm(range(ocupacao_inicial, ocupacao_final+1, incremento_ocupacao)):
    
        # Para o elemento valor_minimo_amplitude_processo_fase na lista lista_valores_minimos_amplitude.
        for valor_minimo_amplitude_processo_fase in tqdm(lista_valores_minimos_amplitude):
    
            # Chamada ordenada das funções.
    
            Matriz_Dados_OC = leitura_dados_ocupacao(n_ocupacao)
            
            Matriz_Dados_OC_Sem_Pedestal = retirada_pedestal(Matriz_Dados_OC)
            
            vetor_amostras_pulsos, vetor_amplitude_referencia, vetor_fase_referencia = amostras_pulsos_e_referencia(Matriz_Dados_OC_Sem_Pedestal)
            
            Matriz_Pulsos_Sinais_Fase_Janelado, vetor_fase_referencia_janelado = amostras_janelamento(vetor_amostras_pulsos, vetor_fase_referencia, n_janelamento_ideal_amplitude_estimada)
            
            Matriz_Pulsos_Sinais_Amplitude_Janelado, vetor_amplitude_referencia_janelado = amostras_janelamento(vetor_amostras_pulsos, vetor_amplitude_referencia, n_janelamento_ideal_amplitude_estimada)
            
            # Caso a variável tipo_opcao_fase seja igual a 1.
            if tipo_opcao_fase == 1:
                
                vetor_amplitude_referencia_janelado = None
            
                K_fold_OF1_otimizado_analise_fase(parametro, n_ocupacao, n_janelamento_ideal_amplitude_estimada, Matriz_Pulsos_Sinais_Fase_Janelado, vetor_fase_referencia_janelado, valor_minimo_amplitude_processo_fase, tipo_fase, vetor_amplitude_referencia_janelado)
            
            # Caso a variável tipo_opcao_fase seja igual a 2.
            elif tipo_opcao_fase == 2:
                
                K_fold_OF1_otimizado_analise_fase(parametro, n_ocupacao, n_janelamento_ideal_amplitude_estimada, Matriz_Pulsos_Sinais_Fase_Janelado, vetor_fase_referencia_janelado, valor_minimo_amplitude_processo_fase, tipo_fase, vetor_amplitude_referencia_janelado)
                
# Chamada da instrução principal do código.
principal_K_fold_analise_fase_OF1_otimizado()    
   
### --------------------------------------------------------------------------------------------------------------------------------- ###

# Impressão de uma linha que representa o fim do programa.

print("\n----------------------------------------------------------------------------------------------------------------------------\n")
