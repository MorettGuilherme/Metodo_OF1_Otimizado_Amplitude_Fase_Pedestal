# EXPERIMENTO ATLAS - Reconstrução de sinal - Método do Filtro Ótimo Otimizado Sem a Restrição do Pedestal (Optimal Filtering - OF1 Otimizado).
# Autor: Guilherme Barroso Morett.
# Data: 18 de novembro de 2024.

# Objetivo do código: gráfico dos dados estatísticos ao longo das ocupações de acordo com o janelamento para o método OF1 otimizado.

""" 
Organização do Código:

Leitura dos dados estatísticos de todas as ocupações para um determinado janelamento.

Funções presentes:

1) Função para a leitura dos dados estatísticos de todas as ocupações para um determinado janelamento.
Entrada: número do janelamento.
Saída: matriz com os dados de entrada organizados de acordo com a coluna (número da ocupação, média, variância e desvio padrão do erro de estimação do parâmetro de interesse).

2) Instrução para o plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento.
Entrada: dado estatístico desejado (média, variância ou desvio padrão) e a matriz dos dados.
Saída: nada.

3) Instrução principal do código.
Entrada: nada.
Saída: nada.
"""

# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
import os
from termcolor import colored

# Impressão de uma linha que representa o início do programa.
print("\n----------------------------------------------------------------------------------------------------------------------------\n")

# Título do programa.

