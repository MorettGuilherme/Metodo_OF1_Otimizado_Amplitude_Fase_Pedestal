# EXPERIMENTO ATLAS - Reconstrução de sinal - Método do Filtro Ótimo Otimizado (Optimal Filtering - OF2 Otimizado).
# Autor: Guilherme Barroso Morett.
# Data: 03 de setembro de 2024.

# Objetivo do código: construção do gráfico da validação cruzada K-Fold para o método OF2 otimizado para a estimação da amplitude, fase ou pedestal.

""" 
Organização do código:

Funções presentes:

1) Função para a leitura dos dados estatísticos da validação cruzada K-Fold.
Entrada: número de ocupação.
Saída: matriz com os dados da ocupação organizados de acordo com a coluna (número do janelamento, média, variância e desvio padrão do dado estatístico)

2) Instrução para a construção do gráfico tipo A da validação cruzada K-Fold.
Obs.: esse gráfico mostra a média do dado estatístico (média, variância e desvio padrão do erro de estimação da amplitude, fase ou pedestal) com as barras de erro para cada um dos janelamentos ao decorrer das ocupações.
Entrada: matriz com os dados da ocupação organizados.
Saída: nada.

3) Instrução para a construção do gráfico tipo B da validação cruzada K-Fold.
Obs.: esse gráfico mostra a média do dado estatístico (média, variância e desvio padrão do erro de estimação da amplitude, fase ou pedestal) com as barras de erro para cada uma das ocupações ao decorrer do janelamento.
Entrada: matriz com os dados da ocupação organizados.
Saída: nada.

4) Instrução principal (main) do código.
Entrada: nada.
Saída: nada.
"""

# Importação de bibliotecas.
import numpy as np
import os
import matplotlib.pyplot as plt
from termcolor import colored

# Impressão de uma linha que representa o início do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Plote do gráfico da validação cruzada K-Fold para o método Optimal Filtering (OF2 Otimizado) para a estimação da amplitude, fase ou pedestal:\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### ----------------- 1) FUNÇÃO PARA A LEITURA DOS DADOS ESTATÍSTICOS DA VALIDAÇÃO CRUZADA K-FOLD PELO MÉTODO OF2 OTIMIZADO -------------------- ###

# Definição da função para a leitura dos dados estatísticos do K-Fold pelo método OF2 otimizado.
def leitura_dados_estatisticos_k_fold_OF2_otimizado(parametro, n_ocupacao, dado_estatistico):
    
    # Nome da pasta em que se encontra o arquivo de entrada dos dados estatísticos do K-Fold.
    pasta_dados_k_fold = f"K_Fold_{parametro}_{dado_estatistico}_Dados_Estatisticos_OF2_Otimizado_OC"

    # Nome do arquivo de entrada dos dados estatísticos do K-Fold.
    arquivo_dados_k_fold = f"k_fold_{parametro}_{dado_estatistico}_dados_estatisticos_OF2_otimizado_OC_{n_ocupacao}.txt"

    # O caminho para esse arquivo de entrada dos dados estatísticos do K-Fold.
    caminho_arquivo_dados_k_fold = os.path.join(pasta_dados_k_fold, arquivo_dados_k_fold)

    # Caso o caminho especificado exista.
    if os.path.exists(caminho_arquivo_dados_k_fold):
    
        # Abre o aquivo de entrada no modo leitura.
        with open(caminho_arquivo_dados_k_fold,"r") as arquivo_entrada_ocupacoes:
        
            # Armazena os dados na variável Matriz_Dados_K_Fold.
            Matriz_Dados_K_Fold = np.array(np.loadtxt(arquivo_entrada_ocupacoes, skiprows = 1, dtype = 'double', delimiter = ','))
 
    # Caso contrário.       
    else:
    
        # Impressão de mensagem que o arquivo de entrada não existe.
        print(f"O arquivo {arquivo_dados_k_fold} não existe na pasta {pasta_dados_k_fold}.")

    # Obs.: da forma que o programa está escrito, os arquivos de entrada devem estar na mesma pasta em que está o código do programa.
    # Caso deseja-se alterar isso basta mudar o endereço do arquivo.
    
    # A função retorna a matriz Matriz_Dados_K_Fold.
    return Matriz_Dados_K_Fold

### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ----------------- 2) INSTRUÇÃO PARA A CONSTRUÇÃO DO GRÁFICO DO TIPO A DA VALIDAÇÃO CRUZADA K-FOLD PELO MÉTODO OF2 OTIMIZADO ---------------- ###

