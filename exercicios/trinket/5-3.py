temperatura_para_conversao = input()

pega_ultima_letra = temperatura_para_conversao[-1]
valor_numerico = temperatura_para_conversao[:-1]
valor_numerico = float(valor_numerico)


if pega_ultima_letra == "F":
    c = (valor_numerico - 32) / 1.8
    f = valor_numerico
    k = c + 273.15

elif pega_ultima_letra == "K":
    c = valor_numerico - 273.15
    f = c * 1.8 + 32
    k = valor_numerico

elif pega_ultima_letra == "C":
    c = valor_numerico
    f = c * 1.8 + 32
    k = c + 273.15

print(f"Temperatura em Celsius: {c:.2f} °C")
print(f"Temperatura em Fahrenheit: {f:.2f} °F")
print(f"Temperatura em Kelvin: {k:.2f} K")
