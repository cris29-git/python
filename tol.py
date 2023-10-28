def bisection(f, a, b, tolerance, max_iterations=100):
    if f(a) * f(b) >= 0:
        print("La función no cumple con los requisitos de cambio de signo en el intervalo [a, b].")
        return None

    iteration = 0
    while iteration < max_iterations:
        c = (a + b) / 2.0
        if f(c) == 0 or (b - a) / 2.0 < tolerance:
            return c  # Hemos encontrado la raíz exacta o cumplido con la tolerancia
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteration += 1

    print("Se alcanzó el número máximo de iteraciones sin converger.")
    return (a + b) / 2.0

# Define la función f(x) que deseas encontrar la raíz
def f(x):
    return x**2 - 4

# Intervalo [a, b] y tolerancia
a = 1.0
b = 3.0
tolerance = 0.001

# Encuentra la raíz utilizando la función de bisección
root = bisection(f, a, b, tolerance)

if root is not None:
    print(f"La raíz aproximada es {root:.5f}")
