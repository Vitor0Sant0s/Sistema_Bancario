from cliente.cliente import Cliente
from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca
from contas.conta_salario import ContaSalario


CLI001 = Cliente('Eugenia Ryan', '123.456.789-11', '52',
                 '(16) 99999-9999', 'email@gmail.com')

CLI002 = Cliente('Grace Webb', '123.456.789-11', '36',
                 '(16) 99999-9999', 'email@gmail.com')

'''
CLI - Instancia de Cliente() 
CCO - Instancia de ContaCorrente()
CPO - Instancia de ContaPoupanca()
CSO - Instancia de ContaSalario()
'''


CCO001 = ContaCorrente(CLI001, '123-12', 0)
CPO001 = ContaPoupanca(CLI001, '123-34', 0)
CSO001 = ContaSalario(CLI001, '123-56', 0)

CCO002 = ContaCorrente(CLI002, '321-12', 0)
CPO002 = ContaPoupanca(CLI002, '321-34', 0)
CSO002 = ContaSalario(CLI002, '321-56', 0)

banco_de_dados = {}

banco_de_dados.update({'CLI001': [CCO001, CPO001, CSO001]})
banco_de_dados.update({'CLI002': [CCO002, CPO002, CSO002]})
