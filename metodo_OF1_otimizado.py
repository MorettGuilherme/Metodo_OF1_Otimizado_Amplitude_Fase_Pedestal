# EXPERIMENTO ATLAS - Reconstrução de sinal - Método do Filtro Ótimo Otimizado Sem a Restrição do Pedestal (Optimal Filtering - OF1 Otimizado).
# Autor: Guilherme Barroso Morett.
# Data: 18 de novembro de 2024.

# Objetivo do código: aplicação do método do Filtro Ótimo Otimizado (Optimal Filtering - OF1 Otimizado).

"""
Organização do código:

Leitura dos dados de entrada de acordo com o janelamento desejado.
Os dados de entrada das ocupações no formato de arquivo texto (txt) contém informações sobre os pulsos de sinais (ADC Count), a amplitude de referência (ADC Count), a fase de referência (ns) e o ruído eletrônico (ADC Count).
O valor de referência considerado para o pedestal foi de 30 ADC Count.

Funções presentes:

1) Função para a definição do vetor pulso de referência.
Entrada: número de janelamento.
Saída: vetor pulso de referência para cada instante de tempo de acordo com o janelamento.

2) Função para a definição do vetor da derivada temporal do pulso de referência.
Entrada: número de janelamento.
Saída: vetor da derivada temporal do pulso de referência para cada instante de tempo de acordo com o janelamento.

3) Função para a construção da matriz de coeficientes do método OF1 otimizado.
Entrada: número de janelamento, matriz de covariância, vetor pulso de referência, vetor da derivada do pulso de referência.
Saída: matriz de coeficientes adaptada para determinado janelamento.

4) Vetor de resposta do método OF1 otimizado.
Entrada: número de janelamento.
Saída: vetor de resposta adaptado para determinado janelamento.

3) Função para o método OF1 otimizado.
Entrada: parâmetro, matriz com os pulsos de sinais, vetor com o parâmetro de referência e o número de janelamento.
Saída: lista com o erro de estimação pelo método OF1 otimizado.

"""

# Importação das bibliotecas.
import numpy as np

# Importação dos arquivos.
from leitura_dados_ocupacao_OF1_otimizado import *
from leitura_dados_ruidos_OF1_otimizado import *

### ---------------------------------------- 1) FUNÇÃO PARA O PULSO DE REFERÊNCIA --------------------------------------------------- ###

