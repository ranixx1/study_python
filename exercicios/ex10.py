seg=int(input("Digite a quantidade de segundos:"))

horas= int(seg//3600)
resto = int(seg%3600)
minutos=int(seg//60)
segundos = int(resto%60)
print(f'tempo em horas:{horas}')
print(f'tempo em minutos:{minutos}')
print(f'tempo em segundos:{seg}')

print(f'hora: {horas:02d}:{minutos:02d}:{segundos:02d}') #02d pega dois digitos