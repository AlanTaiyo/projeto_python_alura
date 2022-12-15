import mr_robot

def login():
    
    print('************************************************************************')
    print('Olá, você está entrando em uma pasta que contém arquivos confidenciais.')
    print('************************************************************************')    
    print('Você tem 5 tentativas para digitar seu nome de usuário corretamente.')
    print('************************************************************************')   
    print('\n' * 3)
    tentativa_nome = 4

    while (tentativa_nome >= 0): 
        nome = str(input('Digite seu nome para que eu possa identificá-lo: '))
        if (nome == 'mr.robot123'):
            print('\n' * 130)
            print(f'Olá {nome}')
            tentativa_senha = 1
            tentativa_restante = 3
                
            for tentativa_senha in range (1, tentativa_restante + 1):
                senha = str(input('Digite sua senha: '))

                if (senha == 'gomugomunomi'):
                    print('\n' * 130)
                    print('Acesso concedido. Seja bem vindo Mr. Robot!')
                    mr_robot.robot()
                    break

                else:
                    print('\n' * 130)
                    print(f'Acesso negado, {tentativa_senha} tentativa(s) de 3')
                    tentativa_restante + 1
                    continue
            break
        else:
            print('\n' * 130)
            print('Não encontrei seu nome no nosso banco de dados, tente novamente.')
            print(f'Você tem {tentativa_nome} tentativa(s) restante(s).')
            tentativa_nome = tentativa_nome - 1
            continue
    else:
        print('Acesso bloqueado, tente novamente mais tarde.')


if (__name__ == '__main__'):
    login()