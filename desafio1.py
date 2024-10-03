from datetime import datetime

def get_date_time():
    current_date_time = datetime.now()
    formatted_date_time  = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
    return formatted_date_time[:10], formatted_date_time[11: ]

def deposit(balance, amount):
    if amount > 0:
        date, hour = get_date_time()
        balance += amount
        if date in deposits_dict: 
            deposits_dict[date].append((hour, amount))
        else:
            deposits_dict[date] = [(hour, amount)]
        return balance, "Sucesso" 
    return balance, "Erro! O valor a ser depositado não é positivo."

def withdraw(balance, amount):
    if amount <= 0:
        return balance, "Erro! O valor a ser sacado não é positivo."
    if amount > 500:
        return balance, "Erro! O valor excede o limite de saque."
    if amount > balance:
        return balance, "Erro! Saldo insuficiente."
    date, hour = get_date_time()
    if date not in withdraws_dict:
        withdraws_dict[date] = []
    else:
       if len(withdraws_dict[date]) >= 3:
           return balance, "Erro! Limite diário de saque excedido."
    balance -= amount
    withdraws_dict[date].append((hour, amount))
    return balance, "Sucesso"

def print_bank_statement():
    if len(deposits_dict) == 0 and len(withdraws_dict) == 0:
        return "Não houveram transações."
    else:
        print(f"{15*'='} Extrato bancário {15*'='}")
        print("Depósitos:")
        for date in deposits_dict:
            for deposit in deposits_dict[date]: 
                print(f"{date} {deposit[0]} -> Valor = R$ {deposit[1]:10.2f}") 
        print("Saques:")
        for date in withdraws_dict:
            for withdraw in withdraws_dict[date]: 
                print(f"{date} {withdraw[0]} -> Valor = R$ {withdraw[1]:10.2f}") 
        print(f"Saldo atual = R$ {balance:10.2f}")
        print(f"{48*'='}")

def print_transaction_result(balance, message):
    print(f"Saldo atual = R$ {balance:.2f}. {message}")

balance = 0
DAYLY_LIMIT = 3
WITHDRAW_LIMIT = 500.0
deposits_dict = {}
withdraws_dict = {}

menu = """

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair

=> """

while True:
    option = input(menu)
    match option:
        case "1":
            amount = float(input("Insira o valor para depósito: R$ "))
            balance, message = deposit(balance, amount)
            print_transaction_result(balance, message)
        case "2":
            amount = float(input("Insira o valor para saque: R$ "))
            balance, message = withdraw(balance, amount)
            print_transaction_result(balance, message)
        case "3":
            message = print_bank_statement()
            if message:
                print(message)
        case "0":
            break
        case _:
            print("Opção Inválida!")    