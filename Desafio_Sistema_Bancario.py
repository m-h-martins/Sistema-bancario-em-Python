menu = f"""
{'Banco MHM':=^20}
O que deseja fazer?
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
{'':=^20}
"""
opção = ''
número_de_saques = 0
LIMITE_DE_SAQUES = 3
saldo = 0
limite = 500
extrato = ''
while True:
    print(menu)
    opção = str(input('Digite a opção desejada: ')).lower().strip()
    if opção == 'd':
        print(f'{'Depósito':=^20}')
        valor = float(input('Insira o valor: R$  '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito no valor de R$ {valor:.2f}\n'
            print(f'O valor R${valor:.2f} foi depositado\n')
        else:
            print('Operação falhou! Valor inválido, tente novamente.')
    elif opção == 's':
        print(f'{'Saque':=^20}')
        valor = float(input('Insira o valor: R$  '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = número_de_saques >= LIMITE_DE_SAQUES
        if excedeu_saques:
            print(f'Operação falhou! Número de saques limite ({LIMITE_DE_SAQUES}) foi atingido')
        elif excedeu_saldo:
            print('Operação falhou! Saldo insuficiente')
        elif excedeu_limite:
            print('Operação falhou! Você ultrapassou o valor limite por saque')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque no valor de R$ {valor:.2f}\n'
            número_de_saques += 1
            c50 = c20 = c10 = c5 = c1 = 0
            v = valor
            while True:
                if v >= 50:
                    v -= 50
                    c50 += 1
                else:
                    if v >= 20:
                        v -= 20
                        c20 += 1
                    else:
                        if v >= 10:
                            v -= 10
                            c10 += 1
                        else:
                            if v >= 5:
                                v -= 5
                                c5 += 1
                            else:
                                if v >= 1:
                                    v -= 1
                                    c1 += 1
                                else:
                                    break
            print(f'{'Serão sacadas':=^20}')
            print(f'{c50} cédulas de R$ 50.00')
            print(f'{c20} cédulas de R$ 20.00')
            print(f'{c10} cédulas de R$ 10.00')
            print(f'{c5} cédulas de R$ 5.00')
            print(f'{c1} cédulas de R$ 1.00')
        else:
            print('Operação falhou! O valor inválido, tente novamente.')
    elif opção == 'e':
        print(f'{'Extrato':=^20}')
        if not extrato:
            print('Não foram realizadas movimentações')
        else:
            print(extrato)
            print(f'Saldo: R$ {saldo:.2f}')
        print(f'{'':=^20}')
    elif opção == 'q':
        print('Obrigado por utilizar o nosso sistema, até a próxima!')
        break
    else:
        print('Opção inválida! Por favor digite novamente')