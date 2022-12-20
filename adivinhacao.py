import random
import mr_robot

def adivinhacao():

    print('**************************************')
    print("Bem vindo ao jogo de Adivinhação!\nNeste jogo você tem que descobrir\nqual número aleatório foi gerado.\nConsidera-se que é de 1 a 50.")

    numero_secreto = random.randint(1,20)
    total_de_tentativas = 3
    rodada = 1

    ##print(f'{numero_secreto}')## ===> Mostra o número que foi gerado

    ##Escolha de dificuldade do jogo
    
    print('**************************************')
    print('Você quer qual nível que seja o jogo?')
    print('(1) Fácil')
    print('(2) Médio')
    print('(3) Difícil')
    print('**************************************')

    nivel = int(input('Digite o nível que você deseja: '))

    if (nivel == 1):
        print('\n' * 130)
        total_de_tentativas = 20
    elif (nivel == 2):
        print('\n' * 130)
        total_de_tentativas = 10
    elif (nivel == 3):
        print('\n' * 130)
        total_de_tentativas = 5
    else:
        print('\n' * 130)
        print('O valor digitado deve ser uma dificuldade muito alta, nossa!\nentão vou colocar uma quantidade de tentativa considerável para você! :)')
        print('\n')
        total_de_tentativas = 1
    
    for rodada in range (1, total_de_tentativas + 1):
        print('Tentativa', rodada, 'de', total_de_tentativas)
        print('\n')
        chute = int(input('Chute um número: '))
        if (numero_secreto == chute):
            print("Você acertou!")
            break
        else:
            if(chute > numero_secreto):
                print('\n' * 130)
                print("Você errou! O seu chute foi MAIOR que o número secreto.")
            elif(chute < numero_secreto):
                print('\n' * 130)
                print("Você errou! O seu chute foi MENOR que o número secreto.")
            rodada = rodada + 1
            continue
    
    print('\n' * 130)
    print(f'Fim de jogo, o número aleatório que foi gerado é {numero_secreto}')
    print('Escolha uma das opções abaixo para prosseguirmos.')
    print('(1) Jogar novamente')
    print('(2) Voltar as minhas pastas de projetos')
    print('(#) Ou digite qualquer outra coisa para SAIR.')

    opcao = str(input('Digite o que você deseja: '))

    if (opcao == '1'):
        print('\n' * 130)
        adivinhacao()
    elif (opcao == '2'):
        print('\n' * 130)
        mr_robot.robot()
    else:
        print('Até mais ;)')

if (__name__ == '__main__'):
    adivinhacao()