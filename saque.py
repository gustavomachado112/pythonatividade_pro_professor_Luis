Saldo = 500.00
print (f"seu saldo atual e de R${Saldo}")
valor_sacar = int (input("Quanto voce gostaria de sacar? R$"))
if valor_sacar > 0 :
    novo= Saldo-valor_sacar
    if valor_sacar > Saldo:
        print("Saldo insuficiente para realizar o saque.")
        if valor_sacar > 500.00:
            print(f"fazer um emprestimo?")
            credito = (input(f"sim/nao? "))
            if credito == "sim":
                print("Otimo, vamos providenciar o emprestimo , com isso ele sera depositado na sua conta .")
                Saldo = valor_sacar 
                print(f"Seu novo saldo com o empréstimo é de R${Saldo}")
        exit() 
    print  ("seu saque foi realizado com sucesso.")
    print  (f"seu saldo atual e de {novo}")
