saldo = 0
limite_diario = 3
extrato = ""
menu = '''
--------- Bem vindo ao Banco -----------

Escolha uma opção:
    [1] Depósito     
    [2] Saque
    [3] Extrato
    [0] Sair
'''

while True:
    opcao = str(input(f'{menu}: '))
    if opcao == '1':
        print('Depósito')
        print(f'Saldo atual: RS{saldo:.2f}')
        deposito = float(input("Quanto deseja depositar? R$"))
        if deposito > 0:
            saldo += deposito
            print(f'Novo Saldo: RS{saldo:.2f}')
        else:
            print('deposito não realizado!')
            print(f'Saldo atual: RS{saldo:.2f}')
    elif opcao == '2':
        print('Saque')
        if limite_diario <=0:
            print('Limite diário para saque atingido. Por favor volte amanhã')
        else:
            print(f'Saldo atual: RS{saldo:.2f}')
            print(f'Você ainda pode fazer {limite_diario} saques hoje.')
            print(f'Valor Máximo de R$500,00 por saque')

            saque = float(input('Quanto deseja sacar? R$ '))
            if (saque >= saldo) or (saque > 500):
                print('Saque não realizado. ')
            elif (saque <= saldo) and (0 < saque <= 500):
                saldo -= saque
                print(f'Saque no valor de R${saque}, foi realizado com sucesso')
                print(f'Saldo atual: RS{saldo:.2f}')
                limite_diario -= 1
            else:
                print('Saque não realizado, por favor digite um valor válido')
    elif opcao == '3':
        print('Extrato')
    elif opcao == '0':
        break
    else:
        print('Opção Inválida')

print('Volte sempre!')