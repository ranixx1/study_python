def polinomio(coeficientes, x):
    if len(coeficientes) == 1:
        return coeficientes[0]
    return x * polinomio(coeficientes[:-1], x) + coeficientes[-1]
