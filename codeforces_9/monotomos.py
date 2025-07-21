N = int(input())
s = input()

total_a_em_monotomas = 0
i = 0

while i < N:
    current_char = s[i]
    j = i
    
    while j + 1 < N and s[j + 1] == current_char:
        j += 1
    
    monotoma_length = j - i + 1
    
    if monotoma_length >= 2:
        if current_char == 'a':
            total_a_em_monotomas += monotoma_length
            
    i = j + 1 

print(total_a_em_monotomas)