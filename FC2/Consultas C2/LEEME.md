# FC2 — material de consulta C2 (27 de noviembre de 2026)

Copia revisada de seis notebooks de `FC2.zip`, basada en las presentaciones 03-ceros, 04-integrales y 05-interpolación (hasta Vandermonde). No se modificó GitHub, ni se incluyeron soluciones de las tareas. Confirma que el docente permita utilizar material de consulta preparado con asistencia de IA durante el certamen; la autorización de llevar código propio no implica necesariamente esa autorización. Declara el uso cuando corresponda según el syllabus.

## Cómo usarlo

1. Extrae el ZIP en una carpeta separada y conserva los originales.
2. Abre el notebook que corresponda y selecciona el kernel de tu entorno `general`.
3. Ejecuta desde arriba (Run All). Para un problema nuevo copia los imports y la función del método; adapta los parámetros y el ejemplo, no los resultados guardados.
4. Comprueba el resultado con una solución conocida, residuo, refinamiento de malla o evaluación en los nodos según el método.

No hay paquetes nuevos: NumPy y Matplotlib; SciPy solo para evaluar la base Legendre. `datos-01.txt` es el archivo original usado en Vandermonde. Mantén el notebook y los datos juntos.

## Índice (por prioridad de estudio)

| Notebook | Qué copiar / adaptar | Cambios principales |
|---|---|---|
| Integrales2.ipynb | `Simpson(f,a,b,N)`; N par | Se eliminan dependencias de variables globales y arange; ejemplos con límites variables, integral iterada, valores complejos y estimación de error por refinamiento. |
| Integrales.ipynb | `rectangulo`, `punto_medio`, `trapezoide`, `trapezoide_datos` | N explícito; nodos con linspace; no se evalúan dos veces los interiores en trapecio; ejemplo con datos no uniformes. |
| polinomios_lagradge_clase_fail.ipynb | `lagrange(z,x,y)` | Se mantiene doble ciclo; valida nodos distintos, permite escalares/arreglos, agrega gráfico y comprobación. |
| Matriz_de_vandermonde.ipynb | `vandermonde(x)`, `matriz_base(x,phi)`, `evaluar(z,A,phi)` | Corrige orden `phi(x,j)`; coeficientes de grado variable; base monomial, coseno original y Legendre; residuo, condición y error en malla. Se omite el bloque spline de esta copia. |
| Soluciones_de_ecuaciones.ipynb | `biseccion`, `posicion_falsa`, `newton`, `secante`, `intervalos_raices` | Métodos independientes, criterios de parada y máximo de iteraciones; posición falsa actualiza el extremo adecuado, bisección comprueba signos; búsqueda de varios cambios de signo. |
| Sistema_de_ecuaciones_no_lineales.ipynb | `newton_sistema(F,J,u0)` | Signo de J[1,1] corregido, solve sin inversa, residuo y chequeo opcional con diferencias centrales. |

## Decidir rápido

- Integrar una función suave: Simpson si hay N par; trapecio para datos no uniformes. En integrales iteradas fija una variable mientras integras la otra.
- Interpolar datos: Lagrange para evaluar directamente, Vandermonde para obtener coeficientes; cambia phi según la base pedida. Nodos distintos en la base monomial.
- Hallar un cero real: bisección si hay cambio de signo; Newton si tienes derivada y semilla razonable; secante si no tienes derivada; posición falsa conserva intervalo.
- Resolver F(u)=0: Newton vectorial y jacobiano. Resolver Ax=b: solve directamente.

## Alcance y verificación

Se ejecutaron los seis notebooks con kernel Python 3 en el entorno de revisión, incluyendo sus comprobaciones `assert`. No se verificó el entorno local de Windows ni la versión remota de FC2 (la búsqueda en GitHub no encontró el repositorio). No se modificaron los notebooks de EDO, derivadas, NumPy ni splines; los dos primeros se consideran repaso de C1, y splines están explícitamente excluidos. El comienzo exacto del temario C2 no está confirmado. Cuadratura de Gauss, Romberg, optimización y ajuste por mínimos cuadrados no se desarrollan en esta copia de consulta prioritaria.
