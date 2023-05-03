class Contacorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor
    
    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)

Conta_do_gui = Contacorrente(15)
print(Conta_do_gui)
Conta_do_gui.deposita(500)
print(Conta_do_gui)

Conta_do_dani = Contacorrente(5000)
print(Conta_do_dani)
Conta_do_dani.deposita(1000)
print(Conta_do_dani)

contas = [Conta_do_dani, Conta_do_gui]
print(contas)