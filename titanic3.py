#atividade 3: gráfico da pizza
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#lê os arquivos e os armazena em 'df'
df = pd.read_csv('dados.csv')

#cria as variaveis de 'naosob' (não sobreviventes) para 0 e 'sob' (sobreviventes) para 1
naosob = 0
sob = 1

#cria uma list 'vetNumeros' que traz a coluna 'survived' do arquivo em 'df'
vetNumeros = df['survived']

#cria um for para os elementos de 'survived'
for item in vetNumeros:
    #verifica se 0 é true para nao sobrevivente
    if item ==0:
        #true adiciona o valor de 'naosob'
        naosob += 1
    else:
        #se nao for 'naosob' adiciona o valor de 'sob'
        sob +=1

#cria uma lista dos dados com os valores de sobreviventes e nao sobreviventes 
dados = [naosob,sob]

#cria o grafico de pizza com a lista dos dados
#'autopct' adiciona a porcentagem das fatias da pizza e 'labels' determina o nome de cada fatia
plt.pie(dados,autopct ='%1.1f%%', labels= ['não sobreviventes','sobreviventes'])

#titulo do grafico
plt.title('Gráfico de pizza de sobreviventes e não sobreviventes')
#mostra o grafico
plt.show()