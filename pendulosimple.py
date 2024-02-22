import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Tus datos
tiempo = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
amplitud = np.array([13, 8.5, 6, 5, 4, 3.5, 3, 2.3, 2.1, 1.9, 1.7, 1.5, 1.4, 1.2])

# Definición de la función exponencial
def func(t, A0, zeta, omega_n):
    return A0 * np.exp(-zeta * omega_n * t)

# Cálculo de la frecuencia natural
L = 0.6  # longitud del péndulo en metros
g = 9.81  # aceleración debido a la gravedad en m/s^2
omega_n = np.sqrt(g / L)

# Ajuste de curva
popt, pcov = curve_fit(lambda t, A0, zeta: func(t, A0, zeta, omega_n), tiempo, amplitud)

A0, zeta = popt
print(f"Amplitud inicial (A0): {A0}")
print(f"Factor de amortiguamiento (zeta): {zeta}")

# Generación de la gráfica
t_fit = np.linspace(tiempo.min(), tiempo.max(), 100)
A_fit = func(t_fit, A0, zeta, omega_n)

plt.figure(figsize=(10, 6))
plt.plot(tiempo, amplitud, 'o', label='Datos')
plt.plot(t_fit, A_fit, '-', label='Ajuste')
plt.xlabel('Tiempo (min)')
plt.ylabel('Amplitud (cm)')
plt.legend()
plt.grid(True)
plt.show()