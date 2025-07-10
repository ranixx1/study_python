#No planeta Alpha vive a criatura Blobs, que come precisamente  (metade) de seu suprimento de comida disponível todos os dias. Escreva um programa que leia a capacidade inicial de suprimento de comida C, em Kg, e calcule quantos dias passarão antes que Blobs coma todo esse suprimento até restar um quilo ou menos.

c = int(input())  # Número de casos
for _ in range(c):
    qtd = float(input())
    dias = 0
    while qtd > 1:
        qtd /= 2
        dias += 1
    print(f"{dias} dias")
