import pandas as pd 

#atividade 01: ajustar as idades que nao sao validas ou estão vazias para a moda da amostra e gravar a saida em um arquivo
#lê os arquivos e os armazena em 'df'
df = pd.read_csv('dados.csv')

#usando o mode() do pandas pra calcular a moda das idades e substituir no arquivo
moda_age = df['age'].mode()[0]

#metodo de substituir no arquivo os valores vazios e invalidos da coluna 'age' pelo valor da moda
df['age'].fillna(moda_age, inplace = True) 

#criando e gravando os dados em um arquivo
f = open("resposta01.txt", "a")
#escrevendo o conteudo do arquivo 'df' inteiro no arquivo criado 'resposta01.txt'
f.write(df.to_string())
#fechando o arquivo
f.close()
