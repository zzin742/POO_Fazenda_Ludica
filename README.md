<h1 align="center">🐮 Fazenda Lúdica — Programação Orientada a Objetos em Python 🐍</h1>

<p align="center">
  <strong>Autor:</strong> José Henrique Teixeira Luiz &nbsp;|&nbsp; <strong>RA:</strong> 3225002  
</p>

---

## 🎯 Sobre o Projeto
O projeto **Fazenda Lúdica** foi desenvolvido com o objetivo de aplicar, de forma prática e divertida, os principais pilares da **Programação Orientada a Objetos (POO)** em Python: **Abstração, Herança, Polimorfismo e Encapsulamento.**

A aplicação simula uma fazenda virtual, onde diferentes animais possuem comportamentos e características próprias, demonstrando como o paradigma da POO pode ser usado para representar o mundo real em código.

---

## 🧠 Pilares da POO Aplicados

| Pilar | Descrição | Exemplo no Código |
|:------|:-----------|:------------------|
| 🧱 **Abstração** | Criação da classe base `Animal`, que define atributos e métodos genéricos. | `class Animal` |
| 🌿 **Herança** | As classes `Cachorro`, `Gato` e `Vaca` herdam da classe `Animal`. | `class Cachorro(Animal)` |
| 🎭 **Polimorfismo** | Cada animal implementa o método `emitir_som()` de maneira diferente. | `"Au! Au!"`, `"Miau!"`, `"Muuu!"` |
| 🔒 **Encapsulamento** | A classe `Vaca` protege o atributo `__producao_leite_litros` e utiliza métodos getter e setter. | `obter_producao_leite()` / `registrar_ordenha()` |

---

## 🧩 Estrutura das Classes

Animal (classe base)
├── Cachorro (raca)
│ └── emitir_som → "Au! Au!"
├── Gato (cor_pelo)
│ └── emitir_som → "Miau!"
└── Vaca (__producao_leite_litros)
└── emitir_som → "Muuu!"

yaml
Copiar código

---

## 💻 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/zzin742/POO_Fazenda_Ludica.git
Entre na pasta do projeto:

bash
Copiar código
cd POO_Fazenda_Ludica
Execute o programa:

bash
Copiar código
python fazenda_ludica.py
🧪 Saída Esperada
css
Copiar código
🐮🐶🐱 Bem-vindo à Fazenda Lúdica!

Olá, sou Rex e tenho 3 anos.
Olá, sou Mimi e tenho 5 anos.
Olá, sou Mimosa e tenho 7 anos.
Au! Au!
Miau!
Muuu!
Produção de leite atual: 25.5 litros
Produção de leite após ordenha: 28.0 litros

🌾 Sistema finalizado com sucesso!
⚙️ Tecnologias Utilizadas
🐍 Python 3.x

💾 Git & GitHub (Controle de Versão)

🧩 Paradigma POO (Abstração, Herança, Polimorfismo, Encapsulamento)

👨‍💻 Autor
Nome	RA	Curso
José Henrique Teixeira Luiz	3225002	Análise e Desenvolvimento de Sistemas

📅 Ano: 2025
🏫 (adicione o nome da sua instituição, se desejar)

🏁 Conclusão
O projeto Fazenda Lúdica representa uma aplicação prática e clara dos pilares da Programação Orientada a Objetos, mostrando como é possível modelar o mundo real em código.
Com classes, herança e encapsulamento, o código se torna modular, reutilizável e de fácil manutenção.

<p align="center"> <em>"Transformar lógica em comportamento é o que faz a programação ser uma arte."</em> 💡 </p> <p align="center"> Feito com ❤️ por <strong>José Henrique Teixeira Luiz</strong> 🧑‍💻 </p> ```




