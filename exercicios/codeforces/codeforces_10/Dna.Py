dna = input()
max_repetition = 1
current_repetition = 1

for i in range(1, len(dna)):
    if dna[i] == dna[i-1]:
        current_repetition += 1
    else:
        max_repetition = max(max_repetition, current_repetition)
        current_repetition = 1
    
max_repetition = max(max_repetition, current_repetition)
        
print(max_repetition)