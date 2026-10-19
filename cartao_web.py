from abc import ABC, abstractmethod

# 1. Classe abstrata CartaoWeb
class CartaoWeb(ABC):
    def __init__(self, destinatario: str):
        self.destinatario = destinatario

    # Método abstrato que deve ser implementado pelas subclasses
    @abstractmethod
    def show_message(self):
        pass


# 2. Classes filhas
class DiaDosNamorados(CartaoWeb):
    def show_message(self):
        print(f"Querido(a) {self.destinatario}, feliz Dia dos Namorados! Muito amor e cumplicidade.")


class Natal(CartaoWeb):
    def show_message(self):
        print(f"Olá, {self.destinatario}! Feliz Natal e um próspero Ano Novo cheio de paz.")


class Aniversario(CartaoWeb):
    def show_message(self):
        print(f"Parabéns, {self.destinatario}! Muitas felicidades e anos de vida no seu Aniversário.")


# 3. Programa principal
if __name__ == "__main__":
    # Criando uma lista de objetos de tipos diferentes, mas que compartilham a mesma classe base
    cartoes = [
        DiaDosNamorados("Mariana"),
        Natal("Carlos"),
        Aniversario("Beatriz")
    ]

    # Iterando sobre a mesma referência genérica e invocando o método
    for cartao in cartoes:
        cartao.show_message()