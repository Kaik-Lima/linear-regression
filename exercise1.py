import numpy as np
import matplotlib.pyplot as plt

x, y = np.load('combustivel_e_temperatura.npy')

X = np.vstack((np.ones(len(x)), x)).T
betas, res, _, _ = np.linalg.lstsq(X, y, rcond=None)
beta0, beta1 = betas
residuo = res[0]

yprev = beta1 * x + beta0

# R^2
ymedio = np.mean(y)# Calculando a média do y
tss = np.sum((y - ymedio)**2)
rss = np.sum((y - yprev)**2)
r2 = 1 - rss / tss

print(f'Intercepto = {beta0}\nCoeficiente angular = {beta1}\nR^2 = {r2:.5f}\nResíduo de Lstsq = {residuo}\nResíduo Calculado = {res}')

plt.scatter(x, y, label='Dados Reais')
plt.plot(x, yprev, color='lightgreen', label='Estimado')
plt.xlabel('Litros')
plt.ylabel('Temperatura')
plt.title('Estudo do Desempenho de um Motor de Combustão Interna')
plt.legend()
plt.grid()
plt.show()


# Faça uma previsão da temperatura do motor para uma quantidade de combustível injetado de 8 litros por minuto usando o modelo. (Resposta: 121.5°C)
prev = beta0 + beta1 * 8
print(f'Se a quantidade de combústivel injetado fosse 8 litros o motor teria a temperatura de {np.around([prev], 1)}º graus.')