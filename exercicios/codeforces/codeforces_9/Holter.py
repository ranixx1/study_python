N = int(input())
measurements = [int(input()) for _ in range(N)]

average = sum(measurements) // N

lower_bound = int(average * 0.9)
upper_bound = int(average * 1.1)

count = sum(1 for b in measurements if b < lower_bound or b > upper_bound)

print(average)
print(count)