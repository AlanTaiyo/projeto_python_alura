import random
import mr_robot

def forca():
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)

        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def imprime_mensagem_abertura():
    print('************************************************************************')
    print('Bem vindo ao jogo da forca, a temática desse jogo é FRUTAS, e você tem\n7 tentativas para descobrir a palavra secreta. Boa sorte! :)')
    print('************************************************************************')

def carrega_palavra_secreta():
    arquivo = open('meus_projetos/palavras.txt','r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input('Qual letra? ')
    chute = chute.strip().upper()

    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1

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
    print('\n')
    print('Escolha uma das opções abaixo para prosseguirmos.')
    print('(1) Jogar novamente')
    print('(2) Voltar as minhas pastas de projetos')
    print('(#) Ou digite qualquer outra coisa para SAIR.')

    opcao = str(input('Digite o que você deseja: '))

    if (opcao == '1'):
        print('\n' * 130)
        forca()
    elif (opcao == '2'):
        print('\n' * 130)
        mr_robot.robot()
    else:
        print('Até mais ;)')

def imprime_mensagem_perdedor(palavra_secreta):
    print("Não foi dessa vez...")
    print(f"A palavra era {palavra_secreta}")
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
    print('\n')
    print('Escolha uma das opções abaixo para prosseguirmos.')
    print('(1) Jogar novamente')
    print('(2) Voltar as minhas pastas de projetos')
    print('(#) Ou digite qualquer outra coisa para SAIR.')

    opcao = str(input('Digite o que você deseja: '))

    if (opcao == '1'):
        print('\n' * 130)
        forca()
    elif (opcao == '2'):
        print('\n' * 130)
        mr_robot.robot()
    else:
        print('Até mais ;)')

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


if (__name__ == '__main__'):
    forca()