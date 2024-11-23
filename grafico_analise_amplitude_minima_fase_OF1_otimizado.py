# EXPERIMENTO ATLAS - Reconstrução de sinal - Método do Filtro Ótimo Otimizado Sem a Restrição do Pedestal (Optimal Filtering - OF1 Otimizado).
# Autor: Guilherme Barroso Morett.
# Data: 18 de novembro de 2024.

# Objetivo do código: gráfico dos dados estatísticos do erro de estimação da fase para uma determinada ocupação versus o valor mínimo da amplitude de acordo com o janelamento ideal para a amplitude estimada pelo método OF1 otimizado.

""" 
Organização do Código:

Funções presentes:

1) Função para a leitura dos dados estatísticos da análise erro de estimação da fase para uma dada ocupação pelo método OF1 otimizado.
Entrada: número da ocupação, número do janelamento ideal para a amplitude estimada e dado estatístico de interesse.
Saída: Matriz com os dados de entrada organizados de acordo com a coluna (valor mínimo da amplitude estimada, média do dado estatístico, variância do dado estatístico, desvio padrão do dado estatístico e quantidade de elementos do vetor que contém os erros de estimação da fase).

2) Instrução para o plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento pelo processo de estimação da fase.
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
titulo_programa = colored("Plote do gráfico do dado estatístico da análise do erro de estimação da fase pelo método Optimal Filtering (OF1 Otimizado):\n", attrs=["bold"])

# Impressão do título do programa.
print(titulo_programa)

### ---- 1) FUNÇÃO PARA A LEITURA DOS DADOS ESTATÍSTICOS DA ANÁLISE DO ERRO DE ESTIMAÇÃO DA FASE PARA UMA DADA OCUPAÇÃO PELO MÉTODO OF1 OTIMIZADO --- ###

# Definição da função para a leitura dos dados estatísticos da análise do erro de estimação da fase pelo método OF1 otimizado.
def leitura_dados_estatisticos_analise_fase_OF1_otimizado(n_ocupacao, n_janelamento_ideal_amplitude_estimada, dado_estatistico, tipo_fase):

    # Nome da pasta em que se encontra o arquivo de entrada dos dados estatísticos da estimação da fase de acordo com a ocupação.
    pasta_dados_estatisticos_analise_fase_ocupacao = f"K_Fold_{tipo_fase}_{dado_estatistico}_J_{n_janelamento_ideal_amplitude_estimada}"

    # Nome do arquivo de entrada dos dados estatísticos da estimação da fase de acordo com a ocupação.
    arquivo_dados_estatisticos_analise_fase_ocupacao = f"k_fold_{tipo_fase}_{dado_estatistico}_OC_{n_ocupacao}.txt"

    # O caminho para esse arquivo de entrada das ocupações.
    caminho_arquivo_dados_estatisticos_analise_fase_ocupacao = os.path.join(pasta_dados_estatisticos_analise_fase_ocupacao, arquivo_dados_estatisticos_analise_fase_ocupacao)

    # Caso o caminho especificado exista.
    if os.path.exists(caminho_arquivo_dados_estatisticos_analise_fase_ocupacao):
    
        # Abre o aquivo de entrada no modo leitura.
        with open(caminho_arquivo_dados_estatisticos_analise_fase_ocupacao,"r") as arquivo_entrada_dados_estatisticos_analise_fase_ocupacao:
        
            # Armazena os dados na variável Matriz_Dados_Estatisticos_Analise_Fase_Ocupacao.
            Matriz_Dados_Estatisticos_Analise_Fase_Ocupacao = np.array(np.loadtxt(arquivo_entrada_dados_estatisticos_analise_fase_ocupacao, skiprows = 1, dtype = 'double', delimiter = ','))
 
    # Caso contrário.       
    else:
    
        # Impressão de mensagem que o arquivo de entrada não existe.
        print(f"O arquivo {arquivo_dados_estatisticos_analise_fase_ocupacao} não existe na pasta {pasta_dados_estatisticos_analise_fase_ocupacao}.")

    # Obs.: da forma que o programa está escrito, os arquivos de entrada devem estar na mesma pasta em que está o código do programa.
    # Caso deseja-se alterar isso basta mudar o endereço do arquivo.
    
    # A função retorna a matriz Matriz_Dados_Estatisticos_Analise_Fase_Ocupacao.
    return Matriz_Dados_Estatisticos_Analise_Fase_Ocupacao

### --------------------------------------------------------------------------------------------------------------------------------- ###

### --- 2) INSTRUÇÃO PARA O PLOTE DOS GRÁFICO DO ANÁLISE DA ESTIMAÇÃO DA FASE PARA UMA DETERMINADA OCUPAÇÃO PELO MÉTODO OF1 OTIMIZADO --- ###

# Definição da instrução para o plote do gráfico do dado estatístico da análise da estimação da fase para uma determinada ocupação pelo método OF1 otimizado.
def grafico_dado_estatistico_analise_fase_OF1_otimizado(n_ocupacao, opcao_dado_estatistico, Matriz_Dados_Estatisticos_Analise_Fase_Ocupacao):
    
    # Definição da variável indice_coluna_valores_minimos_amplitude_estimada que armazena o valor do índice da coluna dos valores mínimos da amplitude estimada.
    indice_coluna_valores_minimos_amplitude_estimada = 0
    
    # Definição da variável indice_coluna_media que armazena o valor do índice da coluna das médias.
    indice_coluna_media = 1
    
    # Definição da variável indice_coluna_var que armazena o valor do índice da coluna das variâncias.
    indice_coluna_var = 2
    
    # Definição da variável indice_coluna_DP que armazena o valor do índice da coluna dos desvios padrão.
    indice_coluna_DP = 3
    
    # Definição da variável indice_coluna_tamanho_vetor_erro_estimacao que armazena a quantidade de elementos presentes no vetor do erro de estimação da fase.
    indice_coluna_tamanho_vetor_erro_estimacao = 4
    
    # Definição do eixo das abscissas.
    vetor_valores_minimos_amplitude_estimada = Matriz_Dados_Estatisticos_Analise_Fase_Ocupacao[: , indice_coluna_valores_minimos_amplitude_estimada]
    
    # Definição do vetor vetor_tamanhos_vetores_erro_estimacao
    vetor_tamanhos_vetores_erro_estimacao = Matriz_Dados_Estatisticos_Analise_Fase_Ocupacao[: , indice_coluna_tamanho_vetor_erro_estimacao]
    
    # Definição do vetor da barra de erro.
    vetor_barra_erro = Matriz_Dados_Estatisticos_Analise_Fase_Ocupacao[: , indice_coluna_DP]
    
    # Comando para o nome do eixo das abscissas.
    plt.xlabel("Valores mínimos da amplitude estimada (ADC Count)", fontsize = 18)
    
    # Comando que define o tamanho dos números do eixo das abscissas.
    plt.xticks(fontsize = 16)
    
    # Caso a variável opcao_dado_estatistico seja 1 (média).
    if opcao_dado_estatistico == 1:
        
        # Definição do vetor dos dados estatísticos.
        vetor_dados = Matriz_Dados_Estatisticos_Analise_Fase_Ocupacao[: , indice_coluna_media]
        
        # Comando para o nome do eixo das ordenadas de acordo com a fase.
        plt.ylabel("Média do erro de estimação da fase (ns)", fontsize = 18)
        
    # Caso a variável opcao_dado_estatistico seja 2 (variância).
    elif opcao_dado_estatistico == 2:
        
        # Definição do vetor dos dados estatísticos.
        vetor_dados = Matriz_Dados_Estatisticos_Analise_Fase_Ocupacao[: , indice_coluna_var]
        
        # Comando para o nome do eixo das ordenadas de acordo com a fase.
        plt.ylabel("Var. do erro de estimação da fase (ns)", fontsize = 18)
            
    # Caso a variável dado_estatistico seja 3 (desvio padrão).
    elif opcao_dado_estatistico == 3:
        
        # Definição do vetor dos dados estatísticos.
        vetor_dados = Matriz_Dados_Estatisticos_Analise_Fase_Ocupacao[: , indice_coluna_DP]
            
        # Comando para o nome do eixo das ordenadas de acordo com a fase.
        plt.ylabel("DP. do erro de estimação da fase (ns)", fontsize = 18)
        
    # Comando que define o tamanho dos números do eixo das ordenadas.
    plt.yticks(fontsize = 16)
    
    # Impressão do título do gráfico (recomendável para a apresentação de slides).
    #plt.title(f"Ocupação {n_ocupacao}", fontsize = 18)
    
    # Definição das variáveis que armazenam a porcentagem da média da quantidade de elementos no vetor de acordo com o valor da amplitude mínima.
    media_quantidade_amplitude_minima_1 = round((vetor_tamanhos_vetores_erro_estimacao[0]/20000)*100,2)
    media_quantidade_amplitude_minima_4v5 = round((vetor_tamanhos_vetores_erro_estimacao[1]/20000)*100,2)
    media_quantidade_amplitude_minima_10 = round((vetor_tamanhos_vetores_erro_estimacao[2]/20000)*100,2)
    media_quantidade_amplitude_minima_25 = round((vetor_tamanhos_vetores_erro_estimacao[3]/20000)*100,2)
    media_quantidade_amplitude_minima_50 = round((vetor_tamanhos_vetores_erro_estimacao[4]/20000)*100,2)
    media_quantidade_amplitude_minima_75 = round((vetor_tamanhos_vetores_erro_estimacao[5]/20000)*100,2)
    media_quantidade_amplitude_minima_100 = round((vetor_tamanhos_vetores_erro_estimacao[6]/20000)*100,2)
    
    media_quantidade_amplitude_minima_1 = "{:.2f}".format(media_quantidade_amplitude_minima_1).replace('.', ',')
    media_quantidade_amplitude_minima_4v5 = "{:.2f}".format(media_quantidade_amplitude_minima_4v5).replace('.', ',')
    media_quantidade_amplitude_minima_10 = "{:.2f}".format(media_quantidade_amplitude_minima_10).replace('.', ',')
    media_quantidade_amplitude_minima_25 = "{:.2f}".format(media_quantidade_amplitude_minima_25).replace('.', ',')
    media_quantidade_amplitude_minima_50 = "{:.2f}".format(media_quantidade_amplitude_minima_50).replace('.', ',')
    media_quantidade_amplitude_minima_75 = "{:.2f}".format(media_quantidade_amplitude_minima_75).replace('.', ',')
    media_quantidade_amplitude_minima_100 = "{:.2f}".format(media_quantidade_amplitude_minima_100).replace('.', ',')
    
    # A variável texto recebe uma string com as informações da média da quantidade de amplitudes estimadas que foram usadas no processo de estimação da fase, consdierando que cada bloco do K-fold contém 20000 amostras.
    texto = f"Porcentagem do número médio de amostras\nsegundo a amplitude mínima considerada:\n1 ADC Count = {media_quantidade_amplitude_minima_1} %\n4,5 ADC Count =  {media_quantidade_amplitude_minima_4v5} %\n10 ADC Count =  {media_quantidade_amplitude_minima_10} %\n25 ADC Count = {media_quantidade_amplitude_minima_25} %\n50 ADC Count = {media_quantidade_amplitude_minima_50} %\n75 ADC Count = {media_quantidade_amplitude_minima_75} %\n100 ADC Count = {media_quantidade_amplitude_minima_100} %"
    
    # Comando para o plote do gráfico.
    plt.errorbar(vetor_valores_minimos_amplitude_estimada, vetor_dados, yerr =  vetor_barra_erro, color = 'blue', linestyle = '--', marker = 'o', markerfacecolor='red', markersize = 4)
    
    # Posicionamento do texto no gráfico.
    plt.text(0.95, 0.3, texto, horizontalalignment = 'right',
    verticalalignment = 'center',
    transform = plt.gca().transAxes,
    bbox = dict(facecolor = 'white', alpha = 0.5),
    fontsize = 14)
    
    # Ajuste esse limite do eixo vertical de forma que a legenda se encaixe corretamente no gráfico.
    #plt.ylim(-6, -2)
    
    # Comando para o grid.
    plt.grid()
    
    # Comando para o plote.
    plt.show()
        
### --------------------------------------------------------------------------------------------------------------------------------- ###        
        
### --------------------------------------------- 3) INSTRUÇÃO PRINCIPAL DO CÓDIGO -------------------------------------------------- ###

# Definição da instrução principal do código.
def principal_grafico_dado_estatistico_analise_fase_OF1_otimizado():
    
    # A variável tipo_opcao_fase armazena a escolha digitada pelo usuário para o processo de estimação da fase.
    tipo_opcao_fase = int(input("Opções para a análise do processo de estimação da fase:\nAmplitude estimada: 1\nAmplitude de referência: 2\nDigite a opção desejada: "))
    
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
        
    # Se a variável tipo_fase for igual a 2.
    elif tipo_opcao_fase == 2:
        
        # A variável tipo_fase recebe a string "fase_analise_amplitude_minima_referencia"
        tipo_fase = "fase_analise_amplitude_minima_referencia"
    
    # Impressão de mensagem no terminal.
    print("Opções de análise:\nMédia: 1\nVariância: 2\nDesvio padrão: 3\n")

    # A variável dado_estatistico armazena o número do tipo inteiro digitado pelo usuário via terminal.
    opcao_dado_estatistico = int(input("Digite o número da opção desejada para o dado estatístico: "))

    # A variável valores_dados é uma lista com os valores aceitáveis para dado_estatistico.
    valores_opcoes_dados_estatisticos = list(range(1,4,1))

    # Caso o valor digitado armazenado na variável opcao_dado_estatistico não estiver presente na lista valores_opcoes_dados_estatisticos.
    if opcao_dado_estatistico  not in valores_opcoes_dados_estatisticos:
    
        # Exibição de uma mensagem de alerta de que a opção solicitada é inválida.
        print("Essa opção de dado estatístico é inválida!")
        print("------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1) 
        
    # Caso opcao_dado_estatistico seja igual a 1.
    if opcao_dado_estatistico == 1:
        
        # A variável dado_estatistico recebe a string "media".
        dado_estatistico = "media"
      
    # Caso opcao_dado_estatistico seja igual a 1.  
    elif opcao_dado_estatistico == 2:
        
        # A variável dado_estatistico recebe a string "var".
        
        dado_estatistico = "var"
        
    # Caso opcao_dado_estatistico seja igual a 3.  
    elif opcao_dado_estatistico == 3:
        
        # A variável dado_estatistico recebe a string "DP".
        
        dado_estatistico = "DP"
    
    # A variável n_ocupação armazena a quantidade da ocupação especificada no terminal pelo usuário.
    n_ocupacao = int(input("Digite a quantidade de ocupação desejada: "))

    # A variável valores_ocupacoes é uma lista com os valores aceitáveis para n_ocupacao.
    #Obs.: em virtude do alto índice de valores baixos para a amplitude estimada na ocupação 0, esta não foi possível analisar.
    valores_ocupacoes = list(range(10,101,10))
    
    # A variável n_janelamento_ideal_amplitude_estimada recebe o valor ideal da amplitude estimada pela análise dos grafícos do K-Fold.
    n_janelamento_ideal_amplitude_estimada = 17

    # Caso o valor digitado armazenado na variável n_ocupação não estiver presente na lista valores_ocupacao.
    if n_ocupacao not in valores_ocupacoes:
    
        # Exibição de uma mensagem de alerta de que a quantidade de janelamento solicitada é inválida.
        print("Quantidade de ocupações inválida! Opções de ocupações de 10 a 100 com incremento de 10.\nem virtude do alto índice de valores baixos para a amplitude estimada na ocupação 0, esta não foi possível analisar.")
        print("------------------------------------------------------------------------------------------------------------------------")
        # A execução do programa é interrompida.
        exit(1)
        
    # Chamada ordenada das funções.
    
    Matriz_Dados_Estatisticos_Analise_Fase_Ocupacao = leitura_dados_estatisticos_analise_fase_OF1_otimizado(n_ocupacao, n_janelamento_ideal_amplitude_estimada, dado_estatistico, tipo_fase)
    grafico_dado_estatistico_analise_fase_OF1_otimizado(n_ocupacao, opcao_dado_estatistico, Matriz_Dados_Estatisticos_Analise_Fase_Ocupacao)
    
# Chamada da instrução principal do código.
principal_grafico_dado_estatistico_analise_fase_OF1_otimizado()

### --------------------------------------------------------------------------------------------------------------------------------- ###

# Impressão de uma linha que representa o fim do programa.
print("\n----------------------------------------------------------------------------------------------------------------------------\n")
    
