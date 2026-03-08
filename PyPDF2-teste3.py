from abc import ABC, abstractmethod

class PagamentoStrategy(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

class PagamentoCartao(PagamentoStrategy):
    def pagar(self, valor):
        print(f"Pagando R${valor:.2f} com cartão de crédito.")

class PagamentoDinheiro(PagamentoStrategy):
    def pagar(self, valor):
        print(f"Pagando R${valor:.2f} em dinheiro.")

class PagamentoPix(PagamentoStrategy):
    def pagar(self, valor):
        print(f"Pagando R${valor:.2f} via Pix.")

class Pagamento:
    def __init__(self, estrategia: PagamentoStrategy):
        self._estrategia = estrategia

    def set_estrategia(self, estrategia: PagamentoStrategy):
        self._estrategia = estrategia

    def pagar_conta(self, valor):
        self._estrategia.pagar(valor)

if __name__ == "__main__":
    valor_conta = float(input("Digite o valor da conta: R$ "))

    print("Escolha a forma de pagamento:")
    print("1 - Cartão de Crédito")
    print("2 - Dinheiro")
    print("3 - Pix")

    opcao = input("Opção: ")

    if opcao == "1":
        estrategia = PagamentoCartao()
    elif opcao == "2":
        estrategia = PagamentoDinheiro()
    elif opcao == "3":
        estrategia = PagamentoPix()
    else:
        print("Opção inválida! Usando pagamento em dinheiro por padrão.")
        estrategia = PagamentoDinheiro()

    pagamento = Pagamento(estrategia)
    pagamento.pagar_conta(valor_conta)
