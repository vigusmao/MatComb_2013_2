UNIVERSO = "abcdefghijklmnopqrstuvwxyz"
TAMANHO_ALVO = 5
ESCOLHAS_DISTINTAS = False
PRINT_OBJETOS = False

def checa_objeto(objeto):
    return "ch" not in "".join(objeto)

def decida(objeto, lista_objetos, opcoes):

    if len(objeto) == TAMANHO_ALVO:
        if checa_objeto(objeto):
            lista_objetos += [objeto]
    else:
        for i in range(len(opcoes)):
            escolha_da_vez = opcoes[i]
            novo_objeto = objeto[:] + [escolha_da_vez]

            if ESCOLHAS_DISTINTAS:
                novas_opcoes = opcoes[:i] + opcoes[i+1:]
            else:
                novas_opcoes = opcoes

            decida(novo_objeto, lista_objetos, novas_opcoes)

##### Main
objeto = []
lista_objetos = []
decida(objeto, lista_objetos, UNIVERSO)

if PRINT_OBJETOS:
    for x in lista_objetos:
        print("".join(x))

print("\nTotal = %d" % len(lista_objetos))




        

















            


