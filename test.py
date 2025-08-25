numero = int(input("Digite um número inteiro positivo: "))
def soma_anteriores(numero):
  if not isinstance(numero, int) or numero <= 0:
    return "Por favor, insira um número inteiro positivo."
  
  soma = 0
  for i in range(1, numero):
    soma += i
  return soma


resultado = soma_anteriores(numero)
numero = str(resultado)
print(numero[0])
print(f"A soma dos números anteriores a {numero} é: {resultado}") # Saída: A soma dos números anteriores a 5 é: 10