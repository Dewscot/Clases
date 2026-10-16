import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

# 1. Lectura de datos y parametros de la experiencia
datos = np.loadtxt("datos_gravedad.txt", skiprows=2)
angulo = datos[:, 0]
xf_cm = datos[:, 2]
u_xf_cm = datos[:, 3]             # Incluye el reajuste del tope: 0.1 cm
t = datos[:, 4]                  # Tiempos usados, principalmente promedios
x0_cm = 20.5                     # Referencia medida una sola vez
division_regla_cm = 0.1
u_x0_cm = division_regla_cm / 2
division_angular_grados = 1.0
u_theta_grados = division_angular_grados / 2
u_t = 0.30                       # Estimacion personal del cronometraje (s)

# 2. Conversiones: longitudes en metros y angulos en radianes
d = (xf_cm - x0_cm) / 100
u_xf = u_xf_cm / 100
u_x0 = u_x0_cm / 100
theta = np.deg2rad(angulo)
u_theta = np.deg2rad(u_theta_grados)

# 3. Calculos fisicos: carrito desde reposo y modelo ideal
X = np.sin(theta)
a = 2 * d / t**2
g_i = a / X

# 4. Propagacion por derivadas parciales, con variables independientes
u_d = np.sqrt(u_xf**2 + u_x0**2)
u_a = a * np.sqrt((u_d / d)**2 + (2 * u_t / t)**2)
u_g_i = g_i * np.sqrt((u_a / a)**2 + (u_theta / np.tan(theta))**2)
u_X = np.abs(np.cos(theta)) * u_theta

# 5. Minimos cuadrados ordinarios: a = g*X, con intercepto cero
g = np.sum(X * a) / np.sum(X**2)
diferencia_relativa = 100 * abs(g - 9.81) / 9.81
print(f"g del ajuste = {g:.5f} m/s^2; incertidumbre de pendiente no calculada")
print(f"Diferencia nominal respecto de 9.81 m/s^2: {diferencia_relativa:.2f}%")
print(f"u_d = {u_d[0]:.7f} m; u_theta = {u_theta_grados:g} grados; u_t = {u_t:.2f} s estimada")
for i in range(len(t)):
    print(f"{angulo[i]:g} grados, d={d[i]:.3f} m: a={a[i]:.4f} +/- {u_a[i]:.4f} m/s^2")
    print(f"    g_i={g_i[i]:.4f} +/- {u_g_i[i]:.4f} m/s^2")

# 6. Grafica: barras de error y recta del ajuste
X_recta = np.linspace(0, 1.08 * X.max(), 100)
plt.figure(figsize=(4, 2.8))
plt.errorbar(X, a, xerr=u_X, yerr=u_a, fmt="o", color="black",
             capsize=3, label="Mediciones")
plt.plot(X_recta, g * X_recta, label=f"Ajuste: g = {g:.2f} m/s$^2$")
plt.xlabel(r"$\sin\theta$")
plt.ylabel(r"Aceleracion $a$ (m/s$^2$)")
plt.grid(True, alpha=0.25)
plt.legend(fontsize=8)
plt.tight_layout()
plt.savefig("ajuste_gravedad.pdf", bbox_inches="tight")
plt.show()
