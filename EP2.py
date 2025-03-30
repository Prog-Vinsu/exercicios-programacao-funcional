######################################################
# Programação Funcional / Programção I (2022/1)
# EP2 - Jogo da Velha
# Nome:
# Matrícula:
######################################################
import random
from os import system, name 

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "2022100364" 

def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "Vincenzo Tognere Polonini" 

def limpaTela(): 
	if name == 'nt':
		system('cls')
	else:
		system('clear')

def jogadaComputador(tab, simbComp):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Estratégia:
    A função “jogadaComputador” tem como estratégia principal completar os espaços onde o jogador tem a possibilidade clara de vitória. 
    No entanto, caso o computador tenha possibilidade de vitória, a estratégia de defesa será deixada de lado para que o computador jogue na posição em que ganhará.
	Caso o computador inicie o jogo, ele sempre optará por jogar na posição 7. Se caso o próximo movimento do jogador for em algum dos cantos (1, 3 ou 9), 
    o computador jogará em um dos cantos vazios, forçando o jogador a se defender. 
	Caso o jogador comece jogando por um dos cantos, o computador jogará sempre na posição 5, pois assim evitará que possíveis chances de derrota surjam. 
    Se o jogador começar pela posição 5, o computador sempre jogará em 1, daí seguirá para as estratégias de defesa ou ataque. 
    Se o jogador fizer a primeira jogada nas posições 2, 4, 6 ou 8, o computador também defendera no meio (posição 5).
	Existe também a estratégia para jogadas sem sentido, as quais não se aplicam às estratégias de defesa e ataque, logo o computador não saberia o que fazer e assim retornaria None. 
    Porém com esta estratégia, o computador optara por uma posição mais vantajosa para ele.
	Por fim, se 8 espaços do tabuleiro já tiverem sido ocupados, e a vez de jogar esteja com o computador, o mesmo optará por jogar na posição vazia, resultando em Velha.


    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador

    Retorno:
    Posição (entre 1 e 9) da jogada do computador
    """
    if simbComp == "X":
        simbPlayer = "O"
    else:
        simbPlayer = "X"  
    
    #### Defesa PC ####

    # Defesa nas posições centrais (coluna central vertical)
    if tab[1] == simbPlayer and tab[3] == simbPlayer and tab[2] == " ":
        return 6 if (tab[4] == simbComp and tab[5] == simbComp and tab[6] == " ") else 4 if (tab[5] == simbComp and tab[6] == simbComp and tab[4] == " ") else 8 if (tab[7] == simbComp and tab[9] == simbComp and tab[8] == " ") else 9 if (tab[7] == simbComp and tab[8] == simbComp and tab[9] == " ") else 5 if (tab[4] == simbComp and tab[6] == simbComp and tab[5] == " ") else 7 if (tab[8] == simbComp and tab[9] == simbComp and tab[7] == " ") else 2
    if tab[4] == simbPlayer and tab[6] == simbPlayer and tab[5] == " ":
        return 9 if (tab[7] == simbComp and tab[8] == simbComp and tab[9] == " ") else 3 if (tab[1] == simbComp and tab[2] == simbComp and tab[3] == " ") else 8 if (tab[7] == simbComp and tab[9] == simbComp and tab[8] == " ") else 2 if (tab[1] == simbComp and tab[3] == simbComp and tab[2] == " ") else 7 if (tab[8] == simbComp and tab[9] == simbComp and tab[7] == " ") else 1 if (tab[2] == simbComp and tab[3] == simbComp and tab[1] == " ") else 5
    if tab[7] == simbPlayer and tab[9] == simbPlayer and tab[8] == " ":
        return 4 if (tab[5] == simbComp and tab[6] == simbComp and tab[4] == " ") else 6 if (tab[4] == simbComp and tab[5] == simbComp and tab[6] == " ") else 3 if (tab[1] == simbComp and tab[2] == simbComp and tab[3] == " ") else 1 if (tab[2] == simbComp and tab[3] == simbComp and tab[1] == " ") else 2 if (tab[1] == simbComp and tab[3] == simbComp and tab[2] == " ") else 5 if (tab[4] == simbComp and tab[6] == simbComp and tab[5] == " ") else 8

    # Defesa nas posições centrais (coluna central horizontal)
    if tab[1] == simbPlayer and tab[7] == simbPlayer and tab[4] == " ":
        return 8 if (tab[2] == simbComp and tab[5] == simbComp and tab[8] == " ") else 2 if (tab[5] == simbComp and tab[8] == simbComp and tab[2] == " ") else 9 if (tab[3] == simbComp and tab[6] == simbComp and tab[9] == " ") else 5 if (tab[2] == simbComp and tab[8] == simbComp and tab[5] == " ") else 6 if (tab[3] == simbComp and tab[9] == simbComp and tab[6] == " ") else 3 if (tab[6] == simbComp and tab[9] == simbComp and tab[3] == " ") else 4
    if tab[2] == simbPlayer and tab[8] == simbPlayer and tab[5] == " ":
        return 4 if (tab[1] == simbComp and tab[7] == simbComp and tab[4] == " ") else 6 if (tab[3] == simbComp and tab[9] == simbComp and tab[6] == " ") else 7 if (tab[1] == simbComp and tab[4] == simbComp and tab[7] == " ") else 9 if (tab[6] == simbComp and tab[3] == simbComp and tab[9] == " ") else 1 if (tab[7] == simbComp and tab[4] == simbComp and tab[1] == " ") else 3 if (tab[9] == simbComp and tab[6] == simbComp and tab[3] == " ") else 5
    if tab[3] == simbPlayer and tab[9] == simbPlayer and tab[6] == " ":
        return 8 if (tab[2] == simbComp and tab[5] == simbComp and tab[8] == " ") else 2 if (tab[8] == simbComp and tab[5] == simbComp and tab[2] == " ") else 4 if (tab[1] == simbComp and tab[7] == simbComp and tab[4] == " ") else 7 if (tab[1] == simbComp and tab[4] == simbComp and tab[7] == " ") else 1 if (tab[4] == simbComp and tab[7] == simbComp and tab[1] == " ") else 5 if (tab[2] == simbComp and tab[8] == simbComp and tab[5] == " ") else 6
    
    # Defesa no centro (cantos preenchidos)
    if tab[1] == simbPlayer and tab[9] == simbPlayer and tab[5] == " ":
        return 5
    if tab[3] == simbPlayer and tab[7] == simbPlayer and tab[5] == " ":
        return 5
    
    # Defesa nos cantos (diagonais)
    if tab[1] == simbPlayer and tab[5] == simbPlayer and tab[9] == " ":
        return 9
    if tab[3] == simbPlayer and tab[5] == simbPlayer and tab[7] == " ":
        return 7
    if tab[7] == simbPlayer and tab[5] == simbPlayer and tab[3] == " ":
        return 3
    if tab[9] == simbPlayer and tab[5] == simbPlayer and tab[1] == " ":
        return 1

    # Defesa nos cantos (diagonais)
    if tab[9] == simbPlayer and tab[5] == simbPlayer and tab[1] == " ":
        return 1
    if tab[7] == simbPlayer and tab[5] == simbPlayer and tab[3] == " ":
        return 3
    if tab[1] == simbPlayer and tab[5] == simbPlayer and tab[9] == " ":
        return 9
    if tab[3] == simbPlayer and tab[5] == simbPlayer and tab[7] == " ":
        return 7

    # Defesa na lateral (esquerda para a direita)
    if tab[1] == simbPlayer and tab[2] == simbPlayer and tab[3] == " ":
        return 8 if (tab[7] == simbComp and tab[9] == simbComp and tab[8] == " ") else 9 if (tab[7] == simbComp and tab[8] == simbComp and tab[9] == " ") else 6 if (tab[4] == simbComp and tab[5] == simbComp and tab[6] == " ") else 5 if (tab[4] == simbComp and tab[6] == simbComp and tab[5] == " ") else 4 if (tab[5] == simbComp and tab[6] == simbComp and tab[4] == " ") else 7 if (tab[8] == simbComp and tab[9] == simbComp and tab[7] == " ") else 3
    if tab[4] == simbPlayer and tab[5] == simbPlayer and tab[6] == " ":
        return 8 if (tab[7] == simbComp and tab[9] == simbComp and tab[8] == " ") else 9 if (tab[7] == simbComp and tab[8] == simbComp and tab[9] == " ") else 2 if (tab[1] == simbComp and tab[3] == simbComp and tab[2] == " ") else 3 if (tab[1] == simbComp and tab[2] == simbComp and tab[3] == " ") else 7 if (tab[8] == simbComp and tab[9] == simbComp and tab[7] == " ") else 1 if (tab[2] == simbComp and tab[3] == simbComp and tab[1] == " ") else 6
    if tab[7] == simbPlayer and tab[8] == simbPlayer and tab[9] == " ":
        return 6 if (tab[4] == simbComp and tab[5] == simbComp and tab[6] == " ") else 3 if (tab[1] == simbComp and tab[2] == simbComp and tab[3] == " ") else 5 if (tab[4] == simbComp and tab[6] == simbComp and tab[5] == " ") else 2 if (tab[1] == simbComp and tab[3] == simbComp and tab[2] == " ") else 4 if (tab[5] == simbComp and tab[6] == simbComp and tab[4] == " ") else 1 if (tab[2] == simbComp and tab[3] == simbComp and tab[1] == " ") else 9

    # Defesa na lateral (baixo para cima)
    if tab[1] == simbPlayer and tab[4] == simbPlayer and tab[7] == " ":
        return 8 if (tab[2] == simbComp and tab[5] == simbComp and tab[8] == " ") else 9 if (tab[3] == simbComp and tab[6] == simbComp and tab[9] == " ") else 5 if (tab[2] == simbComp and tab[8] == simbComp and tab[5] == " ") else 6 if (tab[3] == simbComp and tab[9] == simbComp and tab[6] == " ") else 2 if (tab[5] == simbComp and tab[8] == simbComp and tab[2] == " ") else 3 if (tab[6] == simbComp and tab[9] == simbComp and tab[3] == " ") else 7
    if tab[2] == simbPlayer and tab[5] == simbPlayer and tab[8] == " ":
        return 4 if (tab[1] == simbComp and tab[7] == simbComp and tab[4] == " ") else 7 if (tab[1] == simbComp and tab[4] == simbComp and tab[7] == " ") else 6 if (tab[3] == simbComp and tab[9] == simbComp and tab[6] == " ") else 9 if (tab[3] == simbComp and tab[6] == simbComp and tab[9] == " ") else 1 if (tab[4] == simbComp and tab[7] == simbComp and tab[1] == " ") else 3 if (tab[6] == simbComp and tab[9] == simbComp and tab[3] == " ") else 8
    if tab[3] == simbPlayer and tab[6] == simbPlayer and tab[9] == " ":
        return 8 if (tab[2] == simbComp and tab[5] == simbComp and tab[8] == " ") else 4 if (tab[1] == simbComp and tab[7] == simbComp and tab[4] == " ") else 7 if (tab[1] == simbComp and tab[4] == simbComp and tab[7] == " ") else 5 if (tab[2] == simbComp and tab[8] == simbComp and tab[5] == " ") else 1 if (tab[4] == simbComp and tab[7] == simbComp and tab[1] == " ") else 2 if (tab[5] == simbComp and tab[8] == simbComp and tab[2] == " ") else 9
    
    # Defesa na lateral (direita para a esquerda)
    if tab[3] == simbPlayer and tab[2] == simbPlayer and tab[1] == " ":
        return 4 if (tab[5] == simbComp and tab[6] == simbComp and tab[4] == " ") else 5 if (tab[4] == simbComp and tab[6] == simbComp and tab[5] == " ") else 7 if (tab[8] == simbComp and tab[9] == simbComp and tab[7] == " ") else 8 if (tab[7] == simbComp and tab[9] == simbComp and tab[8] == " ") else 6 if (tab[4] == simbComp and tab[5] == simbComp and tab[6] == " ") else 9 if (tab[7] == simbComp and tab[8] == simbComp and tab[9] == " ") else 1
    if tab[6] == simbPlayer and tab[5] == simbPlayer and tab[4] == " ":
        return 2 if (tab[1] == simbComp and tab[3] == simbComp and tab[2] == " ") else 7 if (tab[8] == simbComp and tab[9] == simbComp and tab[7] == " ") else 1 if (tab[2] == simbComp and tab[3] == simbComp and tab[1] == " ") else 8 if (tab[7] == simbComp and tab[9] == simbComp and tab[8] == " ") else 3 if (tab[1] == simbComp and tab[2] == simbComp and tab[3] == " ") else 9 if (tab[7] == simbComp and tab[8] == simbComp and tab[9] == " ") else 4
    if tab[9] == simbPlayer and tab[8] == simbPlayer and tab[7] == " ":
        return 4 if (tab[5] == simbComp and tab[6] == simbComp and tab[4] == " ") else 1 if (tab[2] == simbComp and tab[3] == simbComp and tab[1] == " ") else 2 if (tab[1] == simbComp and tab[3] == simbComp and tab[2] == " ") else 5 if (tab[4] == simbComp and tab[6] == simbComp and tab[5] == " ") else 3 if (tab[1] == simbComp and tab[2] == simbComp and tab[3] == " ") else 6 if (tab[4] == simbComp and tab[5] == simbComp and tab[6] == " ") else 7

    # Defesa na lateral (cima para baixo)
    if tab[7] == simbPlayer and tab[4] == simbPlayer and tab[1] == " ":
        return 8 if (tab[2] == simbComp and tab[5] == simbComp and tab[8] == " ") else 2 if (tab[8] == simbComp and tab[5] == simbComp and tab[2] == " ") else 3 if (tab[6] == simbComp and tab[9] == simbComp and tab[3] == " ") else 5 if (tab[2] == simbComp and tab[8] == simbComp and tab[5] == " ") else 6 if (tab[3] == simbComp and tab[9] == simbComp and tab[6] == " ") else 9 if (tab[3] == simbComp and tab[6] == simbComp and tab[9] == " ") else 1
    if tab[8] == simbPlayer and tab[5] == simbPlayer and tab[2] == " ":
        return 4 if (tab[1] == simbComp and tab[7] == simbComp and tab[4] == " ") else 1 if (tab[4] == simbComp and tab[7] == simbComp and tab[1] == " ") else 3 if (tab[6] == simbComp and tab[9] == simbComp and tab[3] == " ") else 6 if (tab[3] == simbComp and tab[9] == simbComp and tab[6] == " ") else 7 if (tab[1] == simbComp and tab[4] == simbComp and tab[7] == " ") else 9 if (tab[3] == simbComp and tab[6] == simbComp and tab[9] == " ") else 2
    if tab[9] == simbPlayer and tab[6] == simbPlayer and tab[3] == " ":
        return 4 if (tab[1] == simbComp and tab[7] == simbComp and tab[4] == " ") else 2 if (tab[5] == simbComp and tab[8] == simbComp and tab[2] == " ") else 1 if (tab[4] == simbComp and tab[7] == simbComp and tab[1] == " ") else 5 if (tab[2] == simbComp and tab[8] == simbComp and tab[5] == " ") else 7 if (tab[1] == simbComp and tab[4] == simbComp and tab[7] == " ") else 8 if (tab[2] == simbComp and tab[5] == simbComp and tab[8] == " ") else 3
    
    
    #### Ataques PC ####

    # Ataque nas posições centrais (coluna central vertical)
    if tab[1] == simbComp and tab[3] == simbComp and tab[2] == " ":
        return 2
    if tab[4] == simbComp and tab[6] == simbComp and tab[5] == " ":
        return 5
    if tab[7] == simbComp and tab[9] == simbComp and tab[8] == " ":
        return 8

    # Ataque nas posições centrais (coluna central horizontal)
    if tab[1] == simbComp and tab[7] == simbComp and tab[4] == " ":
        return 4
    if tab[2] == simbComp and tab[8] == simbComp and tab[5] == " ":
        return 5
    if tab[3] == simbComp and tab[9] == simbComp and tab[6] == " ":
        return 6

    # Ataque no centro (cantos preenchidos)
    if tab[1] == simbComp and tab[9] == simbComp and tab[5] == " ":
        return 5
    if tab[3] == simbComp and tab[7] == simbComp and tab[5] == " ":
        return 5

    # Ataque no canto (diagonais)
    if tab[7] == simbComp and tab[5] == simbComp and tab[3] == " ":
        return 3
    if tab[1] == simbComp and tab[5] == simbComp and tab[9] == " ":
        return 9
    if tab[3] == simbComp and tab[5] == simbComp and tab[7] == " ":
        return 7
    if tab[9] == simbComp and tab[5] == simbComp and tab[1] == " ":
        return 1

    # Ataque nas posições laterais (esquerda para a direita)
    if tab[1] == simbComp and tab[2] == simbComp and tab[3] == " ":
        return 3
    if tab[4] == simbComp and tab[5] == simbComp and tab[6] == " ":
        return 6
    if tab[7] == simbComp and tab[8] == simbComp and tab[9] == " ":
        return 9

    # Ataque nas posições laterais (baixo para cima)
    if tab[1] == simbComp and tab[4] == simbComp and tab[7] == " ":
        return 7
    if tab[2] == simbComp and tab[5] == simbComp and tab[8] == " ":
        return 8
    if tab[3] == simbComp and tab[6] == simbComp and tab[9] == " ":
        return 9
    
    # Ataque nas posições laterais (direita para a esquerda)
    if tab[3] == simbComp and tab[2] == simbComp and tab[1] == " ":
        return 1
    if tab[6] == simbComp and tab[5] == simbComp and tab[4] == " ":
        return 4
    if tab[9] == simbComp and tab[8] == simbComp and tab[7] == " ":
        return 7

    # Ataque nas posições laterais (cima para baixo)
    if tab[7] == simbComp and tab[4] == simbComp and tab[1] == " ":
        return 1
    if tab[8] == simbComp and tab[5] == simbComp and tab[2] == " ":
        return 2
    if tab[9] == simbComp and tab[6] == simbComp and tab[3] == " ":
        return 3

    #### Jogadas ####
        
    if tab[7] == " " and tab[1] == " " and tab[2] == " " and tab[3] == " " and tab[4] == " " and tab[5] == " " and tab[6] == " " and tab[8] == " " and tab[9] == " ":
        return 7
    if tab[7] == simbComp and tab[3] == simbPlayer and tab[1] == " ":
        return 1
    if tab[7] == simbComp and tab[1] == simbPlayer and tab[9] == " ":
        return 9
    if tab[7] == simbComp and tab[9] == simbPlayer and tab[1] == " ":
        return 1
    if tab[7] == simbComp and tab[5] == simbPlayer and tab[1] == " ":
        return 1

    if (((tab[1] == simbPlayer or tab[3] == simbPlayer) or tab[7] == simbPlayer) or tab[9] == simbPlayer) and tab[5] == " ":
        return 5
    if tab[5] == simbPlayer and tab[1] == " " and tab[2] == " " and tab[3] == " " and tab[4] == " " and tab[6] == " " and tab[7] == " " and tab[8] == " " and tab[9] == " ":
        return 1
        
    if tab[4] == simbPlayer and tab[5] == " ":
        return 5
    if tab[8] == simbPlayer and tab[5] == " ":
        return 5
    if tab[2] == simbPlayer and tab[5] == " ":
        return 5
    if tab[6] == simbPlayer and tab[5] == " ":
        return 5
    
    # Jogadas sem muito sentido
    if tab[2] == simbPlayer and tab[9] == simbPlayer and tab[5] == simbComp and tab[3] == " ":
        return 3
    if tab[2] == simbPlayer and tab[7] == simbPlayer and tab[5] == simbComp and tab[1] == " ":
        return 1
    if tab[8] == simbPlayer and tab[1] == simbPlayer and tab[5] == simbComp and tab[7] == " ":
        return 7
    if tab[8] == simbPlayer and tab[3] == simbPlayer and tab[5] == simbComp and tab[9] == " ":
        return 9
    if tab[4] == simbPlayer and tab[3] == simbPlayer and tab[5] == simbComp and tab[1] == " ":
        return 1
    if tab[4] == simbPlayer and tab[9] == simbPlayer and tab[5] == simbComp and tab[7] == " ":
        return 7
    if tab[6] == simbPlayer and tab[7] == simbPlayer and tab[5] == simbComp and tab[9] == " ":
        return 9
    if tab[6] == simbPlayer and tab[1] == simbPlayer and tab[5] == simbComp and tab[3] == " ":
        return 3

    if tab[5] == simbPlayer and tab[4] == simbPlayer and tab[3] == simbPlayer and tab[2] == " ":
        return 2

    if tab[5] == simbPlayer and tab[9] == simbPlayer and tab[1] == simbComp and tab[3] == " ":
        return 3

    if tab[5] == simbPlayer and tab[2] == simbPlayer and tab[7] ==  simbPlayer and tab[9] == simbPlayer and tab[4] == " ":
        return 4
    if tab[5] == simbPlayer and tab[7] == simbPlayer and tab[3] ==  simbPlayer and tab[9] == simbPlayer and tab[2] == " ":
        return 2
    if tab[5] == simbPlayer and tab[1] == simbPlayer and tab[3] ==  simbPlayer and tab[8] == simbPlayer and tab[4] == " ":
        return 4
    if tab[5] == simbPlayer and tab[6] == simbPlayer and tab[1] ==  simbPlayer and tab[7] == simbPlayer and tab[2] == " ":
        return 2

    if tab[8] == simbPlayer and tab[4] == simbPlayer and tab[5] ==  simbComp and tab[7] == " ":
        return 7
    if tab[4] == simbPlayer and tab[2] == simbPlayer and tab[5] ==  simbComp and tab[1] == " ":
        return 1
    if tab[2] == simbPlayer and tab[6] == simbPlayer and tab[5] ==  simbComp and tab[3] == " ":
        return 3
    if tab[6] == simbPlayer and tab[8] == simbPlayer and tab[5] ==  simbComp and tab[9] == " ":
        return 9
    
    if tab[2] == simbPlayer and tab[8] == simbPlayer and tab[5] == simbComp and tab[7] == " ":
        return 7
    if tab[4] == simbPlayer and tab[6] == simbPlayer and tab[5] == simbComp and tab[9] == " ":
        return 9
    
    if tab[7] == simbPlayer and tab[3] == simbPlayer and tab[5] == simbComp and tab[2] == " ":
        return 2
    if tab[1] == simbPlayer and tab[9] == simbPlayer and tab[5] == simbComp and tab[2] == " ":
        return 2
    

    #### Completa espaço ####

    if tab[1] != " " and tab[2] != " " and tab[3] != " " and tab[4] != " " and tab[5] != " " and tab[6] != " " and tab[7] != " " and tab[8] != " " and tab[9] == " ":
        return 9
    if tab[1] != " " and tab[2] != " " and tab[3] != " " and tab[4] != " " and tab[5] != " " and tab[6] != " " and tab[7] != " " and tab[8] == " " and tab[9] != " ":
        return 8
    if tab[1] != " " and tab[2] != " " and tab[3] != " " and tab[4] != " " and tab[5] != " " and tab[6] != " " and tab[7] == " " and tab[8] != " " and tab[9] != " ":
        return 7
    if tab[1] != " " and tab[2] != " " and tab[3] != " " and tab[4] != " " and tab[5] != " " and tab[6] == " " and tab[7] != " " and tab[8] != " " and tab[9] != " ":
        return 6
    if tab[1] != " " and tab[2] != " " and tab[3] != " " and tab[4] != " " and tab[5] == " " and tab[6] != " " and tab[7] != " " and tab[8] != " " and tab[9] != " ":
        return 5
    if tab[1] != " " and tab[2] != " " and tab[3] != " " and tab[4] == " " and tab[5] != " " and tab[6] != " " and tab[7] != " " and tab[8] != " " and tab[9] != " ":
        return 4
    if tab[1] != " " and tab[2] != " " and tab[3] == " " and tab[4] != " " and tab[5] != " " and tab[6] != " " and tab[7] != " " and tab[8] != " " and tab[9] != " ":
        return 3
    if tab[1] != " " and tab[2] == " " and tab[3] != " " and tab[4] != " " and tab[5] != " " and tab[6] != " " and tab[7] != " " and tab[8] != " " and tab[9] != " ":
        return 2
    if tab[1] == " " and tab[2] != " " and tab[3] != " " and tab[4] != " " and tab[5] != " " and tab[6] != " " and tab[7] != " " and tab[8] != " " and tab[9] != " ":
        return 9

def escolheSimb():
    '''
    Função responsável por perguntar ao jogaor qual o símbolo que ele vai querer jogar.

    Retorna o símbolo correspondente ao jogador e ao computador.
    '''
    x = leValor(str, "Escolha o simbolo que deseja jogar(X ou O): ")
    if x == "x" or x == "X":
        return "X", "O"
    elif x == "o" or x == "O":
        return "O", "X"
    else:
        print("Simbolo inválido")
        return escolheSimb()

def primeiraJogada():
    '''
    Função responsável por realizar o sorteio de quem começará jogando.
    
    Retorna 0 quando for sorteado o jogador e 1 quando for o computador.
    '''
    x = random.randint(0,1)
    if x == 0:
        print("O jogador joga primeiro")
        return 0
    else:
        print("O computador joga primeiro")
        return 1

def printTab(tab):
    '''
    Função responsável por imprimir o tabuleiro.

    Não retorna nada.

    Parâmetro:
        - recebe a lista das posições
    '''
    print()
    print(f" {tab[7]} | {tab[8]} | {tab[9]} ")
    print("---+---+---")
    print(f" {tab[4]} | {tab[5]} | {tab[6]} ")
    print("---+---+---")
    print(f" {tab[1]} | {tab[2]} | {tab[3]} ")
    print()

def inicio_jogo(jogador, simbPlayer, simbComp, tab, cont):
    '''
    Função responsável por dar início ao jogo e alternas as jogadas entre o jogador e o computador.

    Retorna a si mesma, fazendo a alternancia de jogador através do parâmetro jogador.

    Parâmetros:
        - jogador: representa o jogador que fará a próxima jogada
        - simbPlayer: símbolo do jogador
        - simbComp: símbolo do computador
        - tab: lista do tabuleiro
        - cont: contador
    '''
    if jogador == 0:
        jogada = jogadaPlayer(tab, simbPlayer)
        tab[jogada] = simbPlayer
        printTab(tab)
        cont+=1
        if verificaJogada(tab, simbPlayer, cont) == True:
            print("O jogador venceu")
        elif verificaJogada(tab, simbPlayer, cont) == False:
            print("Deu velha!!")
        else:
            return inicio_jogo(1, simbPlayer, simbComp, tab, cont)
    else:
        jogada = jogadaComputador(tab, simbComp)
        print("---------------------")
        print("Jogada do computador:")
        tab[jogada] = simbComp
        printTab(tab)
        cont+=1
        if verificaJogada(tab, simbComp, cont) == True:
            print("O computador venceu")
        elif verificaJogada(tab, simbPlayer, cont) == False:
            print("Deu velha!!")
        else:
            return inicio_jogo(0, simbPlayer, simbComp, tab, cont)

def jogadaPlayer(tab, simbPlayer):
    '''
    Função responsável por solicitar a posição a ser jogada pelo jogador.

    Retorna a posição da jogada, se a mesma for válida.

    Parâmetros:
        - tab: lista do tabuleiro
        - simbPlayer: símbolo do jogador
    '''
    jogada = leValor(int, "Qual posição deseja marcar? (1-9): ")
    if 1 <= jogada <= 9:
        if tab[jogada] == " ":
            return jogada
        elif tab[jogada] == "X" or tab[jogada] == "O":
            print("Jogada inválida")
            return jogadaPlayer(tab, simbPlayer)
    else:
        print("Posição inexistente")
        return jogadaPlayer(tab, simbPlayer)

def verificaJogada(tab, simb, cont):
    '''
    Função responsável por verificar os casos de vitória ou de empate.

    Retorna True quando um dos jogadores vencer ou False quando o jogo deu velha.

    Parâmetros:
        - tab: lista do tabuleiro
        - simb: símbolo da última jogada
        - cont: contador
    '''
    if cont <= 9:
        if tab[1] == simb and tab[2] == simb and tab[3] == simb:
            return True
        elif tab[4] == simb and tab[5] == simb and tab[6] == simb:
            return True
        elif tab[7] == simb and tab[8] == simb and tab[9] == simb:
            return True
        elif tab[1] == simb and tab[4] == simb and tab[7] == simb:
            return True
        elif tab[2] == simb and tab[5] == simb and tab[8] == simb:
            return True
        elif tab[3] == simb and tab[6] == simb and tab[9] == simb:
            return True
        elif tab[1] == simb and tab[5] == simb and tab[9] == simb:
            return True
        elif tab[3] == simb and tab[5] == simb and tab[7] == simb:
            return True
        elif cont == 9:
            return False

def leValor(funcaoConv, msg = ""):
    '''
    Função responsável por permitir que somente seja aceito um input do tipo solicitado.

    Retorna um input.
    '''
    try:
        return funcaoConv(input(msg))
    except:
        print("ERRO: Tipo inválido")
        return leValor(funcaoConv, msg)

def main():
    '''
    Função responsável por chamar a função de escolha do símbolo, sorteio da primeira jogada e a de início do jogo.

    Não retorna nada.
    '''
    limpaTela()
    #Você pode, se quiser, comentar os dois prints abaixo:
    print(getNome())
    print(getMatricula())
    print("Bem vindo ao Jogo da Velha!")
    print()
    print(f" 7 | 8 | 9 ")
    print("---+---+---")
    print(f" 4 | 5 | 6 ")
    print("---+---+---")
    print(f" 1 | 2 | 3 ")
    print()
    print("---------------------------")
    simbPlayer, simbComp = escolheSimb()
    print("---------------------------")
    jogador = primeiraJogada()
    inicio_jogo(jogador, simbPlayer, simbComp, tab = [" "]*10, cont = 0)
    

################################
## NÃO ALTERE O CÓDIGO ABAIXO ##
################################
if __name__ == "__main__":
    main()