# Definição da função para o vetor pulso de referência de acordo com o janelamento.
def pulso_referencia(n_janelamento): 
    
    # Criação das variáveis que armazenam os valores dos pulsos de referência para cada cada instante de tempo.
    h_tm225 = 0.0 # t = -225,0 ns
    h_tm200 = 0.0 # t = -220,0 ns
    h_tm175 = 0.0 # t = -175,0 ns
    h_tm150 = 0.0 # t = -150,0 ns
    h_tm125 = 0.0 # t = -125,0 ns
    h_tm100 = 0.0 # t = -100,0 ns
    h_tm75 = 2.304e-05 # t = -75,0 ns
    h_tm50 = 0.0172264 # t = -50,0 ns
    h_tm25 = 0.452445 # t = -25,0 ns
    h_t0 = 1.0 # t = 0,0 ns
    h_tM25 = 0.563307 # t = 25,0 ns
    h_tM50 = 0.149335 # t = 50,0 ns
    h_tM75 = 0.0423598 # t = 75,0 ns
    h_tM100 = 0.00480767 # t = 100,0 ns
    h_tM125 = 0.0 # t = 125,0 ns
    h_tM150 = 0.0 # t = 150,0 ns
    h_tM175 = 0.0 # t = 175,0 ns
    h_tM200 = 0.0 # t = 200,0 ns
    h_tM225 = 0.0 # t = 225,0 ns
       
    # Caso o janelamento seja igual a 7.
    if n_janelamento == 7:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 7 no intervalo de tempo de -75,0 a 75,0 ns.
        vetor_pulso_referencia = np.array([h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75])
        
    # Caso o janelamento seja igual a 9.
    elif n_janelamento == 9:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 9 no intervalo de tempo de -100,0 a 100,0 ns.
        vetor_pulso_referencia = np.array([h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100])
        
    # Caso o janelamento seja igual a 11.
    elif n_janelamento == 11:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 11 no intervalo de tempo de -125,0 a 125,0 ns.
        vetor_pulso_referencia = np.array([h_tm125, h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100, h_tM125])
        
    # Caso o janelamento seja igual a 13.
    elif n_janelamento == 13:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 13 no intervalo de tempo de -150,0 a 150,0 ns.
        vetor_pulso_referencia = np.array([h_tm150, h_tm125, h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100, h_tM125, h_tM150])
        
    # Caso o janelamento seja igual a 15.
    elif n_janelamento == 15:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 15 no intervalo de tempo de -175,0 a 175,0 ns.
        vetor_pulso_referencia = np.array([h_tm175, h_tm150, h_tm125, h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100, h_tM125, h_tM150, h_tM175])   

    # Caso o janelamento seja igual a 17.
    elif n_janelamento == 17:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 17 no intervalo de tempo de -200,0 a 200,0 ns.
        vetor_pulso_referencia = np.array([h_tm200, h_tm175, h_tm150, h_tm125, h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100, h_tM125, h_tM150, h_tM175, h_tM200]) 
        
    # Caso o janelamento seja igual a 19.
    elif n_janelamento == 19:
        
        # Definição do vetor pulso de referência de acordo com o janelamento 19 no intervalo de tempo de -225,0 a 225,0 ns.
        vetor_pulso_referencia = np.array([h_tm225, h_tm200, h_tm175, h_tm150, h_tm125, h_tm100, h_tm75, h_tm50, h_tm25, h_t0, h_tM25, h_tM50, h_tM75, h_tM100, h_tM125, h_tM150, h_tM175, h_tM200, h_tM225])     

    # A função retorna o vetor pulso de referência.
    return vetor_pulso_referencia

### --------------------------------------------------------------------------------------------------------------------------------- ###

### -------------------------------------- 2) FUNÇÃO PARA A DERIVADA DO PULSO DE REFERÊNCIA ----------------------------------------- ###

