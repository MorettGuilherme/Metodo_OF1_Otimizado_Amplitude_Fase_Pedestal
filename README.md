A segunda versão do método linear Filtro Ótimo (Optimal Filtering - OF2) tem a finalidade de estimar os parâmetros da amplitude, fase e pedestal por meio da resolução de uma equação matricial (Ax = b) que advém do processo de otimização dos multiplicadores de Lagrange. Em sua versão dita "Otimizada", a matriz de covariância é calculada a partir dos dados de ruídos.
A matriz dos coeficientes contém em seu interior, a matriz de covariância, além dos pulsos de referência e suas derivadas. O vetor de respostas é composto em maioria por zeros,no entanto o único elemento um presente varia de posição de acordo com o parâmetro desejado. O vetor de incógnitas contém os pesos obtidos pelo método OF2 otimizado e também os multiplicadores de Lagrange que não são empregados no processo.
Obs.: os resultados demostram que o último janelamento adotado é o ideal para a amplitude visto que o valor do desvio padrão não se estabilizou a partir de uma certa quantidade. Por outro lado, a fase pela amplitude estimada o melhor é o 17. Novamente, a fase pela amplitude de referência e o pedestal, o janelamento ótimo adotado foi o 19.

A seguir são listadas as pastas e também os arquivos contidos nesse repositório, assim como suas respectivas funções:

1. Dados_Estatisticos_OF2_Otimizado_amplitude_OC
  * Essa pasta contém arquivos para cada um dos janelamentos com os valores das ocupações e médias, variâncias e desvios padrão associados para o erro de estimação da amplitude.

2. Dados_Estatisticos_OF2_Otimizado_fase_amplitude_estimada_OC
  * Essa pasta contém arquivos para cada um dos janelamentos com os valores das ocupações e médias, variâncias e desvios padrão associados para o erro de estimação da fase, por meio da amplitude estimada.

3. Dados_Estatisticos_OF2_Otimizado_fase_amplitude_referencia_OC
  * Essa pasta contém arquivos para cada um dos janelamentos com os valores das ocupações e médias, variâncias e desvios padrão associados para o erro de estimação da fase, por meio da amplitude de referência.
  
4. Dados_Estatisticos_OF2_Otimizado_pedestal_OC
  * Essa pasta contém arquivos para cada um dos janelamento com os valores das ocupações e médias, variâncias e desvios padrão associados para o erro de estimação do pedestal.

5. Dados_Ocupacoes_Free_Running
  * Essa pasta contém arquivos com os dados para cada uma das ocupações referentes ao pulso de sinal, amplitude de referência, fase de referência e ruído eletrônico computados a cada 25 ns.
  
6. K_Fold_amplitude_DP_Dados_Estatisticos_OF2_Otimizado_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão dos desvios padrão dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

7. K_Fold_amplitude_DP_Desempenho_OF2_Otimizado_OC
  * Essa pasta contém um arquivo com os dados da análise estatística do desvio padrão do erro de estimação da amplitude para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

8. K_Fold_amplitude_EME_Desempenho_OF2_Otimizado_OC
  * Essa pasta contém um arquivo com os dados da análise do erro médio de estimação (EME) da amplitude para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

9. K_Fold_amplitude_MAE_Desempenho_OF2_Otimizado_OC
  * Essa pasta contém um arquivo com os dados da análise do erro médio absoluto (MAE) da amplitude para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

10. K_Fold_amplitude_media_Dados_Estatisticos_OF2_Otimizado_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

11. K_Fold_amplitude_MSE_Desempenho_OF2_Otimizado_OC
   * Essa pasta contém um arquivo com os dados da análise do erro médio quadrático (MSE) da amplitude para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

12. K_Fold_amplitude_SNR_Desempenho_OF2_Otimizado_OC
   * Essa pasta contém um arquivo com os dados da análise da relação sinal ruído (SNR) da amplitude para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

13. K_Fold_amplitude_var_Dados_Estatisticos_OF2_Otimizado_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das variâncias dos erros de estimação da amplitude calculados pela técnica de validação cruzada K-Fold.

14. K_Fold_fase_amplitude_estimada_DP_Dados_Estatisticos_OF2_Otimizado_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão dos desvios padrão dos erros de estimação da fase pela amplitude estimada calculados pela técnica de validação cruzada K-Fold.

