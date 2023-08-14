import random

def jogar():
    imprime_nome_jogo()

    palavra_secreta = inicializa_palavra_secreta()
    letras_acertadas = ["_" for letra in palavra_secreta]

    finalizou = False
    print(f"{str(letras_acertadas)}")

    erros = 0
    while (not finalizou):
        chute = pega_chute()
        if (chute in palavra_secreta):
            compara_chute_com_letras(chute, palavra_secreta, letras_acertadas)
        elif(palavra_secreta.find(chute) == -1): 
            erros += 1
            desenha_forca(erros)

        if (erros == 6):
            imprime_mensagem_perdedor()
            finalizou = True
        elif ("_" not in letras_acertadas):
            imprime_mensagem_vencedor()
            finalizou = True
        print(letras_acertadas)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
 
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def compara_chute_com_letras(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            print(f"Encontrei a letra {letra} na posição {index}")
            letras_acertadas[index] = letra
    index += 1

def imprime_nome_jogo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def inicializa_palavra_secreta():
    arquivo = open('palavra.txt', 'r')
    palavras = []
    numero = random.randrange(0, 4)
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    palavra_secreta = palavras[numero].upper()
    
    arquivo.close()
    return palavra_secreta

def pega_chute():
    chute = input("Qual letra você deseja chutar?")
    chute = chute.strip().upper()

    return chute


if(__name__ == "__main__"):
    jogar()