# Definição da instrução para a construção do gráfico tipo A pela validação cruzada K-Fold para o método OF2 otimizado.
def grafico_A_k_fold_OF2_otimizado(parametro, opcao, Matriz_Dados_K_Fold_OC_0, Matriz_Dados_K_Fold_OC_10, Matriz_Dados_K_Fold_OC_20, Matriz_Dados_K_Fold_OC_30, Matriz_Dados_K_Fold_OC_40, Matriz_Dados_K_Fold_OC_50, Matriz_Dados_K_Fold_OC_60, Matriz_Dados_K_Fold_OC_70, Matriz_Dados_K_Fold_OC_80, Matriz_Dados_K_Fold_OC_90, Matriz_Dados_K_Fold_OC_100):
    
    # Definição da variável indice_coluna_janelamento que armazena o índice da coluna do janelamento.
    indice_coluna_janelamento = 0
    
    # Definição da variável indice_coluna_media que armazena o índice da coluna das médias do dado estatístico.
    indice_coluna_medias = 1
    
    # Definição da variável indice_coluna_DP que armazena o índice da coluna dos desvios padrão do dado estatístico.
    indice_coluna_DP = 3
    
    # Definição do vetor do eixo das abscissas.
    janelamento = Matriz_Dados_K_Fold_OC_0[:, indice_coluna_janelamento]
    
    # Nomeação do eixo das abscissas.
    plt.xlabel("Quantidade de janelamento", fontsize = 18)
    
    # Comando para o tamanho dos números do eixo das abscissas.
    plt.xticks(fontsize = 16)
    
    # Comando para o tamanho dos números do eixo das ordenadas.
    plt.yticks(fontsize = 16)
    
    # Caso opcao seja 1:
    if opcao == 1:
        
        # Caso a variável parametro seja a igual a "fase_amplitude_estimada" ou "fase_amplitude_referencia".
        if parametro == "fase_amplitude_estimada" or parametro == "fase_amplitude_referencia":
            
            # Comando para o nome do eixo das ordenadas.
            plt.ylabel(f"Média pelo K-Fold do erro de estimação (ns)", fontsize = 18)
         
        # Caso contrário.   
        else:
            
            # Comando para o nome do eixo das ordenadas.
            plt.ylabel(f"Média pelo K-Fold do erro de estimação (ADC Count)", fontsize = 18)
        
    # Caso opcao seja 2.
    elif opcao == 2:
        
        # Caso a variável parametro seja a igual a "fase_amplitude_estimada" ou "fase_amplitude_referencia".
        if parametro == "fase_amplitude_estimada" or parametro == "fase_amplitude_referencia":
            
            # Comando para o nome do eixo das ordenadas.
            plt.ylabel(f"Var. pelo K-Fold do erro de estimação (ns)", fontsize = 18)
         
        # Caso contrário.   
        else:
            
            # Comando para o nome do eixo das ordenadas.
            plt.ylabel(f"Var. pelo K-Fold do erro de estimação (ADC Count)", fontsize = 18)
        
    # Caso opcao seja 3.
    elif opcao == 3:
        
        # Caso a variável parametro seja a igual a "fase_amplitude_estimada" ou "fase_amplitude_referencia".
        if parametro == "fase_amplitude_estimada" or parametro == "fase_amplitude_referencia":
            
            # Comando para o nome do eixo das ordenadas.
            plt.ylabel(f"DP. pelo K-Fold do erro de estimação (ns)", fontsize = 18)
        
        # Caso contrário.    
        else:
            
            # Comando para o nome do eixo das ordenadas.
            plt.ylabel(f"DP. pelo K-Fold do erro de estimação (ADC Count)", fontsize = 18)
        
    # Armazenamento dos dados referentes a ocupação 0.
    Matriz_Dados_Medias_K_Fold_OC_0 = Matriz_Dados_K_Fold_OC_0[: , indice_coluna_medias]
    Matriz_Dados_Erros_K_Fold_OC_0 = Matriz_Dados_K_Fold_OC_0[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 10.
    Matriz_Dados_Medias_K_Fold_OC_10 = Matriz_Dados_K_Fold_OC_10[: , indice_coluna_medias]
    Matriz_Dados_Erros_K_Fold_OC_10 = Matriz_Dados_K_Fold_OC_10[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 20.
    Matriz_Dados_Medias_K_Fold_OC_20 = Matriz_Dados_K_Fold_OC_20[: , indice_coluna_medias]
    Matriz_Dados_Erros_K_Fold_OC_20 = Matriz_Dados_K_Fold_OC_20[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 30.
    Matriz_Dados_Medias_K_Fold_OC_30 = Matriz_Dados_K_Fold_OC_30[: , indice_coluna_medias]
    Matriz_Dados_Erros_K_Fold_OC_30 = Matriz_Dados_K_Fold_OC_30[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 40.
    Matriz_Dados_Medias_K_Fold_OC_40 = Matriz_Dados_K_Fold_OC_40[: , indice_coluna_medias]
    Matriz_Dados_Erros_K_Fold_OC_40 = Matriz_Dados_K_Fold_OC_40[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 50.
    Matriz_Dados_Medias_K_Fold_OC_50 = Matriz_Dados_K_Fold_OC_50[: , indice_coluna_medias]
    Matriz_Dados_Erros_K_Fold_OC_50 = Matriz_Dados_K_Fold_OC_50[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 60.
    Matriz_Dados_Medias_K_Fold_OC_60 = Matriz_Dados_K_Fold_OC_60[: , indice_coluna_medias]
    Matriz_Dados_Erros_K_Fold_OC_60 = Matriz_Dados_K_Fold_OC_60[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 70.
    Matriz_Dados_Medias_K_Fold_OC_70 = Matriz_Dados_K_Fold_OC_70[: , indice_coluna_medias]
    Matriz_Dados_Erros_K_Fold_OC_70 = Matriz_Dados_K_Fold_OC_70[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 80.
    Matriz_Dados_Medias_K_Fold_OC_80 = Matriz_Dados_K_Fold_OC_80[: , indice_coluna_medias]
    Matriz_Dados_Erros_K_Fold_OC_80 = Matriz_Dados_K_Fold_OC_80[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 90.
    Matriz_Dados_Medias_K_Fold_OC_90 = Matriz_Dados_K_Fold_OC_90[: , indice_coluna_medias]
    Matriz_Dados_Erros_K_Fold_OC_90 = Matriz_Dados_K_Fold_OC_90[: , indice_coluna_DP]
    
    # Armazenamento dos dados referentes a ocupação 100.
    Matriz_Dados_Medias_K_Fold_OC_100 = Matriz_Dados_K_Fold_OC_100[: , indice_coluna_medias]
    Matriz_Dados_Erros_K_Fold_OC_100 = Matriz_Dados_K_Fold_OC_100[: , indice_coluna_DP]

    # Plote dos dados.
    plt.errorbar(janelamento, Matriz_Dados_Medias_K_Fold_OC_0, yerr = Matriz_Dados_Erros_K_Fold_OC_0, color = 'darkviolet', linestyle = '--', marker = 'o', markersize = 3, label = '0')
    plt.errorbar(janelamento, Matriz_Dados_Medias_K_Fold_OC_10, yerr = Matriz_Dados_Erros_K_Fold_OC_10, color = 'violet', linestyle = '--', marker = 'o', markersize = 3, label = '10')
    plt.errorbar(janelamento, Matriz_Dados_Medias_K_Fold_OC_20, yerr = Matriz_Dados_Erros_K_Fold_OC_20, color = 'blue', linestyle = '--', marker = 'o', markersize = 3, label = '20')
    plt.errorbar(janelamento, Matriz_Dados_Medias_K_Fold_OC_30, yerr = Matriz_Dados_Erros_K_Fold_OC_30, color = 'slateblue', linestyle = '--', marker = 'o', markersize = 3, label = '30')
    plt.errorbar(janelamento, Matriz_Dados_Medias_K_Fold_OC_40, yerr = Matriz_Dados_Erros_K_Fold_OC_40, color = 'cyan', linestyle = '--', marker = 'o', markersize = 3, label = '40')
    plt.errorbar(janelamento, Matriz_Dados_Medias_K_Fold_OC_50, yerr = Matriz_Dados_Erros_K_Fold_OC_50, color = 'green', linestyle = '--', marker = 'o', markersize = 3, label = '50')
    plt.errorbar(janelamento, Matriz_Dados_Medias_K_Fold_OC_60, yerr = Matriz_Dados_Erros_K_Fold_OC_60, color = 'greenyellow', linestyle = '--', marker = 'o', markersize = 3, label = '60')
    plt.errorbar(janelamento, Matriz_Dados_Medias_K_Fold_OC_70, yerr = Matriz_Dados_Erros_K_Fold_OC_70, color = 'yellow', linestyle = '--', marker = 'o', markersize = 3, label = '70')
    plt.errorbar(janelamento, Matriz_Dados_Medias_K_Fold_OC_80, yerr = Matriz_Dados_Erros_K_Fold_OC_80, color = 'gold', linestyle = '--', marker = 'o', markersize = 3, label = '80')
    plt.errorbar(janelamento, Matriz_Dados_Medias_K_Fold_OC_90, yerr = Matriz_Dados_Erros_K_Fold_OC_90, color = 'orange', linestyle = '--', marker = 'o', markersize = 3, label = '90')
    plt.errorbar(janelamento, Matriz_Dados_Medias_K_Fold_OC_100, yerr = Matriz_Dados_Erros_K_Fold_OC_100, color = 'red', linestyle = '--', marker = 'o', markersize = 3, label = '100')
    
    # Ajuste esse limite do eixo vertical de forma que a legenda se encaixe corretamente no gráfico.
    #plt.ylim(-5, 100)
    
    # Comando para o grid do gráfico.
    plt.grid()

    # Comando para a legenda e o posicionamento.
    plt.legend(title = 'Ocupação (OC.)', title_fontproperties = {'weight': 'bold', 'size': 12}, loc = 'upper center', fontsize = 16, ncol = 6)

    # Comando para a exibição do gráfico.
    plt.show()  
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ------------------ 2) INSTRUÇÃO PARA A CONSTRUÇÃO DO GRÁFICO DO TIPO B DA VALIDAÇÃO CRUZADA K-FOLD PELO MÉTODO OF2 OTIMIZADO --------------- ###

# Definição da instrução para a construção do gráfico do tipo B pela validação cruzada K-Fold para o método OF2 otimizado.
def grafico_B_k_fold_OF2_otimizado(parametro, opcao, Matriz_Dados_K_Fold_OC_0, Matriz_Dados_K_Fold_OC_10, Matriz_Dados_K_Fold_OC_20, Matriz_Dados_K_Fold_OC_30, Matriz_Dados_K_Fold_OC_40, Matriz_Dados_K_Fold_OC_50, Matriz_Dados_K_Fold_OC_60, Matriz_Dados_K_Fold_OC_70, Matriz_Dados_K_Fold_OC_80, Matriz_Dados_K_Fold_OC_90, Matriz_Dados_K_Fold_OC_100):
    
    # Definição do vetor das ocupações.
    ocupacoes = np.arange(0, 101, 10)
    
    # Definição da variável indice_coluna_media que armazena o índice da coluna das médias do dado estatístico.
    indice_coluna_medias = 1
    
    # Definição da variável indice_coluna_DP que armazena o índice da coluna dos desvios padrão do dado estatístico.
    indice_coluna_DP = 3
    
    # Comando para o nome do eixo das abscissas.
    plt.xlabel("Ocupações (OC.)", fontsize = 18)
    
    # Comando para o tamanho dos números do eixo das abscissas.
    plt.xticks(fontsize = 16)
    
    # Comando para o tamanho dos números do eixo das ordenadas.
    plt.yticks(fontsize = 16)
    
    # Caso opcao seja 1:
    if opcao == 1:
        
        # Caso a variável parametro seja a igual a "fase_amplitude_estimada" ou "fase_amplitude_referencia".
        if parametro == "fase_amplitude_estimada" or parametro == "fase_amplitude_referencia":
            
            # Comando para o nome do eixo das ordenadas.
            plt.ylabel(f"Média pelo K-Fold do erro de estimação (ns)", fontsize = 18)
         
        # Caso contrário.   
        else:
            
            # Comando para o nome do eixo das ordenadas.
            plt.ylabel(f"Média pelo K-Fold do erro de estimação (ADC Count)", fontsize = 18)
        
    # Caso opcao seja 2.
    elif opcao == 2:
        
        # Caso a variável parametro seja a igual a "fase_amplitude_estimada" ou "fase_amplitude_referencia".
        if parametro == "fase_amplitude_estimada" or parametro == "fase_amplitude_referencia":
            
            # Comando para o nome do eixo das ordenadas.
            plt.ylabel(f"Var. pelo K-Fold do erro de estimação (ns)", fontsize = 18)
         
        # Caso contrário.   
        else:
            
            # Comando para o nome do eixo das ordenadas.
            plt.ylabel(f"Var. pelo K-Fold do erro de estimação (ADC Count)", fontsize = 18)
        
    # Caso opcao seja 3.
    elif opcao == 3:
        
        # Caso a variável parametro seja a igual a "fase_amplitude_estimada" ou "fase_amplitude_referencia".
        if parametro == "fase_amplitude_estimada" or parametro == "fase_amplitude_referencia":
            
            # Comando para o nome do eixo das ordenadas.
            plt.ylabel(f"DP. pelo K-Fold do erro de estimação (ns)", fontsize = 18)
        
        # Caso contrário.    
        else:
            
            # Comando para o nome do eixo das ordenadas.
            plt.ylabel(f"DP. pelo K-Fold do erro de estimação (ADC Count)", fontsize = 18)
    
    # Definição dos índices para cada um dos janelamentos de acordo com a organização do arquivo de entrada.    
    indice_J7 = 0
    indice_J9 = 1
    indice_J11 = 2
    indice_J13 = 3
    indice_J15 = 4
    indice_J17 = 5
    indice_J19 = 6
        
    # Armazenamentos dos dados referentes ao janelamento 7.
    Matriz_Dados_K_Fold_J7_OC = [Matriz_Dados_K_Fold_OC_0[indice_J7, indice_coluna_medias], Matriz_Dados_K_Fold_OC_10[indice_J7, indice_coluna_medias], Matriz_Dados_K_Fold_OC_20[indice_J7, indice_coluna_medias], Matriz_Dados_K_Fold_OC_30[indice_J7, indice_coluna_medias], Matriz_Dados_K_Fold_OC_40[indice_J7, indice_coluna_medias], Matriz_Dados_K_Fold_OC_50[indice_J7, indice_coluna_medias], Matriz_Dados_K_Fold_OC_60[indice_J7, indice_coluna_medias], Matriz_Dados_K_Fold_OC_70[indice_J7, indice_coluna_medias], Matriz_Dados_K_Fold_OC_80[indice_J7, indice_coluna_medias], Matriz_Dados_K_Fold_OC_90[indice_J7, indice_coluna_medias], Matriz_Dados_K_Fold_OC_100[indice_J7, indice_coluna_medias]]
    Matriz_Dados_K_Fold_Erros_J7_OC = [Matriz_Dados_K_Fold_OC_0[indice_J7, indice_coluna_DP], Matriz_Dados_K_Fold_OC_10[indice_J7, indice_coluna_DP], Matriz_Dados_K_Fold_OC_20[indice_J7, indice_coluna_DP], Matriz_Dados_K_Fold_OC_30[indice_J7, indice_coluna_DP], Matriz_Dados_K_Fold_OC_40[indice_J7, indice_coluna_DP], Matriz_Dados_K_Fold_OC_50[indice_J7, indice_coluna_DP], Matriz_Dados_K_Fold_OC_60[indice_J7, indice_coluna_DP], Matriz_Dados_K_Fold_OC_70[indice_J7, indice_coluna_DP], Matriz_Dados_K_Fold_OC_80[indice_J7, indice_coluna_DP], Matriz_Dados_K_Fold_OC_90[indice_J7, indice_coluna_DP], Matriz_Dados_K_Fold_OC_100[indice_J7, indice_coluna_DP]]

    # Armazenamentos dos dados referentes ao janelamento 9.
    Matriz_Dados_K_Fold_J9_OC = [Matriz_Dados_K_Fold_OC_0[indice_J9, indice_coluna_medias], Matriz_Dados_K_Fold_OC_10[indice_J9, indice_coluna_medias], Matriz_Dados_K_Fold_OC_20[indice_J9, indice_coluna_medias], Matriz_Dados_K_Fold_OC_30[indice_J9, indice_coluna_medias], Matriz_Dados_K_Fold_OC_40[indice_J9, indice_coluna_medias], Matriz_Dados_K_Fold_OC_50[indice_J9, indice_coluna_medias], Matriz_Dados_K_Fold_OC_60[indice_J9, indice_coluna_medias], Matriz_Dados_K_Fold_OC_70[indice_J9, indice_coluna_medias], Matriz_Dados_K_Fold_OC_80[indice_J9, indice_coluna_medias], Matriz_Dados_K_Fold_OC_90[indice_J9, indice_coluna_medias], Matriz_Dados_K_Fold_OC_100[indice_J9, indice_coluna_medias]]
    Matriz_Dados_K_Fold_Erros_J9_OC = [Matriz_Dados_K_Fold_OC_0[indice_J9, indice_coluna_DP], Matriz_Dados_K_Fold_OC_10[indice_J9, indice_coluna_DP], Matriz_Dados_K_Fold_OC_20[indice_J9, indice_coluna_DP], Matriz_Dados_K_Fold_OC_30[indice_J9, indice_coluna_DP], Matriz_Dados_K_Fold_OC_40[indice_J9, indice_coluna_DP], Matriz_Dados_K_Fold_OC_50[indice_J9, indice_coluna_DP], Matriz_Dados_K_Fold_OC_60[indice_J9, indice_coluna_DP], Matriz_Dados_K_Fold_OC_70[indice_J9, indice_coluna_DP], Matriz_Dados_K_Fold_OC_80[indice_J9, indice_coluna_DP], Matriz_Dados_K_Fold_OC_90[indice_J9, indice_coluna_DP], Matriz_Dados_K_Fold_OC_100[indice_J9, indice_coluna_DP]]

    # Armazenamentos dos dados referentes ao janelamento 11.
    Matriz_Dados_K_Fold_J11_OC = [Matriz_Dados_K_Fold_OC_0[indice_J11, indice_coluna_medias], Matriz_Dados_K_Fold_OC_10[indice_J11, indice_coluna_medias], Matriz_Dados_K_Fold_OC_20[indice_J11, indice_coluna_medias], Matriz_Dados_K_Fold_OC_30[indice_J11, indice_coluna_medias], Matriz_Dados_K_Fold_OC_40[indice_J11, indice_coluna_medias], Matriz_Dados_K_Fold_OC_50[indice_J11, indice_coluna_medias], Matriz_Dados_K_Fold_OC_60[indice_J11, indice_coluna_medias], Matriz_Dados_K_Fold_OC_70[indice_J11, indice_coluna_medias], Matriz_Dados_K_Fold_OC_80[indice_J11, indice_coluna_medias], Matriz_Dados_K_Fold_OC_90[indice_J11, indice_coluna_medias], Matriz_Dados_K_Fold_OC_100[indice_J11, indice_coluna_medias]]
    Matriz_Dados_K_Fold_Erros_J11_OC = [Matriz_Dados_K_Fold_OC_0[indice_J11, indice_coluna_DP], Matriz_Dados_K_Fold_OC_10[indice_J11, indice_coluna_DP], Matriz_Dados_K_Fold_OC_20[indice_J11, indice_coluna_DP], Matriz_Dados_K_Fold_OC_30[indice_J11, indice_coluna_DP], Matriz_Dados_K_Fold_OC_40[indice_J11, indice_coluna_DP], Matriz_Dados_K_Fold_OC_50[indice_J11, indice_coluna_DP], Matriz_Dados_K_Fold_OC_60[indice_J11, indice_coluna_DP], Matriz_Dados_K_Fold_OC_70[indice_J11, indice_coluna_DP], Matriz_Dados_K_Fold_OC_80[indice_J11, indice_coluna_DP], Matriz_Dados_K_Fold_OC_90[indice_J11, indice_coluna_DP], Matriz_Dados_K_Fold_OC_100[indice_J11, indice_coluna_DP]]

    # Armazenamentos dos dados referentes ao janelamento 13.
    Matriz_Dados_K_Fold_J13_OC = [Matriz_Dados_K_Fold_OC_0[indice_J13, indice_coluna_medias], Matriz_Dados_K_Fold_OC_10[indice_J13, indice_coluna_medias], Matriz_Dados_K_Fold_OC_20[indice_J13, indice_coluna_medias], Matriz_Dados_K_Fold_OC_30[indice_J13, indice_coluna_medias], Matriz_Dados_K_Fold_OC_40[indice_J13, indice_coluna_medias], Matriz_Dados_K_Fold_OC_50[indice_J13, indice_coluna_medias], Matriz_Dados_K_Fold_OC_60[indice_J13, indice_coluna_medias], Matriz_Dados_K_Fold_OC_70[indice_J13, indice_coluna_medias], Matriz_Dados_K_Fold_OC_80[indice_J13, indice_coluna_medias], Matriz_Dados_K_Fold_OC_90[indice_J13, indice_coluna_medias], Matriz_Dados_K_Fold_OC_100[indice_J13, indice_coluna_medias]]
    Matriz_Dados_K_Fold_Erros_J13_OC = [Matriz_Dados_K_Fold_OC_0[indice_J13, indice_coluna_DP], Matriz_Dados_K_Fold_OC_10[indice_J13, indice_coluna_DP], Matriz_Dados_K_Fold_OC_20[indice_J13, indice_coluna_DP], Matriz_Dados_K_Fold_OC_30[indice_J13, indice_coluna_DP], Matriz_Dados_K_Fold_OC_40[indice_J13, indice_coluna_DP], Matriz_Dados_K_Fold_OC_50[indice_J13, indice_coluna_DP], Matriz_Dados_K_Fold_OC_60[indice_J13, indice_coluna_DP], Matriz_Dados_K_Fold_OC_70[indice_J13, indice_coluna_DP], Matriz_Dados_K_Fold_OC_80[indice_J13, indice_coluna_DP], Matriz_Dados_K_Fold_OC_90[indice_J13, indice_coluna_DP], Matriz_Dados_K_Fold_OC_100[indice_J13, indice_coluna_DP]]

    # Armazenamentos dos dados referentes ao janelamento 15.
    Matriz_Dados_K_Fold_J15_OC = [Matriz_Dados_K_Fold_OC_0[indice_J15, indice_coluna_medias], Matriz_Dados_K_Fold_OC_10[indice_J15, indice_coluna_medias], Matriz_Dados_K_Fold_OC_20[indice_J15, indice_coluna_medias], Matriz_Dados_K_Fold_OC_30[indice_J15, indice_coluna_medias], Matriz_Dados_K_Fold_OC_40[indice_J15, indice_coluna_medias], Matriz_Dados_K_Fold_OC_50[indice_J15, indice_coluna_medias], Matriz_Dados_K_Fold_OC_60[indice_J15, indice_coluna_medias], Matriz_Dados_K_Fold_OC_70[indice_J15, indice_coluna_medias], Matriz_Dados_K_Fold_OC_80[indice_J15, indice_coluna_medias], Matriz_Dados_K_Fold_OC_90[indice_J15, indice_coluna_medias], Matriz_Dados_K_Fold_OC_100[indice_J15, indice_coluna_medias]]
    Matriz_Dados_K_Fold_Erros_J15_OC = [Matriz_Dados_K_Fold_OC_0[indice_J15, indice_coluna_DP], Matriz_Dados_K_Fold_OC_10[indice_J15, indice_coluna_DP], Matriz_Dados_K_Fold_OC_20[indice_J15, indice_coluna_DP], Matriz_Dados_K_Fold_OC_30[indice_J15, indice_coluna_DP], Matriz_Dados_K_Fold_OC_40[indice_J15, indice_coluna_DP], Matriz_Dados_K_Fold_OC_50[indice_J15, indice_coluna_DP], Matriz_Dados_K_Fold_OC_60[indice_J15, indice_coluna_DP], Matriz_Dados_K_Fold_OC_70[indice_J15, indice_coluna_DP], Matriz_Dados_K_Fold_OC_80[indice_J15, indice_coluna_DP], Matriz_Dados_K_Fold_OC_90[indice_J15, indice_coluna_DP], Matriz_Dados_K_Fold_OC_100[indice_J15, indice_coluna_DP]]

    # Armazenamentos dos dados referentes ao janelamento 17.
    Matriz_Dados_K_Fold_J17_OC = [Matriz_Dados_K_Fold_OC_0[indice_J17, indice_coluna_medias], Matriz_Dados_K_Fold_OC_10[indice_J17, indice_coluna_medias], Matriz_Dados_K_Fold_OC_20[indice_J17, indice_coluna_medias], Matriz_Dados_K_Fold_OC_30[indice_J17, indice_coluna_medias], Matriz_Dados_K_Fold_OC_40[indice_J17, indice_coluna_medias], Matriz_Dados_K_Fold_OC_50[indice_J17, indice_coluna_medias], Matriz_Dados_K_Fold_OC_60[indice_J17, indice_coluna_medias], Matriz_Dados_K_Fold_OC_70[indice_J17, indice_coluna_medias], Matriz_Dados_K_Fold_OC_80[indice_J17, indice_coluna_medias], Matriz_Dados_K_Fold_OC_90[indice_J17, indice_coluna_medias], Matriz_Dados_K_Fold_OC_100[indice_J17, indice_coluna_medias]]
    Matriz_Dados_K_Fold_Erros_J17_OC = [Matriz_Dados_K_Fold_OC_0[indice_J17, indice_coluna_DP], Matriz_Dados_K_Fold_OC_10[indice_J17, indice_coluna_DP], Matriz_Dados_K_Fold_OC_20[indice_J17, indice_coluna_DP], Matriz_Dados_K_Fold_OC_30[indice_J17, indice_coluna_DP], Matriz_Dados_K_Fold_OC_40[indice_J17, indice_coluna_DP], Matriz_Dados_K_Fold_OC_50[indice_J17, indice_coluna_DP], Matriz_Dados_K_Fold_OC_60[indice_J17, indice_coluna_DP], Matriz_Dados_K_Fold_OC_70[indice_J17, indice_coluna_DP], Matriz_Dados_K_Fold_OC_80[indice_J17, indice_coluna_DP], Matriz_Dados_K_Fold_OC_90[indice_J17, indice_coluna_DP], Matriz_Dados_K_Fold_OC_100[indice_J17, indice_coluna_DP]]

    # Armazenamentos dos dados referentes ao janelamento 19.
    Matriz_Dados_K_Fold_J19_OC = [Matriz_Dados_K_Fold_OC_0[indice_J19, indice_coluna_medias], Matriz_Dados_K_Fold_OC_10[indice_J19, indice_coluna_medias], Matriz_Dados_K_Fold_OC_20[indice_J19, indice_coluna_medias], Matriz_Dados_K_Fold_OC_30[indice_J19, indice_coluna_medias], Matriz_Dados_K_Fold_OC_40[indice_J19, indice_coluna_medias], Matriz_Dados_K_Fold_OC_50[indice_J19, indice_coluna_medias], Matriz_Dados_K_Fold_OC_60[indice_J19, indice_coluna_medias], Matriz_Dados_K_Fold_OC_70[indice_J19, indice_coluna_medias], Matriz_Dados_K_Fold_OC_80[indice_J19, indice_coluna_medias], Matriz_Dados_K_Fold_OC_90[indice_J19, indice_coluna_medias], Matriz_Dados_K_Fold_OC_100[indice_J19, indice_coluna_medias]]
    Matriz_Dados_K_Fold_Erros_J19_OC = [Matriz_Dados_K_Fold_OC_0[indice_J19, indice_coluna_DP], Matriz_Dados_K_Fold_OC_10[indice_J19, indice_coluna_DP], Matriz_Dados_K_Fold_OC_20[indice_J19, indice_coluna_DP], Matriz_Dados_K_Fold_OC_30[indice_J19, indice_coluna_DP], Matriz_Dados_K_Fold_OC_40[indice_J19, indice_coluna_DP], Matriz_Dados_K_Fold_OC_50[indice_J19, indice_coluna_DP], Matriz_Dados_K_Fold_OC_60[indice_J19, indice_coluna_DP], Matriz_Dados_K_Fold_OC_70[indice_J19, indice_coluna_DP], Matriz_Dados_K_Fold_OC_80[indice_J19, indice_coluna_DP], Matriz_Dados_K_Fold_OC_90[indice_J19, indice_coluna_DP], Matriz_Dados_K_Fold_OC_100[indice_J19, indice_coluna_DP]]

    # Plote dos dados.
    plt.errorbar(ocupacoes, Matriz_Dados_K_Fold_J7_OC, yerr = Matriz_Dados_K_Fold_Erros_J7_OC, color = 'violet', linestyle = '--', marker = 'o', markersize = 3, label = '7')
    plt.errorbar(ocupacoes, Matriz_Dados_K_Fold_J9_OC, yerr = Matriz_Dados_K_Fold_Erros_J9_OC, color = 'blue', linestyle = '--', marker = 'o', markersize = 3, label = '9')
    plt.errorbar(ocupacoes, Matriz_Dados_K_Fold_J11_OC, yerr = Matriz_Dados_K_Fold_Erros_J11_OC, color = 'cyan', linestyle = '--', marker = 'o', markersize=3, label = '11')
    plt.errorbar(ocupacoes, Matriz_Dados_K_Fold_J13_OC, yerr = Matriz_Dados_K_Fold_Erros_J13_OC, color = 'green', linestyle = '--', marker = 'o', markersize=3, label = '13')
    plt.errorbar(ocupacoes, Matriz_Dados_K_Fold_J15_OC, yerr = Matriz_Dados_K_Fold_Erros_J15_OC, color = 'yellow', linestyle = '--', marker = 'o', markersize=3, label = '15')
    plt.errorbar(ocupacoes, Matriz_Dados_K_Fold_J17_OC, yerr = Matriz_Dados_K_Fold_Erros_J17_OC, color = 'orange', linestyle = '--', marker = 'o', markersize=3, label = '17')
    plt.errorbar(ocupacoes, Matriz_Dados_K_Fold_J19_OC, yerr = Matriz_Dados_K_Fold_Erros_J19_OC, color = 'red', linestyle = '--', marker = 'o', markersize=3, label = '19')
    
    # Ajuste esse limite do eixo vertical de forma que a legenda se encaixe corretamente no gráfico.
    #plt.ylim(-5, 100)
    
    # Comando para o grid do gráfico.
    plt.grid()

    # Comando para a legenda e o posicionamento.
    plt.legend(title = 'Janelamento', title_fontproperties = {'weight': 'bold', 'size': 12}, loc = 'upper center', fontsize = 16, ncol = 4)

    # Comando para a exibição do gráfico.
    plt.show()  
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

### ---------------------------------------------------- 4) INSTRUÇÃO PRINCIPAL DO CÓDIGO ------------------------------------------------------ ###

# Definição da instrução principal (main) do código.
def principal_grafico_k_fold_OF2_otimizado():
    
    # Impressão de mensagem no terminal.
    print("Opções de parâmetros:\nAmplitude: 1\nFase pela amplitude estimada: 2\nFase pela amplitude de referência: 3\nPedestal: 4\n")
    
    # A variável parametro armazena o número do tipo inteiro digitado pelo usuário via terminal.
    parametro = int(input("Digite o número do parâmetro desejado: "))
    
    # A variável lista_valores_parametros armazena os valroes válidos para parametro.
    lista_valores_parametro = list(range(1,5,1))
    
    # Caso o valor digitado armazenado na variável parametro não estiver presente na lista lista_valores_parametro.
    if parametro not in lista_valores_parametro:
    
        # Exibição de uma mensagem de alerta de que a opção solicitada é inválida.
        print("Essa opção é inválida!")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
    
    # Impressão de mensagem no terminal.
    print("\nTipos de gráficos:\nNúmero de janelamento versus média do dado estatístico ao decorrer das ocupações: A\nNúmero de ocupações versus média do dado estatístico ao decorrer do janelamento: B")
    
    # A variável tipo_grafico armazena a string digitada pelo usuário via terminal.
    tipo_grafico = str(input("Digite o tipo de gráfico desejado: "))
    
    # A string tipo_grafico é convertida para maiúscula.
    tipo_grafico = tipo_grafico.upper()
    
    # Se a variável tipo_grafico for diferente de "A" ou "B".
    if tipo_grafico != "A" and tipo_grafico != "B":
        
        # Exibição de uma mensagem de alerta de que o tipo de gráfico solicitado é inválido.
        print("Por favor digite uma tipo válido de gráfico: A ou B!")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
    
    # Impressão de mensagem no terminal.
    print("\nOpções de análise:\nMédia: 1\nVariância: 2\nDesvio padrão: 3\n")

    # A variável opcao_dado_estatistico armazena o número do tipo inteiro digitado pelo usuário via terminal.
    opcao_dado_estatistico = int(input("Digite o número da opção desejada: "))

    # A variável lista_valores_dado_estatistico é uma lista com os valores aceitáveis para opcao.
    lista_valores_dado_estatistico = list(range(1,4,1))

    # Caso o valor digitado armazenado na variável opcao_dado_estatistico não estiver presente na lista valores_dado_estatistico.
    if opcao_dado_estatistico not in lista_valores_dado_estatistico:
    
        # Exibição de uma mensagem de alerta de que a opção solicitada é inválida.
        print("Essa opção é inválida!")
        print("---------------------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
        
    # Caso a variável opcao_parametro seja igual a 1.
    if parametro == 1:
        
        # A variável parametro recebe a string "amplitude".
        parametro = "amplitude"
        
    # Caso a variável opcao_parametro seja igual a 2.
    elif parametro == 2:
    
        # A variável parametro recebe a string "fase_amplitude_estimada".
        parametro = "fase_amplitude_estimada"
        
    # Caso a variável opcao_parametro seja igual a 3.
    elif parametro == 3:
    
        # A variável parametro recebe a string "fase_amplitude_referencia".
        parametro = "fase_amplitude_referencia"
        
    # Caso a variável opcao_parametro seja igual a 4.
    elif parametro == 4:
        
        # A variável parametro recebe a string "pedestal".
        parametro = "pedestal" 
        
    # Caso opcao_dado_estatistico seja 1.
    if opcao_dado_estatistico == 1:
        
        # A variável dado_estatistico recebe a string "media".
        dado_estatistico = "media"
        
    # Caso opcao_dado_estatistico seja 2.
    elif opcao_dado_estatistico == 2:
        
        # A variável dado_estatistico recebe a string "var".
        dado_estatistico = "var"
        
    # Caso a opcao_dado_estatistico seja 3.
    elif opcao_dado_estatistico == 3:
        
        # A variável dado_estatistico recebe a string "DP".
        dado_estatistico = "DP"
        
    # Chamada ordenada das funções.  
      
    Matriz_Dados_K_Fold_OC_0 = leitura_dados_estatisticos_k_fold_OF2_otimizado(parametro, 0, dado_estatistico)
    Matriz_Dados_K_Fold_OC_10 = leitura_dados_estatisticos_k_fold_OF2_otimizado(parametro, 10, dado_estatistico)
    Matriz_Dados_K_Fold_OC_20 = leitura_dados_estatisticos_k_fold_OF2_otimizado(parametro, 20, dado_estatistico)
    Matriz_Dados_K_Fold_OC_30 = leitura_dados_estatisticos_k_fold_OF2_otimizado(parametro, 30, dado_estatistico)
    Matriz_Dados_K_Fold_OC_40 = leitura_dados_estatisticos_k_fold_OF2_otimizado(parametro, 40, dado_estatistico)
    Matriz_Dados_K_Fold_OC_50 = leitura_dados_estatisticos_k_fold_OF2_otimizado(parametro, 50, dado_estatistico)
    Matriz_Dados_K_Fold_OC_60 = leitura_dados_estatisticos_k_fold_OF2_otimizado(parametro, 60, dado_estatistico)
    Matriz_Dados_K_Fold_OC_70 = leitura_dados_estatisticos_k_fold_OF2_otimizado(parametro, 70, dado_estatistico)
    Matriz_Dados_K_Fold_OC_80 = leitura_dados_estatisticos_k_fold_OF2_otimizado(parametro, 80, dado_estatistico)
    Matriz_Dados_K_Fold_OC_90 = leitura_dados_estatisticos_k_fold_OF2_otimizado(parametro, 90, dado_estatistico)
    Matriz_Dados_K_Fold_OC_100 = leitura_dados_estatisticos_k_fold_OF2_otimizado(parametro, 100, dado_estatistico)
    
    # Caso a variável tipo_grafico seja "A".
    if tipo_grafico == "A":
        
        # Chamada da função grafico_A_k_fold_OF2_otimizado.
        grafico_A_k_fold_OF2_otimizado(parametro, opcao_dado_estatistico, Matriz_Dados_K_Fold_OC_0, Matriz_Dados_K_Fold_OC_10, Matriz_Dados_K_Fold_OC_20, Matriz_Dados_K_Fold_OC_30, Matriz_Dados_K_Fold_OC_40, Matriz_Dados_K_Fold_OC_50, Matriz_Dados_K_Fold_OC_60, Matriz_Dados_K_Fold_OC_70, Matriz_Dados_K_Fold_OC_80, Matriz_Dados_K_Fold_OC_90, Matriz_Dados_K_Fold_OC_100)
      
    # Caso a variável tipo_grafico seja "B".  
    elif tipo_grafico == "B":
    
        # Chamada da função grafico_B_k_fold_OF2_otimizado.
        grafico_B_k_fold_OF2_otimizado(parametro, opcao_dado_estatistico, Matriz_Dados_K_Fold_OC_0, Matriz_Dados_K_Fold_OC_10, Matriz_Dados_K_Fold_OC_20, Matriz_Dados_K_Fold_OC_30, Matriz_Dados_K_Fold_OC_40, Matriz_Dados_K_Fold_OC_50, Matriz_Dados_K_Fold_OC_60, Matriz_Dados_K_Fold_OC_70, Matriz_Dados_K_Fold_OC_80, Matriz_Dados_K_Fold_OC_90, Matriz_Dados_K_Fold_OC_100)
    
### -------------------------------------------------------------------------------------------------------------------------------------------- ###

# Chamada da instrução principal do código.
principal_grafico_k_fold_OF2_otimizado()

# Impressão de uma linha que representa o fim do programa.
print("\n---------------------------------------------------------------------------------------------------------------------------------------\n")   