15. K_Fold_fase_amplitude_estimada_DP_Desempenho_OF2_Otimizado_OC
  * Essa pasta contém um arquivo dos dados estatísticos para cada ocupação do desvio padrão para o erro de estimação da fase, por meio da amplitude estimada.

16. K_Fold_fase_amplitude_estimada_EME_Desempenho_OF2_Otimizado_OC
   * Essa pasta contém um arquivo com os dados da análise do erro médio de estimação (EME) da fase pela amplitude estimada para o janelamento ideal 17 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

17. K_Fold_fase_amplitude_estimada_MAE_Desempenho_OF2_Otimizado_OC
   * Essa pasta contém um arquivo com os dados da análise do erro médio absoluto (MAE) da fase pela amplitude estimada para o janelamento ideal 17 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

18. K_Fold_fase_amplitude_estimada_media_Dados_Estatisticos_OF2_Otimizado_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação da fase pela amplitude estimada calculados pela técnica de validação cruzada K-Fold.

19. K_Fold_fase_amplitude_estimada_MSE_Desempenho_OF2_Otimizado_OC
   * Essa pasta contém um arquivo com os dados da análise do erro médio quadrático (MSE) da fase pela amplitude estimada para o janelamento ideal 17 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

20. K_Fold_fase_amplitude_estimada_SNR_Desempenho_OF2_Otimizado_OC
   * Essa pasta contém um arquivo com os dados da análise da relação sinal ruído (SNR) da fase pela amplitude estimada para o janelamento ideal 17 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

21. K_Fold_fase_amplitude_estimada_var_Dados_Estatisticos_OF2_Otimizado_OC
   * Essa pasta contém arquivos para cada uma das ocupações dos dados estatísticos da variância do erro de estimação da fase pela amplitude estimada.

22. K_Fold_fase_amplitude_referencia_DP_Dados_Estatisticos_OF2_Otimizado_OC
  * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão dos desvios padrão dos erros de estimação da fase pela amplitude de referência calculados pela técnica de validação cruzada K-Fold.

23. K_Fold_fase_amplitude_referencia_DP_Desempenho_OF2_Otimizado_OC
  * Essa pasta contém um arquivo dos dados estatísticos para cada ocupação do desvio padrão para o erro de estimação da fase, por meio da amplitude de referência.

24. K_Fold_fase_amplitude_referencia_EME_Desempenho_OF2_Otimizado_OC
   * Essa pasta contém um arquivo com os dados da análise do erro médio de estimação (EME) da fase pela amplitude de referência para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

25. K_Fold_fase_amplitude_referencia_MAE_Desempenho_OF2_Otimizado_OC
   * Essa pasta contém um arquivo com os dados da análise do erro médio absoluto (MAE) da fase pela amplitude de referência para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

26. K_Fold_fase_amplitude_referencia_media_Dados_Estatisticos_OF2_Otimizado_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação da fase pela amplitude de referência calculados pela técnica de validação cruzada K-Fold.

27. K_Fold_fase_amplitude_referencia_MSE_Desempenho_OF2_Otimizado_OC
   * Essa pasta contém um arquivo com os dados da análise do erro médio quadrático (MSE) da fase pela amplitude de referência para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

28. K_Fold_fase_amplitude_referencia_SNR_Desempenho_OF2_Otimizado_OC
   * Essa pasta contém um arquivo com os dados da análise da relação sinal ruído (SNR) da fase pela amplitude de referência para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold para todas as ocupações.

29. K_Fold_fase_amplitude_referencia_var_Dados_Estatisticos_OF2_Otimizado_OC
   * Essa pasta contém arquivos para cada uma das ocupações dos dados estatísticos da variância do erro de estimação da fase pela amplitude de referência.

30. K_Fold_fase_analise_amplitude_minima_estimada_DP_J_19
  * Essa pasta contém os arquivos da análise do desvio padrão do erro de estimação da fase pela amplitude mínima estimada pelo K-Fold das ocupações 10 a 100.

31. K_Fold_fase_analise_amplitude_minima_estimada_media_J_19
  * Essa pasta contém os arquivos da análise da média do erro de estimação da fase pela amplitude mínima estimada pelo K-Fold das ocupações 10 a 100.

32. K_Fold_fase_analise_amplitude_minima_estimada_var_J_19
  * Essa pasta contém os arquivos da análise da variância do erro de estimação da fase pela amplitude mínima estimada pelo K-Fold das ocupações 10 a 100.

