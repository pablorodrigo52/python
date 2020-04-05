
rules = {
    0:
    {
        0: "draw",
        1: "lose",
        2: "win"
    },
    1:
    {
        0: "win",
        1: "draw",
        2: "lose"
    },
    2:
    {
        0: "lose",
        1: "win",
        2: "draw"
    }
}

print('Welcome to rock paper scissors python')
print('0 - Rock')
print('1 - Paper')
print('2 - Scissor')

a = True
while(a):
    stop = 'n'
    player1 = int(input('P1 switch one of then\n\t'))
    player2 = int(input('P2 switch one of then\n\t'))

    if (((player1 >= 0) & (player1 < 3)) & ((player2 >= 0) & (player2 < 3))):
        if (rules[player1][player2] == "win"):
            print("\tPlayer 1 WIN!!!!")
        elif (rules[player1][player2] == "draw"):
            print("\tDRAW!!!!")
        else:
            print("\tPlayer 2 WIN!!!!")

        while (stop.lower() != 'y'):
            stop = input('Match one more? Y or N\n\t')
            if ( stop.lower() == 'n'):
                a = False
                break
    else:
        print("You r not funny :(")