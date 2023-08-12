def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'banana'
    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        print('jogando...')
        chute = input('Qual letra você deseja chutar? ')
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print(f"Encontrei a letra {letra} na posição {index}")
            index = index + 1

        if (palavra_secreta.find(chute) == -1):
            print(f"a leta {chute} não existe na plavra")

        acertou = True

    print("Fim do jogo")



if(__name__ == "__main__"):
    jogar()
