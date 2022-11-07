def getInput():
    N, K = [int(x) for x in input().split()]
    return N, K

N, K = getInput()
fib = [1,1]
for i in range(N-2):
    fib.append(fib[-1] + fib[-2])

if N > 2:
    index = -1
    while fib[index-2] > 1:
        if fib[index-2] < K: 
            K -= fib[index-2]
            index-=1
        else:
            index-=2

    if fib[index] == 3:
        if K % 2 == 0:
            print("N")
        else:
            print("A")
    else:
        if K == 1:
            print("N")
        else:
            print("A")
else:
    if N == 1:
        print("N")
    else:
        print("A")