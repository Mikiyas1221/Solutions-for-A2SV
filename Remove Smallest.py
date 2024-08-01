n = int(input())
for i in range(n):
    k = int(input())
    numb = list(map(int, input().split()))
    numb.sort()

    j = 1
    while j < len(numb):
        if numb[j] - numb[j-1] == 0 or numb[j] - numb[j-1] == 1:
            numb.pop(j-1)
        else:
            j += 1

    if len(numb) == 1:
        print("YES")
    else:
        print("NO")
