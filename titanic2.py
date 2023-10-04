#atividade 2: apresentar no terminal o somatório de male e female
import pandas as pd

#lê os arquivos e os armazena em 'df'
df = pd.read_csv('dados.csv')

#criei uma variavel pra pegar os valores de sex (female e male) do arquivo e fazer a contagem de cada um
#o argumento 'value_counts()' conta quantas vezes o valor unico que aparece na coluna 'sex'
somatorio_sex = df['sex'].value_counts()

#mostra no terminal o resultado
print(somatorio_sex)