33. K_Fold_fase_analise_amplitude_minima_referencia_DP_J_19
  * Essa pasta contém os arquivos da análise do desvio padrão do erro de estimação da fase pela amplitude mínima de referência pelo K-Fold das ocupações 10 a 100.

34. K_Fold_fase_analise_amplitude_minima_referencia_media_J_19
  * Essa pasta contém os arquivos da análise da média do erro de estimação da fase pela amplitude mínima de referencia pelo K-Fold das ocupações 10 a 100.

35. K_Fold_fase_analise_amplitude_minima_referencia_var_J_19
  * Essa pasta contém os arquivos da análise da variância do erro de estimação da fase pela amplitude mínima de referência pelo K-Fold das ocupações 10 a 100.

36. K_Fold_pedestal_DP_Dados_Estatisticos_OF2_Otimizado_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão dos desvios padrão dos erros de estimação do pedestal calculados pela técnica de validação cruzada K-Fold.

37. K_Fold_pedestal_DP_Desempenho_OF2_Otimizado_OC
   * Essa pasta contém arquivos com os dados da análise do desvio padrão do erro estimação para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

38. K_Fold_pedestal_EME_Desempenho_OF2_Otimizado_OC
   * Essa pasta contém arquivos com os dados da análise do erro médio de estimação (EME) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

39. K_Fold_pedestal_MAE_Desempenho_OF2_Otimizado_OC
   * Essa pasta contém arquivos com os dados da análise do erro médio absoluto (MAE) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

40.  K_Fold_pedestal_media_Dados_Estatisticos_OF2_Otimizado_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação do pedestal calculados pela técnica de validação cruzada K-Fold.

41. K_Fold_pedestal_MSE_Desempenho_OF2_Otimizado_OC
   * Essa pasta contém arquivos com os dados da análise do erro médio quadrático (MSE) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

42. K_Fold_pedestal_SNR_Desempenho_OF2_Otimizado_OC
   * Essa pasta contém arquivos com os dados da análise da relação sinal ruído (SNR) para o janelamento ideal 19 calculados pela técnica de validação cruzada K-Fold.

43. K_Fold_pedestal_var_Dados_Estatisticos_OF2_Otimizado_OC
   * Essa pasta contém arquivos para cada uma das ocupações; os valores dos janelamentos com as médias, variâncias e desvios padrão das médias dos erros de estimação do pedestal calculados pela técnica de validação cruzada K-Fold.

44. Resultados_OF2_Otimizado_Amplitude
   * Essa pasta com os gráficos dos dados estatísticos (média, variância e desvio padrão) para o erro de estimação da amplitude pela técnica da validação cruzada K-Fold, assim como os histogramas para cada janelamento e ocupações e a análise do desempenho.

45. Resultados_OF2_Otimizado_Fase_amplitude_Estimada
   * Essa pasta com os gráficos dos dados estatísticos (média, variância e desvio padrão) para o erro de estimação da fase pela amplitude estimada pela técnica da validação cruzada K-Fold, assim como os histogramas para cada janelamento e ocupações e a análise do desempenho.

46. Resultados_OF2_Otimizado_Fase_amplitude_Referencia
   * Essa pasta com os gráficos dos dados estatísticos (média, variância e desvio padrão) para o erro de estimação da fase pela amplitude de referência pela técnica da validação cruzada K-Fold, assim como os histogramas para cada janelamento e ocupações e a análise do desempenho.
   
47. Resultados_OF2_Otimizado_Pedestal
   * Essa pasta com os gráficos dos dados estatísticos (média, variância e desvio padrão) para o erro de estimação do pedestal pela técnica da validação cruzada K-Fold, assim como os histogramas para cada janelamento e ocupações e a análise do desempenho.

48. arquivo_saida_analise_amplitude_minima_fase_OF2_Otimizado.py
   * Instrução para salvar em arquivos os dados estatísticos pela validação cruzada k-Fold para a estimação da fase.
   * Instrução da validação cruzada K-Fold para a análise de como o valor da amplitude mínima adotado influencia no processo de estimação da fase.
   * Instrução principal.

49. arquivo_saida_dados_estatisticos_OF2_Otimizado.py
   * Função para o cálculo dos dados estatísticos do erro de estimação pelo método Optimal Filtering 2 (OF2 Otimizado).
   * Instrução para salvar os dados estatísticos do erro de estimação da amplitude, fase ou pedestal para determinada ocupação em um arquivo de saída.
   * Instrução principal do código.

