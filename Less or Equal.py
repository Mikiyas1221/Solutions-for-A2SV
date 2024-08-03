def find_x(n, k, seq):
    sorted_seq = sorted(seq)
    
    if k == 0:
        if sorted_seq[0] > 1:
            return 1
        else:
            return -1
    elif k == n:
        return sorted_seq[-1]
    else:
        x_cand = sorted_seq[k - 1]
        if k < n and sorted_seq[k] == x_cand:
            return -1
        else:
            return x_cand

n, k = map(int, input().split())
seq = list(map(int, input().split()))

result = find_x(n, k, seq)
print(result)
