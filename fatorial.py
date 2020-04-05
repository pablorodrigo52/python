n = 0
count = 0 #contador para o for
k = 0

while(n >=0 and n <= 12):
    n = int(input())
    count = n 
    k = n

    if(n == -1):
        break
    if(n > 12):
        break
    if(k == 0):
        print('1')
        continue
    if(k == 1):
        print('1')
        continue
    while(count > 1):
        k = k * (count - 1) #atualizando o valor do fatorial
        count = count - 1 #atualizando o controlador do while
    
    print('{}'.format(k))

print('\n')