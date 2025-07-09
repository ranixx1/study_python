# H. Loop musical - Solução

while True:
    N = int(input())

    if N == 0:
        break 

    H = list(map(int, input().split()))

    count_peaks = 0

    for i in range(N):
        h_prev_index = (i - 1 + N) % N 
        h_prev = H[h_prev_index]
        
        h_next_index = (i + 1) % N
        h_next = H[h_next_index]
        
        h_current = H[i] 

        if (h_current > h_prev and h_current > h_next) or \
           (h_current < h_prev and h_current < h_next):
            count_peaks += 1

    print(count_peaks)