factor = int(input())
# always a 4x4 matrix
m = [[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]

for i in range(4):
    for j in range(4):
        mElem = int(input())
        if (i == j):
            m[j][i] = mElem * factor
        else:
            m[j][i] = mElem

for i in range(4):
    for j in range(4):
        print(m[i][j], end=' ')
    print('')