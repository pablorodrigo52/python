#constantes
LIMITE_VERTICAL = 200 #200m
LIMITE_HORIZONTAL = 2000 #2km
PASSO = 10 #o passo é sempre de 10m

N = int(input()) # quantidade de comandos

dist_horizontal = 0
dist_vertical = 0
direcao = 1 # [1 - indo para frente] [-1 - indo para trás] 

def balaoVoando():
    if (dist_vertical > 0):
        return True
    else:
        return False

def dentroLimites(dist, limite):
    if ((dist + PASSO) <= limite):
        return True
    else:
        return False

def executarAcao(dist, passo):
    return dist + passo

for i in range(N):
    comando = input()
    if (comando.upper() == "S"): #subir
        if ( dentroLimites(dist_vertical, LIMITE_VERTICAL) ):
            dist_vertical = executarAcao(dist_vertical, PASSO)
    
    elif(comando.upper() == "F"): #frente
        if ( balaoVoando() and dentroLimites(dist_horizontal, LIMITE_HORIZONTAL) ):
            dist_horizontal = executarAcao(dist_horizontal, (PASSO * direcao))
            if (dist_horizontal == 0):
                direcao = 1
    
    elif (comando.upper() == "V"): #dar volta
        if ( balaoVoando() and dentroLimites(dist_horizontal, LIMITE_HORIZONTAL) ):
            if (dist_horizontal < 0): # nao posso percorrer negativamente, porque vai quebrar a logica
                dist_horizontal = dist_horizontal * (-1)
            dist_horizontal = executarAcao(dist_horizontal, (PASSO * direcao))
            direcao = -1
    
    elif (comando.upper() == "D"): #descer
        if ( balaoVoando() and dentroLimites(dist_vertical, LIMITE_VERTICAL) ):
            dist_vertical = executarAcao(dist_vertical, (PASSO * (-1)))
    
    else: #comando não mapeado
        pass

if (dist_horizontal < 0):
    dist_horizontal = dist_horizontal * (-1)
if (dist_vertical < 0):
    dist_vertical = dist_vertical * (-1)

print('{} {}'.format(dist_vertical, dist_horizontal))