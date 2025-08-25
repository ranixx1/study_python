from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapa = {}
        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in mapa:
                return [mapa[complemento], i]
            mapa[num] = i

entrada_numeros = input("Digite os números separados por vírgula (ex: 2,7,11,15): ")
alvo = int(input("Digite o valor alvo: "))
nums = list(map(int, entrada_numeros.split(",")))
sol = Solution()
resultado = sol.twoSum(nums, alvo)
print("Índices encontrados:", resultado)