# Definição da função para o vetor da derivada do pulso de referência de acordo com o janelamento.
def derivada_pulso_referencia(n_janelamento):
    
    # Criação das variáveis que armazenam os valores das derivadas dos pulsos de referência para cada cada instante de tempo.
    dh_tm225 = 0.0 # t = -225,0 ns
    dh_tm200 = 0.0 # t = -220,0 ns
    dh_tm175 = 0.0 # t = -175,0 ns
    dh_tm150 = 0.0 # t = -150,0 ns
    dh_tm125 = 0.0 # t = -125,0 ns
    dh_tm100 = 0.0 # t = -100,0 ns
    dh_tm75 = 5.472e-05 # t = -75,0 ns
    dh_tm50 = 0.0036703166666666675 # t = -50,0 ns
    dh_tm25 = 0.031080499999999955 # t = -25,0 ns
    dh_t0 = 1.666666668009853e-07 # t = 0,0 ns
    dh_tM25 = -0.024345499999999964 # t = 25,0 ns
    dh_tM50 = -0.008006833333333371 # t = 50,0 ns
    dh_tM75 = -0.0024333666666666635 # t = 75,0 ns
    dh_tM100 = -0.0005361350000000002 # t = 100,0 ns
    dh_tM125 = -0.00215426 # t = 125,0 ns
    dh_tM150 = 0.0 # t = 150,0 ns
    dh_tM175 = 0.0 # t = 175,0 ns
    dh_tM200 = 0.0 # t = 200,0 ns
    dh_tM225 = 0.0 # t = 225,0 ns
    
    # Caso o janelamento seja igual a 7.
    if n_janelamento == 7:
        
        # Definição do vetor da derivada do pulso de referência de acordo com o janelamento 7 no intervalo de tempo de -75,0 a 75,0 ns.
        vetor_derivada_pulso_referencia = np.array([dh_tm75, dh_tm50, dh_tm25, dh_t0, dh_tM25, dh_tM50, dh_tM75])
        
    # Caso o janelamento seja igual a 9.
    elif n_janelamento == 9:
        
        # Definição do vetor da derivada do pulso de referência de acordo com o janelamento 9 no intervalo de tempo de -100,0 a 100,0 ns.
        vetor_derivada_pulso_referencia = np.array([dh_tm100, dh_tm75, dh_tm50, dh_tm25, dh_t0, dh_tM25, dh_tM50, dh_tM75, dh_tM100])
        
    # Caso o janelamento seja igual a 11.
    elif n_janelamento == 11:
        
        # Definição do vetor da derivada do pulso de referência de acordo com o janelamento 11 no intervalo de tempo de -125,0 a 125,0 ns.
        vetor_derivada_pulso_referencia = np.array([dh_tm125, dh_tm100, dh_tm75, dh_tm50, dh_tm25, dh_t0, dh_tM25, dh_tM50, dh_tM75, dh_tM100, dh_tM125])
        
    # Caso o janelamento seja igual a 13.
    elif n_janelamento == 13:
        
        # Definição do vetor da derivada do pulso de referência de acordo com o janelamento 13 no intervalo de tempo de -150,0 a 150,0 ns.
        vetor_derivada_pulso_referencia = np.array([dh_tm150, dh_tm125, dh_tm100, dh_tm75, dh_tm50, dh_tm25, dh_t0, dh_tM25, dh_tM50, dh_tM75, dh_tM100, dh_tM125, dh_tM150])
        
    # Caso o janelamento seja igual a 15.
    elif n_janelamento == 15:
        
        # Definição do vetor da derivada do pulso de referência de acordo com o janelamento 15 no intervalo de tempo de -175,0 a 175,0 ns.
        vetor_derivada_pulso_referencia = np.array([dh_tm175, dh_tm150, dh_tm125, dh_tm100, dh_tm75, dh_tm50, dh_tm25, dh_t0, dh_tM25, dh_tM50, dh_tM75, dh_tM100, dh_tM125, dh_tM150, dh_tM175])   

    # Caso o janelamento seja igual a 17.
    elif n_janelamento == 17:
        
        # Definição do vetor da derivada do pulso de referência de acordo com o janelamento 17 no intervalo de tempo de -200,0 a 200,0 ns.
        vetor_derivada_pulso_referencia = np.array([dh_tm200, dh_tm175, dh_tm150, dh_tm125, dh_tm100, dh_tm75, dh_tm50, dh_tm25, dh_t0, dh_tM25, dh_tM50, dh_tM75, dh_tM100, dh_tM125, dh_tM150, dh_tM175, dh_tM200]) 
        
    # Caso o janelamento seja igual a 19.
    elif n_janelamento == 19:
        
        # Definição do vetor da derivada do pulso de referência de acordo com o janelamento 19 no intervalo de tempo de -225,0 a 225,0 ns.
        vetor_derivada_pulso_referencia = np.array([dh_tm225, dh_tm200, dh_tm175, dh_tm150, dh_tm125, dh_tm100, dh_tm75, dh_tm50, dh_tm25, dh_t0, dh_tM25, dh_tM50, dh_tM75, dh_tM100, dh_tM125, dh_tM150, dh_tM175, dh_tM200, dh_tM225])     

    # A função retorna o vetor pulso de referência.
    return vetor_derivada_pulso_referencia
    
### --------------------------------------------------------------------------------------------------------------------------------- ###   

### ------------------------------------------ 3) FUNÇÃO PARA A MATRIZ DE COEFICIENTES ---------------------------------------------- ###   

