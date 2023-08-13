def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'maça'.upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(f"{letras_acertadas}")

    while (not enforcou and not acertou):
        print('jogando...')
        chute = input('Qual letra você deseja chutar? ')
        chute = chute.strip().upper()

        index = 0

        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    print(f"Encontrei a letra {letra} na posição {index}")
                    letras_acertadas[index] = letra
                index += 1
        else: 
            erros += 1
        
        print(letras_acertadas)
        if (palavra_secreta.find(chute) == -1):
            print(f"a leta {chute} não existe na plavra")

        if (erros == 6):
            print("VOCÊ SE ENFORCOU")
            enforcou = True
        elif ("_" not in letras_acertadas):
            print("VOCÊ GANHOU !!!")
            acertou = True

       

       
       

    print("Fim do jogo")



if(__name__ == "__main__"):
    jogar()
