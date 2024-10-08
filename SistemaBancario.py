class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, quantia):
        if quantia > 0:
            self.saldo += quantia
            print(f"Depósito de R${quantia} realizado com sucesso.")
        else:
            print("Quantia de depósito inválida.")

    def sacar(self, quantia):
        if 0 < quantia <= self.saldo:
            self.saldo -= quantia
            print(f"Saque de R${quantia} realizado com sucesso.")
        else:
            print("Quantia de saque inválida ou saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")

def main():
    conta = ContaBancaria("Luana")
    while True:
        print("\n1. Depositar")
        print("\n2. Sacar")
        print("\n3. Consultar Saldo")
        print("\n4. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            quantia = float(input("Digite a quantia para depósito: "))
            conta.depositar(quantia)
        elif opcao == 2:
            quantia = float(input("Digite a quantia para saque: "))
            conta.sacar(quantia)
        elif opcao == 3:
            conta.consultar_saldo()
        elif opcao == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()