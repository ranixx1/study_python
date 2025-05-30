input_line = input()
A, B = map(int, input_line.split())
sum_B = (B * (B + 1)) // 2
sum_A_minus_1 = ((A - 1) * A) // 2
result = sum_B - sum_A_minus_1
print(result)