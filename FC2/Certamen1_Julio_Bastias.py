import numpy as np
import matplotlib.pyplot as plt

#Problema 2


#Primero tenemos que reducir el nivel de la EDO de segundo orden a un sistema de EDOS de primero orden
#Lo cual nos deja y'(t)=v(t) ---> v'(t)=-w**2y(t)-g = y''(t)
#u = (y,v) arreglo de la posicion y velocidad

def du(u,w,g):   #du derivada de u (arreglo de la velocidad, aceleracion)
    x, v =u
    return np.array([v, (-g)])



w = 1 #Constante
g = 9.8 #Gravedad de la tierra
Npuntos = 1000 #cantidad de puntos que uno quiere, incluyendo al inicio 
u = np.zeros([Npuntos,2]) #Arreglo  para remplazarlo en cada posicion el valor que calculemos, posicion y velocidad
x_0 = 0 #Posicion inicial, reposo
v_0 = 10 #Velocidad inicial
V = 0.1 #constante aire

u[0,0]= x_0 #Posicion inicial, reposo
u[0,1]= v_0 #Velocidad inicial
h = 0.00002 #cuanto nos estamos acercando en la derivada
for n in range(Npuntos-1): 
    u[n+1]= u[n] + h*du(u[n],w,g)




#Problema 3
#Realiza biseccion a P_4 en 0<x<1 con 6 cifras decimales

def f(x):
    
    return (35*x**4)/8-(15*x**2)/4+3/8
#Grafica de la funcion
x_P_4 = np.linspace(-10,10,100)
y_P_4 = f(x_P_4)
plt.scatter(x_P_4,y_P_4)
#plt.show()

a, b = 0, 1
tolerancia = 1e-6
error = 0.5*(b-a)

while error > tolerancia:
    c = 0.5*(a+b)

    if abs(f(c)) < tolerancia:
        break

    if f(a)*f(c) < 0:
        b = c
    else:
        a = c

    error = 0.5*(b-a)

print('valor de la bissecion', c)
