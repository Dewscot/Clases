import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

# Datos: m, dm en g; x, dx en cm
datos = np.genfromtxt("datos_resorte.txt", skip_header=2)

m_g   = datos[:, 0]
dm_g  = datos[:, 1]
x_cm  = datos[:, 2]
dx_cm = datos[:, 3]

# Conversión a unidades SI
m  = m_g / 1000
dm = dm_g / 1000
x  = x_cm / 100
dx = dx_cm / 100

g = 9.81  # m/s^2

# Ajuste por mínimos cuadrados: Delta x = a1*m + a0
a1, a0 = np.polyfit(m, x, 1)

# Equilibrio en reposo: mg = k*Delta x
# Entonces a1 = g/k, y k = g/a1
k = g / a1

# Valores obtenidos del ajuste
print(f"a0 = {a0:.4f} m")
print(f"a1 = {a1:.4f} m/kg")
print(f"k = {k:.2f} N/m")

# Propagación de incertidumbre para k_i = m_i*g/x_i
k_i = m*g/x
dk_i = k_i*np.sqrt((dm/m)**2 + (dx/x)**2)

# Medición que se quiere revisar
i = 11

print(f"k_i = {k_i[i]:.2f} ± {dk_i[i]:.2f} N/m")

# Plot con barras de error y ajuste lineal
m_recta = np.linspace(0, 1.03*np.max(m), 250)

plt.errorbar( m, x, xerr=dm, yerr=dx, fmt="o", capsize=3, label="Mediciones")

plt.plot(m_recta, a1*m_recta + a0, label="Ajuste lineal")

plt.xlabel("Masa, m (kg)")
plt.ylabel("Elongación, Δx (m)")
plt.grid(True, alpha=0.25)
plt.legend()

plt.tight_layout()
plt.savefig("ajuste_resorte.pdf", bbox_inches="tight")
plt.show()