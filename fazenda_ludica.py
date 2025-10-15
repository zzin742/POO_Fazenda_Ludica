# ============================================================
# 🐮 Projeto: Fazenda Lúdica
# Autor: José Henrique Teixeira Luiz
# RA: 3225002
# Disciplina: Programação Orientada a Objetos (Python)
# ============================================================
# Objetivo:
# Aplicar os pilares da Programação Orientada a Objetos (POO)
# — Abstração, Herança, Polimorfismo e Encapsulamento —
# através de uma simulação interativa de uma fazenda lúdica.
# ============================================================

from abc import ABC, abstractmethod

# ============================================================
# 🌾 Classe Base: Animal (Abstração)
# ============================================================
class Animal(ABC):
    """
    Classe base que representa um animal genérico da fazenda.
    """

    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def emitir_som(self) -> str:
        """
        Método abstrato que deve ser implementado nas subclasses.
        """
        pass

    def apresentar(self) -> str:
        """
        Apresenta o animal com nome e idade.
        """
        return f"Olá, sou {self.nome} e tenho {self.idade} anos."


# ============================================================
# 🐶 Subclasse: Cachorro (Herança + Polimorfismo)
# ============================================================
class Cachorro(Animal):
    """
    Representa um cachorro da fazenda.
    """

    def __init__(self, nome: str, idade: int, raca: str):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self) -> str:
        return "Au! Au!"

    def apresentar(self) -> str:
        return f"Olá, sou {self.nome}, tenho {self.idade} anos e sou da raça {self.raca}."


# ============================================================
# 🐱 Subclasse: Gato (Herança + Polimorfismo)
# ============================================================
class Gato(Animal):
    """
    Representa um gato da fazenda.
    """

    def __init__(self, nome: str, idade: int, cor_pelo: str):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo

    def emitir_som(self) -> str:
        return "Miau!"

    def apresentar(self) -> str:
        return f"Olá, sou {self.nome}, tenho {self.idade} anos e tenho o pelo {self.cor_pelo}."


# ============================================================
# 🐄 Subclasse: Vaca (Herança + Encapsulamento)
# ============================================================
class Vaca(Animal):
    """
    Representa uma vaca com controle de produção de leite.
    """

    def __init__(self, nome: str, idade: int, producao_leite_litros: float):
        super().__init__(nome, idade)
        self.__producao_leite_litros = producao_leite_litros  # atributo privado

    def emitir_som(self) -> str:
        return "Muuu!"

    def obter_producao_leite(self) -> float:
        """
        Getter para acessar a produção atual de leite.
        """
        return self.__producao_leite_litros

    def registrar_ordenha(self, litros: float):
        """
        Setter para atualizar a produção de leite.
        """
        self.__producao_leite_litros = litros

    def apresentar(self) -> str:
        return f"Olá, sou {self.nome}, tenho {self.idade} anos e produzo {self.__producao_leite_litros} litros de leite."


# ============================================================
# 🚀 Execução e Teste do Sistema
# ============================================================
if __name__ == "__main__":
    print("🐮🐶🐱 Bem-vindo à Fazenda Lúdica!\n")

    # Criação dos objetos
    cachorro = Cachorro("Rex", 3, "Labrador")
    gato = Gato("Mimi", 5, "Branco")
    vaca = Vaca("Mimosa", 7, 25.5)

    animais = [cachorro, gato, vaca]

    # Apresentação geral
    for animal in animais:
        print(animal.apresentar())
    print()

    # Sons personalizados
    for animal in animais:
        print(f"{animal.nome} diz: {animal.emitir_som()}")
    print()

    # Teste de encapsulamento com a vaca
    print(f"Produção atual de leite: {vaca.obter_producao_leite()} litros")
    vaca.registrar_ordenha(28.0)
    print(f"Produção após ordenha: {vaca.obter_producao_leite()} litros")

    print("\n🌾 Sistema finalizado com sucesso!")
