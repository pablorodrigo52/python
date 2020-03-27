M = int(input())
N = int(input())

i = 1
maiorMult = 0
if (M > 0):
    while (i <= N):
        if ((i % M == 0) & (i % M <= N)):
            maiorMult = i
        i = i + 1
if (maiorMult != 0):
    print(maiorMult)
else:
    print("sem multiplos menores que ",N)