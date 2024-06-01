from time import sleep
def cadastrar_usuario():
    #usuarios (nome, data de nascimento, cpf e endereco)
    #endereco( logradouro, nro - bairro - cidade/sigla)
    while True:
        n_user = dict()
        global usuarios
        while True:
            cpf = str(input("CPF: "))
            filtro = 0
            for usuario in usuarios:
                if cpf in usuario.values():
                    filtro +=1
            if filtro==0:
                break

            print(f'ERRO! CPF já cadastrado! Tente novamente!')           
        n_user['cpf'] = cpf
        n_user['nome'] = str(input("Nome: "))
        n_user['data de nascimento'] = str(input("Data de Nascimento: [dd/mm/aaaa] "))
        print("Endereço")
        estado = str(input("Estado: "))
        cidade = str(input("Cidade: "))
        logradouro =str(input("Logradouro: "))
        nr = str(input("Número: "))
        bairro = str(input("Bairro: "))
        n_user['endereco'] = f'{logradouro}, {nr}, - {bairro} - {cidade}/{estado}'

        usuarios.append(n_user.copy())
        print("Usuário cadastrado com sucesso")
        continuar = str(input("Deseja cadastrar outro usuário? [S/N]"))
        if continuar in "nN":
            menu()
def criar_conta(usuario):
    
    for indice, dic in enumerate(usuarios):
        if usuario in dic.values():
            user = dic
            codigo_usuario = indice
    if 'conta' not in user.keys():
        conta = f'00011{codigo_usuario}'
        user['conta'] = [conta]
    else:
        conta = f'0001{len(user['conta'])+1}{codigo_usuario}'
        user['conta'].append(conta)

        
    print(f'A conta {conta} foi criada para o CPF {user["cpf"]}')
    sleep(3)
    menu()

def menu():
    opcoes = '''
[d] Depositar
[s] Sacar
[e] Extrato
[f] Novo Usuário
[g] Nova Conta
[q] Sair
=>'''

    while True:

        opcao = input(opcoes)

        # if opcao == "d":
        #     deposito_valor = float(input("Informe o valor a ser depositado: "))
        #     if deposito_valor>0:
        #         saldo += deposito_valor
        #         extrato += f"Depósito: R$ {deposito_valor:.2f}\n"
        #     else:
        #         print("Informe um valor válido")
            
            

        # elif opcao == "s":
            
        #     saque_valor = float(input("Informe o valor a ser sacado: "))
            
        #     sem_saldo = saque_valor > saldo
        #     excedeu_limite = saque_valor > limite
        #     excedeu_limite_saques = numero_saques >= LIMITE_SAQUES

        #     if sem_saldo:
        #         print("Operação falhou! Você não possui saldo suficiente")
        #     elif excedeu_limite:
        #         print(f"Operação falhou! Você ultrapassou o limite de saque de {limite}")
        #     elif excedeu_limite_saques:
        #         print("Operação falhou! Você não pode mais fazer saques hoje")
        #     else:
        #         if saque_valor>0:
        #             saldo -= saque_valor
        #             extrato += f"Saque: R$ {saque_valor:.2f}\n"
        #             numero_saques +=1
    

        # elif opcao == "e":
        #     print("############EXTRATO BANCARIO############")
        #     print(extrato)
        #     print(f'Saldo: R$ {saldo:.2f}')
        if opcao in "Ff":
            cadastrar_usuario()
        elif opcao in "Gg":
            while True:
                if len(usuarios) == 0:
                    print("Você não possui nenhum usuário cadastrado.")
                    sleep(2)
                    menu()
                cpf = str(input("Informe o CPF do cliente: "))
                for usuario in usuarios:
                    
                    if cpf in usuario.values():
                        criar_conta(cpf)
                        break
                    print("CPF inválido!")
            
            
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")










# def vincular_conta():
#     print("vinculando")

# def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):

# def depositar(saldo, valor, extrato):

# def extrato(saldo, *, extrato):

# def listar_contas():



#programa principal
contas = list()
usuarios = list()
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
menu()