50. arquivo_saida_desempenho_OF2_Otimizado.py
   * Instrução para salvar em arquivos os dados estatísticos do desempenho do método OF2 Otimizado.
   * Função para o cálculo do desempenho do método OF2 Otimizado pelo Erro Médio de Estimação (EME).
   * Função para o cálculo do desempenho do método OF2 Otimizado pelo Erro Médio Quadrático (Mean Squared Error - MSE).
   * Função para o cálculo do desempenho do método OF2 Otimizado pelo Erro Médio Absoluto (Mean Absolute Error - MAE).
   * Função para o cálculo do desempenho do método OF2 Otimizado pela Relação Sinal-Ruído (Signal-to-Noise Ratio - SNR).
   * Função para o cálculo do desempenho do método OF2 Otimizado pelo desvio padrão (DP).
   * Instrução da validação cruzada K-Fold adaptada para o cálculo do desempenho do método OF2 Otimizado.
   * Instrução principal do código.

51. arquivo_saida_k_fold_OF2_Otimizado.py
   * Instrução para salvar em arquivos os dados estatísticos pela validação cruzada k-Fold.
   * Instrução da validação cruzada K-Fold.
   * Instrução principal do código.

52. grafico_analise_amplitude_minima_fase_OF2_Otimizado.py
   * Função para a leitura dos dados estatísticos da análise erro de estimação da fase para uma dada ocupação pelo método OF2 Otimizado.
   * Instrução para o plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento pelo processo de estimação da fase.
   * Instrução principal do código.
   
53. grafico_dado_estatistico_janelamento_OF2_Otimizado.py
   * Função para a leitura dos dados estatísticos de todas as ocupações para um determinado janelamento.
   * Instrução para o plote do gráfico do dado estatístico ao longo das ocupações para um determinado janelamento.
   * Instrução principal do código.

54. grafico_desempenho_OF2_Otimizado.py
   * Função para a leitura dos dados do desempenho do método OF2 Otimizado de todas as ocupações para o janelamento ideal.
   * Instrução para o plote do gráfico do desempenho do método OF2 Otimizado ao longo das ocupações para o janelamento ideal.
   * Instrução principal do código.

55. grafico_k_fold_OF2_Otimizado.py
   * Função para a leitura dos dados estatísticos da validação cruzada K-Fold.
   * Instrução para a construção do gráfico tipo A da validação cruzada K-Fold.
   * Instrução para a construção do gráfico tipo B da validação cruzada K-Fold.
   * Instrução principal (main) do código.
   
56. histograma_erro_parametro_OF2_Otimizado.py
   * Função para o cálculo da estatística do erro de estimação da amplitude, fase ou pedestal.
   * Instrução para o plote do histograma do tipo A do erro de estimação da amplitude, fase ou pedestal.
   * Instrução para o plote do histograma do tipo B do erro de estimação da amplitude, fase ou pedestal.
   * Instrução principal (main) do código.
   
57. leitura_dados_ocupacao_OF2_Otimizado.py
   * Função para a leitura dos dados de ocupação.
   * Função para a retirada do pedestal dos pulsos de sinais.
   * Função para a construção da matriz dos pulsos de sinais e o vetor do parâmetro de referência.
   * Função para separação em dados de treino e teste.

58. leitura_dados_ruidos_OF2_Otimizado.py
   * Função para a leitura dos dados de ruídos de acordo com a ocupação.
   * Função para a organização dos dados de ruídos de acordo com o janelamento.
   * Função para separação em dados de treino e teste.
   * Função para a construção da matriz de covariância como identidade.

59. metodo_OF2_Otimizado.py
   * Função para a definição do vetor pulso de referência.
   * Função para a definição do vetor da derivada temporal do pulso de referência.
   * Função para o método OF2 Otimizado.
   
IMPORTANTE: os dados das ocupações foram simulados computacionalmente. As características das distribuições são:

* Distribuição amplitude: exponencial com média 100 ADC Count.
* Distribuição Fase: uniforme com números inteiros no intervalo de -5 a 5 ns.
* Pedestal: 30 ADC Count.
* Nível de deformação: 0,01 ADC Count.
* Número de eventos: 2000000.
* Fold: 100.
* Os dados de ruídos para a matriz de covariância foram os mesmos que para os pulsos de sinais.

Obs.: antes da aplicação do método, o valor constante do pedestal foi retirado dos dados referentes aos pulsos de sinais.
O vetor da fase de referência foi multiplicado por 0,5; pois esse valor representa a resolução da fase.