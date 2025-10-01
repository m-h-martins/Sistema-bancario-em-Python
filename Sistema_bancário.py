import textwrap
def menu():
    menu = f"""
    {'Banco MHM':=^20}
    O que deseja fazer?
    [d] Depósito
    [s] Saque
    [e] Extrato
    [u] Novo usuário
    [c] Nova conta
    [l] Listar contas
    [q] Sair
    {'':=^20}
    => """
    return input(textwrap.dedent(menu))
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\t R$ {valor:.2f}\n'
        print(f'O valor R${valor:.2f} foi depositado\n')
    else:
        print('Operação falhou! Valor inválido, tente novamente.')
    return saldo, extrato
def sacar(*, saldo, valor, extrato, limite, número_de_saques, LIMITE_DE_SAQUES):
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
        extrato += f'Saque:\t\t R$ {valor:.2f}\n'
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
        print(f'{c50} cédulas de\t R$ 50.00')
        print(f'{c20} cédulas de\t R$ 20.00')
        print(f'{c10} cédulas de\t R$ 10.00')
        print(f'{c5} cédulas de\t R$ 5.00')
        print(f'{c1} cédulas de\t R$ 1.00')
    else:
        print('Operação falhou! O valor inválido, tente novamente.')
    return saldo, extrato
def exibir_extrato(saldo,/,*,extrato):
    if not extrato:
        print('Não foram realizadas movimentações')
    else:
        print(extrato)
        print(f'Saldo:\t\t R$ {saldo:.2f}')
    print(f'{'':=^20}')
def criar_usuario(usuarios):
    cpf = input('Digite o CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Já existe um usuário com esse CPF')
        return
    nome = str(input('Digite o nome completo: '))
    data_de_nascimento = str(input('Digite a data de nascimento (dd/mm/aaa): '))
    endereço = str(input('Informe o endereço (logradouro, número - bairro - cidade/sigla do estado): '))

    usuarios.append({'nome': nome, 'data_de_nascimento': data_de_nascimento, 'cpf': cpf, 'endereço': endereço})
    print('Novo usuário criado com sucesso!')
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
def criar_conta(AGÊNCIA, número_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Nova conta criada com sucesso!')
        return{'agência': AGÊNCIA, 'número_conta': número_conta, 'usuario': usuario}
    print('Usuário não foi encontrado! Cadastre o usuário e tente novamente.')
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
                Agência:\t{conta['agência']}
                C/C:\t{conta['número_conta']}
                Titular:\t{conta['usuario']['nome']}
        """
        print('=' * 20)
        print(textwrap.dedent(linha))
def main():
    AGÊNCIA = '0001'
    número_de_saques = 0
    LIMITE_DE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = ''
    usuarios = []
    contas = []
    número_conta = 1
    while True:
        opção = menu()
        if opção == 'd':
            print(f'{'Depósito':=^20}')
            valor = float(input('Insira o valor: R$  '))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opção == 's':
            print(f'{'Saque':=^20}')
            valor = float(input('Insira o valor: R$  '))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                número_de_saques=número_de_saques,
                LIMITE_DE_SAQUES=LIMITE_DE_SAQUES,
            )
        elif opção == 'e':
            print(f'{'Extrato':=^20}')
            exibir_extrato(saldo, extrato=extrato)
        elif opção == 'q':
            print('Obrigado por utilizar o nosso sistema, até a próxima!')
            break
        elif opção == 'u':
            criar_usuario(usuarios)
        elif opção == 'c':
            conta = criar_conta(AGÊNCIA, número_conta, usuarios)
            if conta:
                contas.append(conta)
                número_conta += 1
        elif opção == 'l':
            listar_contas(contas)
        else:
            print('Opção inválida! Por favor digite novamente')
main()
