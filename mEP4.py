######################################################
# Programção I / Programação Funcional (2022/1)
# miniEP4 - Jogo da Velha
# Nome: Vincenzo Tognere Polonini
# Matrícula: 2022100364
######################################################

def imprimeTabuleiro(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e imprime o tabuleiro
    """
    #Complete o código da função
    print(f" {p7} | {p8} | {p9} ")
    print("---+---+---")
    print(f" {p4} | {p5} | {p6} ")
    print("---+---+---")
    print(f" {p1} | {p2} | {p3} ")

def entradaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores são válidos, ou seja, retorna True
    se cada variável possui " " ou "x" ou "o" e False, caso contrário.
    """
    return True if verificaEntrada(p1) == True and verificaEntrada(p2) == True and verificaEntrada(p3) == True and verificaEntrada(p4) == True and verificaEntrada(p5) == True and verificaEntrada(p6) == True and verificaEntrada(p7) == True and verificaEntrada(p8) == True and verificaEntrada(p9) == True else False

def verificaEntrada(px):
    return True if px == " " or px == "x" or px == "o" else False
        
def jogadaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores formam uma jogada válida.

    Retorna True se a jogada for válida e False, caso contrário
    """
    #Complete o código da função
    x = contadorx(p1) + contadorx(p2) + contadorx(p3) + contadorx(p4) + contadorx(p5) + contadorx(p6) + contadorx(p7) + contadorx(p8) + contadorx(p9)
    o = contadoro(p1) + contadoro(p2) + contadoro(p3) + contadoro(p4) + contadoro(p5) + contadoro(p6) + contadoro(p7) + contadoro(p8) + contadoro(p9)
    return True if  x - o == 1 or x - o == -1 or x - o == 0 else False

def contadorx(px):
    return 1 if px == 'x' else 0

def contadoro(px):
    return 1 if px == 'o' else 0
        
def verificaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    imprime se um jogador ('x' ou 'o') venceu a jogada. 
    (Cada variável representa uma posição no tabuleiro)
    """
    if verificaResultado(p1, p2, p3) == True or verificaResultado(p4, p5, p6) == True or verificaResultado(p7, p8, p9) == True or verificaResultado(p1, p4, p7) == True or verificaResultado(p2, p5, p8) == True or verificaResultado(p3, p6, p9) == True or verificaResultado(p1, p5, p9) == True or verificaResultado(p3, p5, p7) == True:
        if p1 == "x" and p2 == "x" and p3 == "x" or p4 == "x" and p5 == "x" and p6 == "x" or  p7 == "x" and p8 == "x" and p9 == "x" or p1 == "x" and p4 == "x" and p7 == "x" or p2 == "x" and p5 == "x" and p8 == "x" or p3 == "x" and p6 == "x" and p9 == "x" or p1 == "x" and p5 == "x" and p9 == "x" or p3 == "x" and p5 == "x" and p7 == "x":
            print("O jogador 'x' venceu!")
        else:
            print("O jogador 'o' venceu!")
    else:
        if p1 != " " and p2 != " " and p3 != " " and p4 != " " and p5 != " " and p6 != " " and p7 != " " and p8 != " " and p9 != " ":
            print("Empate!")
        else:
            print("O jogo nao terminou!")
        
def verificaResultado(px1, px2, px3):
    if px1 != " " or px2 != " " or px3 != " ":
        return True if px1 == px2 and px2 == px3 and px3 == px1 else False  
    else:
        return False

def main():
    t1 = input()
    t2 = input()
    t3 = input()
    t4 = input()
    t5 = input()
    t6 = input()
    t7 = input()
    t8 = input()
    t9 = input()
    imprimeTabuleiro(t1, t2, t3, t4, t5, t6, t7, t8, t9)
    if entradaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Entrada invalida!")
    elif jogadaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Jogada invalida!")
    else:
        verificaJogada(t1, t2, t3, t4, t5, t6, t7, t8, t9)

main()