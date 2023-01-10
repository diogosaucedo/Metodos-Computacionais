import pandas
import numpy as np

dados = pandas.read_csv('dados.csv',sep=';')

#print(dados.std())
#print(dados.loc[:,'LSAT'].std())

#print(dados['LSAT'].corr(dados['GPA']))
#print(dados.corr())

B=200
n=dados.shape[0]
R=[]

for b in range(B):
	idx = np.random.randint(0,n,n)
	LSAT=dados.loc[idx,'LSAT']
	GPA=dados.loc[idx,'GPA']
	R.append(LSAT.corr(GPA))


print(dados['LSAT'].corr(dados['GPA']))
print(np.mean(R))
print(np.std(R))

