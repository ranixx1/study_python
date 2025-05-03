class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        prev_value = 0

        for char in reversed(s):
            current_value = roman_dict[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
                prev_value = current_value

        return total

if __name__ == "__main__":
    entrada = input("Digite um número romano (ex: MCMXCIV): ").upper().strip()
    sol = Solution()
    try:
        resultado = sol.romanToInt(entrada)
        print(f"Valor inteiro de {entrada} é: {resultado}")
    except KeyError:
        print("Entrada inválida: contém letras que não fazem parte dos números romanos.")
