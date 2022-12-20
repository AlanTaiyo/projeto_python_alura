import adivinhacao
import forca

def robot():
    
    while True:
        print('\n' * 130)
        print('************************************************************************')
        print('Olá Mr. Robot, aqui é o seu espaço de projetos feitos ou em andamentos.')
        print('************************************************************************')
        print('Aqui está os seguintes projetos:')
        print('(1) Adivinhacao')
        print('(2) Forca')
        print('Caso você deseje sair basta digitar SAIR em maiúsculo ou digitar 0')
        print('************************************************************************')
        projeto = str(input('Qual deles você deseja executar? '))
        
        if (projeto == '1'):
            print('\n' * 130)
            print('**Executando "Adivinhacao"**')
            adivinhacao.adivinhacao()
            break

        elif (projeto == '2'):
            print('\n' *130)
            print('**Executando "Forca"**')
            forca.forca()

            continue

        elif (projeto == '0') or (projeto == 'SAIR'):
            print('Saindo...')
            break

        else:
            print('Desculpe, mas esse projeto não existe, ou você digitou de uma forma em que eu não posso compreender...')
            print('Tente novamente...')
            continue

    else:
        print('Saindo...')


if(__name__ == '__main__'):
    robot()