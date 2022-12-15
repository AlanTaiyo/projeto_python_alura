def jogar():
    print('************************************************************************')
    print('Bem vindo ao jogo da forca')
    print('************************************************************************')

    palavra_secreta = 'cachorro'

    enforcou = False
    acertou = False

    
    while(not enforcou and not acertou):

        chute = input('Qual letra? ')

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print(f'Encontrei a letra {letra} na posição {index}')
            index = index + 1

        print('iniciando...')


if (__name__ == '__main__'):
    jogar()