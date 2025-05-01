tabuleiro = [
    ['  ', '  ', '  '],
    ['  ', '  ', '  '],
    ['  ', '  ', '  ']
]

def exibir():
    print("Tabuleiro:")
    for i in range(len(tabuleiro)):
        print(" | ".join(tabuleiro[i]))
        if not i == len(tabuleiro) - 1:
            print("--" * 6)

def verificarGanhou():
    if tabuleiro[0][0] == tabuleiro[0][1] and tabuleiro[0][1] == tabuleiro[0][2] and not tabuleiro[0][0] == '  ':
        return True

    if tabuleiro[1][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[1][2] and not tabuleiro[1][0] == '  ':
        return True

    if tabuleiro[2][0] == tabuleiro[2][1] and tabuleiro[2][1] == tabuleiro[2][2] and not tabuleiro[2][0] == '  ':
        return True

    if tabuleiro[2][0] == tabuleiro[1][0] and tabuleiro[1][0] == tabuleiro[0][0] and not tabuleiro[2][0] == '  ':
        return True

    if tabuleiro[2][1] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[0][1] and not tabuleiro[2][1] == '  ':
        return True

    if tabuleiro[2][2] == tabuleiro[1][2] and tabuleiro[1][2] == tabuleiro[0][2] and not tabuleiro[2][2] == '  ':
        return True

    if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2] and not tabuleiro[0][0] == '  ':
        return True

    if tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0] and not tabuleiro[0][2] == '  ':
        return True

    return False

forma = "X"
exibir()

while True:

    while True:
        row = int(input(f"Em qual linha deseja inserir sua forma? ({forma})\n"))
        while row < 0 or row > 2:
            row = int(input(f"Em qual linha deseja inserir sua forma entre 0 e 2? ({forma})\n"))

        col = int(input(f"Em qual coluna deseja inserir sua forma? ({forma})\n"))
        while col < 0 or col > 2:
            col = int(input(f"Em qual coluna deseja inserir sua forma entre 0 e 2? ({forma})\n"))

        if tabuleiro[row][col] == '  ':
            break
        else:
            print("Posição já ocupada!")


    if(col == 1):
        tabuleiro[row][col] = f'{forma} '
    else:
        tabuleiro[row][col] = f'{forma} '


    print('\n')
    exibir()

    if verificarGanhou():
        print(f"\n\n\nO ganhador foi o {forma}!")
        break

    if(forma == "X"):
        forma = "O"
    else:
        forma = "X"

