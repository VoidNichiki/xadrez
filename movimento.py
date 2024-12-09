from colorama import Fore, Style

def chesserror(error):
    return f"{Fore.RED}[ERRO] {error}{Style.RESET_ALL}"

def lista_movimento(lista_casa_atual: list[int], 
                    lista_casa_movimento: list[int], 
                    jogador: str,
                    move: list[int] = [1,1]):
    
    """
    Checa se a `lista_casa_atual`, após somar as posições de `movimento`,
    resulta em `lista_casa_movimento`.
    
    Ex: [0, 0] + [1, 1] == [1, 1] -> True
    """
    nova_lista: list[int] = []

    for i, posicao in enumerate(lista_casa_atual):
        if jogador == "Brancas":
            nova_lista.append(posicao+move[i])
        else:
            nova_lista.append(posicao-move[i])
    
    if nova_lista == lista_casa_movimento:
        return True
    return False



def checar_movimento(tab: list, jogador, casa_x:str, casa_y:str, movimento_x:str, movimento_y:str):
    casa_atual = [casa_x, casa_y]
    movimento = [movimento_x, movimento_y]
    peca_movimentada: str = tab[casa_x][casa_y]
    peca_casa_mov: str = tab[movimento_x][movimento_y]

    #Checagem Geral
    if peca_movimentada == "  ":
        return chesserror("Casa vazia.")
    if peca_movimentada.startswith(Fore.BLACK) and jogador == "Brancas":
        return chesserror("Movimento de peça adversaria.")
    if peca_movimentada.startswith(Fore.WHITE) and jogador == "Pretas":
        return chesserror("Movimento de peça adversaria.")
    if casa_atual == movimento:
        return chesserror("Selecione uma casa diferente.")
        
    # Peão
    if "wP" in peca_movimentada in peca_movimentada:
        if lista_movimento(casa_atual, movimento, jogador, [-1, 1]) and peca_casa_mov == "  ":
            return chesserror("Não há peças para serem capturadas!")
        if lista_movimento(casa_atual, movimento, jogador, [-1,-1]) and peca_casa_mov == "  ":
            return chesserror("Não há peças para serem capturadas!")
        if movimento > casa_atual:
            return chesserror("Peões só podem se mover para frente!")

    # Bispo
    if "bB" in peca_movimentada or "wB" in peca_movimentada:
        if (not movimento_y == casa_y + 1 or not movimento_y == casa_y - 1) and (not movimento_x == casa_x + 1 or not movimento_x == casa_x - 1):
            return chesserror("Movimento inválido!")
    
    # Torre
    if "bT" in peca_movimentada or "wT" in peca_movimentada:
        if (movimento_x > casa_x or movimento_x < casa_x) and (movimento_y > casa_y or movimento_y < casa_y): 
            return chesserror("Movimento inválido!")
        
    # Rei
    if "bK" in peca_movimentada or "wK" in peca_movimentada:
        if (movimento_x > casa_x + 1 or movimento_x < casa_x - 1) or (movimento_y > casa_y + 1 or movimento_y < casa_y - 1):
            return chesserror("Movimento inválido!")
    return True

ex_lista = [1, 1]
ex_lista2 = [1, 2]
if ex_lista < ex_lista2:
    print(True)
else:
    print(False)