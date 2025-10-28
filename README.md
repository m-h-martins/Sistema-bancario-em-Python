# 🏦 Sistema Bancário em Python

Este projeto é um **sistema bancário orientado a objetos** desenvolvido em Python, com foco em boas práticas de programação, reutilização de código e organização em classes.  
Ele permite o **cadastro de clientes, criação de contas, depósitos, saques e exibição de extratos**, simulando operações básicas de um banco.

---

## 🚀 Funcionalidades

- 👤 **Cadastro de clientes (Pessoa Física)**  
  Permite registrar novos clientes com nome, CPF, data de nascimento e endereço.

- 💳 **Criação de contas correntes**  
  Cada cliente pode possuir uma ou mais contas associadas.

- 💰 **Depósito**  
  Permite realizar depósitos em contas existentes.

- 💸 **Saque com limite**  
  Saques limitados por valor e quantidade máxima de operações diárias.

- 📜 **Extrato detalhado**  
  Exibe todas as transações (depósitos e saques) com data, valor e tipo.

- 📄 **Listagem de contas**  
  Mostra todas as contas cadastradas com dados do titular.

---

## 🧠 Conceitos Utilizados

O projeto aplica diversos conceitos de **Programação Orientada a Objetos (POO)**:

| Conceito | Descrição |
|-----------|------------|
| **Classe e Objeto** | Representam entidades como `Cliente`, `Conta`, `Transacao`, etc. |
| **Herança** | A classe `ContaCorrente` herda de `Conta`. |
| **Abstração** | A classe `Transacao` é abstrata e serve como modelo para `Saque` e `Deposito`. |
| **Encapsulamento** | Atributos privados com prefixo `_` para proteger dados sensíveis. |
| **Composição** | A classe `Conta` contém um `Historico` que registra as transações. |

---

## 🎓 Referências

Este projeto foi desenvolvido com base nos conteúdos e desafios práticos do curso 📘 Suzano - Python Developer
 da Digital Innovation One (DIO)
.
A atividade faz parte dos módulos voltados a Programação Orientada a Objetos (POO).

---

## 👤 Autor

**Nome:** Murilo Humberto Martins  
**Área:** Estudante de Análise e Desenvolvimento de Sistemas + Engenharia de Produção

🔗**LinkedIn:** https://www.linkedin.com/in/murilo-humberto-martins  
🔗**GitHub:** https://github.com/m-h-martins 

💡 Apaixonado por dados, processos e melhoria contínua, tecnologia, automação e soluções inteligentes.  
Desenvolvo projetos que combinam **análise de dados**, **IA aplicada** e **melhoria de processos**, sempre buscando eficiência e aprendizado contínuo.