# A variável titulo_programa armazena o título em negrito.
titulo_programa = colored("Plote do gráfico do dado estatístico do erro de estimação da amplitude, fase ou pedestal ao longo das ocupações para um determinado janelamento pelo método Optimal Filtering (OF1 Otimizado):\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### --- 1) FUNÇÃO PARA A LEITURA DOS DADOS ESTATÍSTICOS DE TODAS AS OCUPAÇÕES PARA UM DETERMINADO JANELAMENTO PELO MÉTODO OF1 OTIMIZADO --- ###

# Definição da função para a leitura dos dados estatísticos de todas as ocupações para um determinado janelamento pelo método OF1 otimizado.
def leitura_dados_estatisticos_janelamento_OF1_otimizado(parametro, n_janelamento):

    # Nome da pasta em que se encontra o arquivo de entrada dos dados estatísticos de acordo com o parâmetro.
    pasta_dados_estatisticos_janelamento = f"Dados_Estatisticos_OF1_Otimizado_{parametro}_OC"

    # Nome do arquivo de entrada dos dados estatísticos de acordo com o janelamento.
    arquivo_dados_estatisticos_janelamento = f"dados_estatisticos_OF1_otimizado_{parametro}_janelamento_{n_janelamento}.txt"

    # O caminho para esse arquivo de entrada das ocupações.
    caminho_arquivo_dados_estatisticos_janelamento = os.path.join(pasta_dados_estatisticos_janelamento, arquivo_dados_estatisticos_janelamento)

    # Caso o caminho especificado exista.
    if os.path.exists(caminho_arquivo_dados_estatisticos_janelamento):
    
        # Abre o aquivo de entrada no modo leitura.
        with open(caminho_arquivo_dados_estatisticos_janelamento,"r") as arquivo_entrada_dados_estatisticos_janelamento:
        
            # Armazena os dados na variável Matriz_Dados_Estatisticos_Janelamento.
            Matriz_Dados_Estatisticos_Janelamento = np.array(np.loadtxt(arquivo_entrada_dados_estatisticos_janelamento, skiprows = 1, dtype = 'double', delimiter = ','))
 
    # Caso contrário.       
    else:
    
        # Impressão de mensagem que o arquivo de entrada não existe.
        print(f"O arquivo {arquivo_dados_estatisticos_janelamento} não existe na pasta {pasta_dados_estatisticos_janelamento}.")

    # Obs.: da forma que o programa está escrito, os arquivos de entrada devem estar na mesma pasta em que está o código do programa.
    # Caso deseja-se alterar isso basta mudar o endereço do arquivo.
    
    # A função retorna a matriz Matriz_Dados_Estatisticos_Janelamento.
    return Matriz_Dados_Estatisticos_Janelamento

### --------------------------------------------------------------------------------------------------------------------------------- ###

### --- 2) INSTRUÇÃO PARA O PLOTE DOS GRÁFICO DO DADO ESTATÍSTICO AO LONGO DAS OCUPAÇÕES PARA UM DETERMINADO JANELAMENTO PELO MÉTODO OF1 OTIMIZADO --- ###

# Definição da instrução para o plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento pelo método OF1 otimizado.
def grafico_dado_estatistico_janelamento_OF1_otimizado(parametro, dado_estatistico, Matriz_Dados_Estatisticos_Janelamento):
    
    # Definição da variável indice_coluna_ocupacoes que armazena o valor do índice da coluna das ocupações.
    indice_coluna_ocupacoes = 0
    
    # Definição da variável indice_coluna_media que armazena o valor do índice da coluna das médias.
    indice_coluna_media = 1
    
    # Definição da variável indice_coluna_var que armazena o valor do índice da coluna das variâncias.
    indice_coluna_var = 2
    
    # Definição da variável indice_coluna_DP que armazena o valor do índice da coluna dos desvio padrão.
    indice_coluna_DP = 3
    
    # Definição do eixo das abscissas.
    vetor_ocupacoes = Matriz_Dados_Estatisticos_Janelamento[: , indice_coluna_ocupacoes]
    
    # Comando para o nome do eixo das abscissas.
    plt.xlabel("Ocupação (OC.)", fontsize = 18)
    
    # Comando que define o tamanho dos números do eixo das abscissas.
    plt.xticks(fontsize = 16)
    
    # Caso a variável dado_estatístico seja 1 (média).
    if dado_estatistico == 1:
        
        # Definição do vetor dos dados estatísticos.
        vetor_dados = Matriz_Dados_Estatisticos_Janelamento[: , indice_coluna_media]
        
        # Caso a variável parametro seja a igual a "fase_amplitude_estimada" ou "fase_amplitude_referencia".
        if parametro == "fase_amplitude_estimada" or parametro == "fase_amplitude_referencia":
            
            # Comando para o nome do eixo das ordenadas de acordo com a fase.
            plt.ylabel(f"Média do erro de estimação da fase (ns)", fontsize = 18)
        
        # Caso a variável parametro seja igual ao "pedestal".
        elif parametro == "pedestal":
        
            # Comando para o nome do eixo das ordenadas de acordo com o pedestal.
            plt.ylabel(f"Média do erro de estimação do {parametro} (ADC Count)", fontsize = 18)
            
        else:
            
            # Comando para o nome do eixo das ordenadas de acordo com os demais parâmetros.
            plt.ylabel(f"Média do erro de estimação da {parametro} (ADC Count)", fontsize = 18)
        
    # Caso a variável dado_estatístico seja 2 (variância).
    elif dado_estatistico == 2:
        
        # Definição do vetor dos dados estatísticos.
        vetor_dados = Matriz_Dados_Estatisticos_Janelamento[: , indice_coluna_var]
        
        # Caso a variável parametro seja a igual a "fase_amplitude_estimada" ou "fase_amplitude_referencia".
        if parametro == "fase_amplitude_estimada" or parametro == "fase_amplitude_referencia":
            
            # Comando para o nome do eixo das ordenadas de acordo com a fase.
            plt.ylabel(f"Var. do erro de estimação da fase (ns)", fontsize = 18)
        
        # Caso a variável parametro seja igual ao "pedestal".
        elif parametro == "pedestal":
        
            # Comando para o nome do eixo das ordenadas de acordo com o pedestal.
            plt.ylabel(f"Var. do erro de estimação do {parametro} (ADC Count)", fontsize = 18)
            
        else:
            
            # Comando para o nome do eixo das ordenadas de acordo com os demais parâmetros.
            plt.ylabel(f"Var. do erro de estimação da {parametro} (ADC Count)", fontsize = 18)
        
    # Caso a variável dado_estatistico seja 3 (desvio padrão).
    elif dado_estatistico == 3:
        
        # Definição do vetor dos dados estatísticos.
        vetor_dados = Matriz_Dados_Estatisticos_Janelamento[: , indice_coluna_DP]
        
        # Caso a variável parametro seja a igual a "fase_amplitude_estimada" ou "fase_amplitude_referencia".
        if parametro == "fase_amplitude_estimada" or parametro == "fase_amplitude_referencia":
            
            # Comando para o nome do eixo das ordenadas de acordo com a fase.
            plt.ylabel(f"DP. do erro de estimação da fase (ns)", fontsize = 18)
        
        # Caso a variável parametro seja igual ao "pedestal".
        elif parametro == "pedestal":
        
            # Comando para o nome do eixo das ordenadas de acordo com o pedestal.
            plt.ylabel(f"DP. do erro de estimação do {parametro} (ADC Count)", fontsize = 18)
         
        # Caso contrário.   
        else:
            
            # Comando para o nome do eixo das ordenadas de acordo com os demais parâmetros.
            plt.ylabel(f"DP. do erro de estimação da {parametro} (ADC Count)", fontsize = 18)
        
    # Comando que define o tamanho dos números do eixo das ordenadas.
    plt.yticks(fontsize = 16)
    
    # Comando para o plote do gráfico.
    plt.plot(vetor_ocupacoes, vetor_dados, color = 'blue', linestyle = '--', marker = 'o')
    
    # Comando para o grid.
    plt.grid()
    
    # Comando para o plote.
    plt.show()
        
### --------------------------------------------------------------------------------------------------------------------------------- ###        
    
### -------------------------------------------- 3) INSTRUÇÃO PRINCIPAL DO CÓDIGO  -------------------------------------------------- ###

# Definição da instrução principal do código.
def principal_grafico_dado_estatistico_janelamento_OF1_otimizado():
    
    # Impressão de mensagem no terminal.
    print("Opções de parâmetros:\nAmplitude: 1\nFase pela amplitude estimada: 2\nFase pela amplitude de referência: 3\nPedestal: 4\n")
    
    # A variável parametro armazena o número do tipo inteiro digitado pelo usuário via terminal.
    parametro = int(input("Digite o número do parâmetro desejado: "))
    
    # A variável lista_valores_parametros armazena os valores válidos para parametro.
    lista_valores_parametro = list(range(1,5,1))
    
    # Caso o valor digitado armazenado na variável parametro não estiver presente na lista lista_valores_parametro.
    if parametro not in lista_valores_parametro:
    
        # Exibição de uma mensagem de alerta de que a opção solicitada é inválida.
        print("Essa opção é inválida!")
        print("------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
    
    # Impressão de mensagem no terminal.
    print("Opções de análise:\nMédia: 1\nVariância: 2\nDesvio padrão: 3\n")

    # A variável dado_estatistico armazena o número do tipo inteiro digitado pelo usuário via terminal.
    dado_estatistico = int(input("Digite o número da opção desejada: "))

    # A variável valores_dados_estatisticos é uma lista com os valores aceitáveis para dado_estatistico.
    lista_valores_dados_estatisticos = list(range(1,4,1))

    # Caso o valor digitado armazenado na variável dado_estatistico não estiver presente na lista lista_valores_dados_estatisticos.
    if dado_estatistico  not in lista_valores_dados_estatisticos:
    
        # Exibição de uma mensagem de alerta de que a opção solicitada é inválida.
        print("Essa opção é inválida!")
        print("------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
        
    # Caso a variável parametro seja igual a 1.
    if parametro == 1:
        
        # A variável parametro recebe a string "amplitude".
        parametro = "amplitude"
        
    # Caso a variável parametro seja igual a 2.
    elif parametro == 2:
    
        # A variável parametro recebe a string "fase_amplitude_estimada".
        parametro = "fase_amplitude_estimada"
        
    # Caso a variável parametro seja igual a 3.
    elif parametro == 3:
    
        # A variável parametro recebe a string "fase_amplitude_referencia".
        parametro = "fase_amplitude_referencia"
        
    # Caso a variável parametro seja igual a 3.
    elif parametro == 4:
        
        # A variável parametro recebe a string "pedestal".
        parametro = "pedestal"  
    
    # A variável n_janelamento armazena a quantidade de janelamento especificada no terminal pelo usuário.
    n_janelamento = int(input("Digite a quantidade de janelamento: "))

    # A variável valores_janelamento é uma lista com os valores aceitáveis do janelamento de 7 até 19 com incremento de 2.
    valores_janelamento = list(range(7,20,2))

    # Caso o valor digitado armazenado na variável n_janelamento não estiver presente na lista valores_janelamento.
    if n_janelamento not in valores_janelamento:
    
        # Exibição de uma mensagem de alerta de que a quantidade de janelamento solicitada é inválida.
        print("Quantidade de janelamento inválida! Opções de janelamento: 7, 9, 11, 13, 15, 17, 19.")
        print("------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
        
    # Chamada ordenada das funções.
    
    Matriz_Dados_Estatisticos_Janelamento = leitura_dados_estatisticos_janelamento_OF1_otimizado(parametro, n_janelamento)
    grafico_dado_estatistico_janelamento_OF1_otimizado(parametro, dado_estatistico, Matriz_Dados_Estatisticos_Janelamento)
    
# Chamada da instrução principal do código.
principal_grafico_dado_estatistico_janelamento_OF1_otimizado()

### --------------------------------------------------------------------------------------------------------------------------------- ###

# Impressão de uma linha que representa o fim do programa.
print("\n----------------------------------------------------------------------------------------------------------------------------\n")
    
