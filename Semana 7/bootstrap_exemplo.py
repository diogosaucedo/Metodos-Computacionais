import pandas
import numpy as np

dados = pandas.read_csv('exemplo.csv',sep=';')

B=10
n=dados.shape[0]
R=[]

for b in range(B):
	idx = np.random.randint(0,n,n)
	X=dados.loc[idx,'X']
	R.append(X.mean())


print(dados['X'].mean())
print(dados['X'].std())
print(np.mean(R))
print(np.std(R))