# Definição da função para a construção da matriz de coeficientes.
def matriz_coeficientes(n_janelamento, Matriz_Covariancia, vetor_pulso_referencia, vetor_derivada_pulso_referencia):
    
    # A matriz M1 recebe a matriz de covariância.
    Matriz_M1 = Matriz_Covariancia
    
    # Definição da matriz M2 com colunas extras.
    Matriz_M2 = np.column_stack((-1*vetor_pulso_referencia, -1*vetor_derivada_pulso_referencia))
    
    # Acréscimo de colunas na matriz de covariância para formar a matriz M2.
    Matriz_M1_M2 = np.hstack((Matriz_M1, Matriz_M2))
    
    # Definição do vetor de zeros de tamanho 2.
    vetor_zeros = np.zeros(2)
    
    # Definição do vetor que corresponde a primeira linha extra.
    vetor_primeira_linha_extra = np.concatenate((vetor_pulso_referencia, vetor_zeros))
    
    # Definição do vetor que corresponde a segunda linha extra.
    vetor_segunda_linha_extra = np.concatenate((vetor_derivada_pulso_referencia, vetor_zeros))
    
    # Definição da matriz M3 com as linhas extras.
    Matriz_M3 = np.vstack((vetor_primeira_linha_extra, vetor_segunda_linha_extra))
    
    # Definição da matriz de coeficientes.
    Matriz_Coeficientes = np.vstack((Matriz_M1_M2, Matriz_M3))
    
    # A função retorna a matriz de coeficientes.
    return Matriz_Coeficientes

### --------------------------------------------------------------------------------------------------------------------------------- ###

### --------------------------------------- 4) FUNÇÃO PARA O VETOR DE RESPOSTA ------------------------------------------------------ ###

# Definição da função para a construção do vetor de resposta.
def vetor_resposta(n_janelamento, parametro_desejado):
    
    # Definição da variável n_tamanho.
    n_tamanho = n_janelamento+2
    
    # Definição do vetor de reposta inicialmente de zeros com a quantidade n_tamanho.
    vetor_resposta = np.zeros(n_tamanho)
    
    # Se a variável parâmetro for igual a "amplitude".
    if parametro_desejado == "amplitude":
    
        # Definição do pré-antepenúltimo elemento como um do vetor de resposta.
        vetor_resposta[-2] = 1
        
    # Se a variável parametro for igual a "amplitude_versus_fase".
    elif parametro_desejado == "amplitude_versus_fase":
        
        # Definição do antepenúltimo elemento como um do vetor de resposta.
        vetor_resposta[-1] = 1
    
    # A função retorna o vetor de resposta.
    return vetor_resposta

### --------------------------------------------------------------------------------------------------------------------------------- ###

### ------------------------------------ 5) FUNÇÃO PARA O MÉTODO OF1 OTIMIZADO ------------------------------------------------------ ###

