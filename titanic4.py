#atividade 04: gráfico de dispersão da idade pela tarifa
import pandas as pd
import matplotlib.pyplot as plt
#lê o arquivo de dados e armazena ele em "df"
df = pd.read_csv('dados.csv')

#transforma as colunas 'age' e 'fare' em string (estava dando erro de value se nao fosse em str)
df['age'] = df['age'].astype(str)
df['fare'] = df['fare'].astype(str)

#cria as variaveis trazendo as colunas 'age' e 'fare' para posteriormente colocar no scatter
age = df['age']
fare = df['fare']

#determina o tamanho da figura (o maximo possivel que cabe pois são muitos dados)
plt.figure(figsize=(100,100))

#cria o grafico de dispersão em si com 'age' e 'fare'
plt.scatter (age, fare)

#título do grafico
plt.title('Gráfico de dispersão de idade pela tarifa')
#eixo x
plt.xlabel("Idade")
#eixo y
plt.ylabel("Tarifa")

#mostra o grafico
plt.show() 
