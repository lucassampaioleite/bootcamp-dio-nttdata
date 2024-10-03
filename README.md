# bootcamp-dio-nttdata

### Desafio 1

Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

### Detalhes da implementação: 
- As transações (saques e depósitos) são armazenadas em dicionários, onde a chave é a data (formato dd/mm/aaaa) e valor é uma lista de tuplas, cada uma contendo o formato (hh:mm:ss, valor da transação).
- A biblioteca datetime foi utilizada para gerenciar as datas e horas, além de aplicar a restrição de 3 saques diários.
- Após cada operação de depósito ou saque, o saldo atual é exibido juntamente com uma mensagem indicando sucesso ou erro da transação.
- O código foi totalmente modularizado, organizado em funções que facilitam a leitura e manutenção do script.
- Requer Python 3.10+, devido ao uso da estrutura match-case (nova sintaxe introduzida no Python 3.10).
