from colorama import Fore, Back, Style, init
from movimento import checar_movimento
import os
init()
# Tabuleiro

tabuleiro = [0 for i in range(8)] # Y

for j in range(len(tabuleiro)):
    tabuleiro[j] = ["  "] * 8 # X

def mostrar_tabuleiro(tab):
    for i, linha in enumerate(tabuleiro):
        print(8 - i, end=f": {Style.RESET_ALL}")
        for j, coluna in enumerate(linha):
            print(f"{coluna}", end=f" {Style.RESET_ALL}")
        print("")
        
    print("   a  b  c  d  e  f  g  h")

colunas = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}
# mostrar_tabuleiro(tabuleiro)
# Peças

pecas_brancas ={
        "wP": [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
        "wT": [(7, 0), (7, 7)],
        "wH": [(7, 1), (7, 6)],
        "wB": [(7, 2), (7, 5)],
        "wQ": [(7, 3)],
        "wK": [(7, 4)]
    }
pecas_pretas ={
        "bP": [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)],
        "bT": [(0, 0), (0, 7)],
        "bH": [(0, 1), (0, 6)],
        "bB": [(0, 2), (0, 5)],
        "bQ": [(0, 3)],
        "bK": [(0, 4)]
    }

def comecar_jogo(tab):
    
    # Brancas
    for peca, casas in pecas_brancas.items():
        for casa in casas:
            x, y = casa[0], casa[1]
            tab[x][y] = Fore.WHITE +peca
        

    # Pretas
    for peca, casas in pecas_pretas.items():
        for casa in casas:
            x, y = casa[0], casa[1]
            tab[x][y] = Fore.BLACK + peca

def mover_peca(tab):
    print("Escolha a casa da peça que você quer mover.")
    casa_peca = input("> ")
    casa_x, casa_y = casa_peca[0], casa_peca[1]
    casa_x = colunas[casa_x]
    casa_y = 8 - int(casa_y)
    casa_x, casa_y = casa_y, casa_x

    print("Escolha a casa que deseja ir (Ex: e4).")
    movimento_peca = input("> ").lower()
    movimento_x, movimento_y = movimento_peca[0], movimento_peca[1]    
    movimento_x = colunas[movimento_x]
    movimento_y = 8 - int(movimento_y)
    movimento_x, movimento_y = movimento_y, movimento_x

    response = checar_movimento(tabuleiro, jogador_atual, casa_x, casa_y, movimento_x, movimento_y) 
    if response is True:
        peca_casa_atual = tabuleiro[casa_x][casa_y]
        tabuleiro[casa_x][casa_y] = "  "
        tabuleiro[movimento_x][movimento_y] = peca_casa_atual  
        return True
    os.system("clear")
    return response
        
# colocar_peca(tabuleiro)
# mostrar_tabuleiro(tabuleiro)
# Jogadas

turno = 1
jogador_atual = ""
comecar_jogo(tabuleiro)

while True:

    mostrar_tabuleiro(tabuleiro)
    print("")
    
    print(f"Turno {turno}")
    jogador_atual = "Brancas" if turno % 2 == 1 else "Pretas"

    print(f"Jogador atual: {Fore.YELLOW}{jogador_atual}{Style.RESET_ALL}")
    response = mover_peca(tabuleiro)

    if response == True:
        os.system("clear")
        turno += 1
    else:
        print(response)
        continue
