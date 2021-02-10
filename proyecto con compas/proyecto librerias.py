# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:21:21 2021

@author: Iván Sarmiento 
"""

import numpy as np
from matplotlib import pyplot as plt

"""La pérdida de peso de una persona que sigue una determinada dieta, 
en el transcurso del tiempo, viene dada por la siguiente tabla:
Tiempo (meses) 1 2 3 4 5 6 
Pérdida de Peso (kg) 9 7.5 5.2 4.6 3.1 2
Con el objetivo de estudiar la pérdida de peso en función del tiempo, 
ajuste a dichos datos una recta.¿Qué pérdida de
peso se tenía cuando habían pasado 2 meses y medio?"""

# Datos experimentales
x = np.array([ 1,  2,  3,  4,  5, 6 ])
y = np.array([ 9,  7.5,  5.2,  4.6,  3.1,  2 ])

# Ajuste a una recta (polinomio de grado 1, y=mx+b)
p = np.polyfit(x, y, 1)

print(p)
# imprime [ -1.3942...  10.113... ]

#GRAFICAR LA RECTA DE MÍNIMOS CUADRADOS 

# Valores de y calculados del ajuste
y_ajuste = p[0]*x + p[1]

# Dibujamos los datos experimentales
p_datos, = plt.plot(x, y, 'b.')
# Dibujamos la recta de ajuste
p_ajuste, = plt.plot(x, y_ajuste, 'r-')

plt.title('Ajuste lineal por mínimos cuadrados')

plt.xlabel('Tiempo (meses)')
plt.ylabel('Pérdida de peso (kg)')

plt.legend(('Datos experimentales', 'Ajuste lineal'), loc="upper right")
plt.show()