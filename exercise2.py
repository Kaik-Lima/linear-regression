import numpy as np
import matplotlib.pyplot as plt

dados = np.genfromtxt('dados_descarbonizacao.csv', delimiter=',', skip_header=1).T

x = dados[:4]
y = dados[4]

x = x.T

x = np.hstack((np.ones((len(x), 1)), x))

betas, res, _, _ = np.linalg.lstsq(x, y, rcond=None)

y_medio = np.mean(y)

tss = sum((y - y_medio)**2)
r2 = 1 - (res / tss)

y_pred = x @ betas

id = np.arange(1, len(y)+1)
print(f'{"ID":<3} {"Real":>5} {"Predito":>5} {"Diferença":>6}')

for ID, real, pred in zip(id, y, y_pred): print(f'\033[1m{ID:<3}\033[0m {real:>5} {np.round(pred, 2):>5} {100*(pred-real)/real:>8.2f}')

plt.scatter(id, y, c='b', label='Real')
plt.scatter(id, y_pred, c='g', label='Predito')
plt.xlabel('ID')
plt.ylabel('Emissão de Gases')
plt.title('Efeitos Descarbonização')
plt.grid()
plt.legend()
plt.show()