# Definição da função para o método OF1 otimizado.
def metodo_OF1_otimizado(parametro, n_janelamento, Matriz_Pulsos_Sinais_Treino_Janelado, Matriz_Pulsos_Sinais_Teste_Janelado, vetor_parametro_referencia_teste_janelado, valor_minimo_amplitude_processo_fase, vetor_amplitude_referencia_treino_janelado):

    # Criação da lista vazia para armazenar os erros calculados para o parâmetro. 
    lista_erro_estimacao_parametro = []
    
    # A variável Matriz_Covariancia_Ruidos recebe o valor de retorno da função matriz_covariancia.
    Matriz_Covariancia_Ruidos = matriz_covariancia(Matriz_Pulsos_Sinais_Treino_Janelado)
    
    # A variável vetor_h recebe o retorno da função pulso_referencia.
    vetor_h = pulso_referencia(n_janelamento)
    
    # A variável vetor_dh recebe o retorno da função derivada_pulso_referencia.
    vetor_dh = derivada_pulso_referencia(n_janelamento)
    
    # A variável Matriz_Coeficientes recebe o valor de retorno da função matriz_coeficientes.
    Matriz_Coeficientes = matriz_coeficientes(n_janelamento, Matriz_Covariancia_Ruidos, vetor_h, vetor_dh)
    
    # Caso a variável parametro seja igual a "amplitude".
    if parametro == "amplitude" or parametro == "fase_amplitude_estimada":
        
        # A variável vetor_resposta_amplitude recebe o valor de retorno da função vetor_resposta com o parâmetro desejado sendo igual a amplitude.
        vetor_resposta_amplitude = vetor_resposta(n_janelamento, parametro_desejado = "amplitude")
      
        # Cálculo do vetor vetor_incognitas_amplitude como o resultado da equação matricial Ax = b.
        vetor_incognitas_amplitude = np.linalg.solve(Matriz_Coeficientes, vetor_resposta_amplitude)
    
        # Definição do vetor de pesos da amplitude a partir do vetor de incógnitas.
        vetor_pesos_amplitude_OF1_otimizado = vetor_incognitas_amplitude[:-2]
        
        # Definição do vetor com os multiplicadores de Lagrange do vetor de incógnitas da amplitude.
        vetor_multiplicadores_Lagrange_amplitude = vetor_incognitas_amplitude[-2:]  
    
    # Caso a variável parametro seja igual a "fase_amplitude_estimada" ou "fase_amplitude_referencia".
    if parametro == "fase_amplitude_estimada" or parametro == "fase_amplitude_referencia":
        
        # A variável vetor_resposta_fase recebe o valor de retorno da função vetor_resposta com o parâmetro desejado sendo igual a amplitude versus a fase.
        vetor_resposta_fase = vetor_resposta(n_janelamento, parametro_desejado = "amplitude_versus_fase")
    
        # Cálculo do vetor_incognitas_amplitude_versus_fase como o resultado da equação matricial Ax = b.
        vetor_incognitas_amplitude_versus_fase = np.linalg.solve(Matriz_Coeficientes, vetor_resposta_fase)
    
        # Definição do vetor de pesos da amplitude versus fase a partir do vetor de incógnitas.
        vetor_pesos_amplitude_versus_fase_OF1_otimizado = vetor_incognitas_amplitude_versus_fase[:-2]
    
        # Definição do vetor com os multiplicadores de Lagrange do vetor de incógnitas da amplitude versus fase.
        vetor_multiplicadores_Lagrange_amplitude_versus_fase = vetor_incognitas_amplitude_versus_fase[-2:]
    
    # Caso a variável parametro seja igual a "pedestal".
    if parametro == "pedestal": 
        
        # A variável vetor_resposta_pedestal recebe o valor de retorno da função vetor_resposta com o parâmetro desejado sendo igual ao pedestal.
        vetor_resposta_pedestal = vetor_resposta(n_janelamento, parametro_desejado = "pedestal")
        
        # Cálculo do vetor_incognitas_pedestal como o resultado da equação matricial Ax = b.
        vetor_incognitas_pedestal = np.linalg.solve(Matriz_Coeficientes, vetor_resposta_pedestal)
    
        # Definição do vetor de pesos do pedestal a partir do vetor de incógnitas.
        vetor_pesos_pedestal_OF1_otimizado = vetor_incognitas_pedestal[:-2]
    
        # Definição do vetor com os multiplicadores de Lagrange do vetor de incógnitas do pedestal.
        vetor_multiplicadores_Lagrange_pedestal = vetor_incognitas_pedestal[-2:]
    
    # Para o índice de zero até o número de linhas da matriz Matriz_Pulsos_Sinais_Teste_Janelado.
    for indice_linha in range(len(Matriz_Pulsos_Sinais_Teste_Janelado)):
        
        # O vetor vetor_pulsos_sinais corresponde a linha de índice indice_linha da matriz Matriz_Pulsos_Sinais_Teste_Janelado.    
        vetor_pulsos_sinais_teste = Matriz_Pulsos_Sinais_Teste_Janelado[indice_linha]
        
        # Caso a variável parametro seja igual a "amplitude".
        if parametro == "amplitude":
            
            # Cálculo da amplitude estimada pelo método OF1 otimizado.
            valor_parametro_estimado = np.dot(vetor_pesos_amplitude_OF1_otimizado, vetor_pulsos_sinais_teste)
        
        # Caso a variável parametro seja igual a "fase_amplitude_estimada".
        elif parametro == "fase_amplitude_estimada":
            
            # Cálculo da amplitude estimada pelo método OF1 otimizado.
            valor_amplitude_estimada = np.dot(vetor_pesos_amplitude_OF1_otimizado, vetor_pulsos_sinais_teste) 
               
            # caso o valor de valor_amplitude_estimada for maior que o valor valor_minimo_amplitude_processo_fase.
            if valor_amplitude_estimada >= valor_minimo_amplitude_processo_fase:
                
                # Cálculo do termo da amplitude versus a fase estimada pelo método OF1 otimizado.
                valor_amplitude_versus_fase_estimada = np.dot(vetor_pesos_amplitude_versus_fase_OF1_otimizado, vetor_pulsos_sinais_teste)
                
                # A variável valor_parametro_estimado é calculada pela divisão entre os valores do valor_amplitude_versus_fase_estimada pelo valor_amplitude_estimada.
                valor_parametro_estimado = valor_amplitude_versus_fase_estimada / valor_amplitude_estimada
            
            # caso contrário.    
            else:
                
                # Segue para a próxima iteração.
                continue
            
        # Caso a variável parâmetro seja igual a "fase_amplitude_referencia".
        elif parametro == "fase_amplitude_referencia":
            
            # O valor_amplitude_referencia_treino é o elemento de índice indice_linha do vetor vetor_amplitude_referencia_treino_janelado.
            valor_amplitude_referencia_treino = vetor_amplitude_referencia_treino_janelado[indice_linha]
            
            # caso o valor de valor_amplitude_referencia_treino for maior que o valor_minimo_amplitude_processo_fase.
            if valor_amplitude_referencia_treino >= valor_minimo_amplitude_processo_fase:
                
                # Cálculo do termo da amplitude versus a fase estimada pelo método OF1 otimizado.
                valor_amplitude_versus_fase_estimada = np.dot(vetor_pesos_amplitude_versus_fase_OF1_otimizado, vetor_pulsos_sinais_teste)
                
                # A variável valor_parametro_estimado é calculada pela divisão entre os valores do valor_amplitude_versus_fase_estimada pelo valor_amplitude_referencia_treino.
                valor_parametro_estimado = valor_amplitude_versus_fase_estimada / valor_amplitude_referencia_treino
            
            # Caso contrário.         
            else:
                
                # Segue para a próxima iteração.
                continue
            
        # Caso a variável parametro seja igual a "pedestal".
        elif parametro == "pedestal":
        
            # Cálculo do pedestal estimado pelo método OF1 otimizado.
            valor_parametro_estimado = np.dot(vetor_pesos_pedestal_OF1_otimizado, vetor_pulsos_sinais_teste)
        
        # o valor_parametro_referencia_teste é o elemento de índice indice_linha do vetor vetor_parametro_referencia_teste_janelado.
        valor_parametro_referencia_teste = vetor_parametro_referencia_teste_janelado[indice_linha]
            
        # Cálculo do erro de estimação do parâmetro.
        erro_estimacao = valor_parametro_referencia_teste-valor_parametro_estimado
            
        # O elemento erro_amplitude é adicionado na lista correspondente.    
        lista_erro_estimacao_parametro.append(erro_estimacao)

    # A função retorna a lista lista_erro_estimacao_parametro.
    return lista_erro_estimacao_parametro
 
### --------------------------------------------------------------------------------------------------------------------------------- ###