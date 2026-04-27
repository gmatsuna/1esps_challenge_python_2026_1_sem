# 🏃‍♂️ Sistema de Gamificação de Hábitos Saudáveis

## 👨‍💻 Integrantes

| Nome | RM |
|------|----|
| Douglas Taveira Vilella Roberto | 567846 |
| Gilberto Hideaki Matsunaga      | 568191 |
| Igor Davi Avelar Rosa Cesário   | 568163 |
| Wenderson da Silva Santos       | 567847 |

---

## 📌 Descrição do Projeto

Este projeto tem como objetivo desenvolver um sistema em Python para registro de atividades diárias relacionadas à saúde e bem-estar, aplicando conceitos de **Computational Thinking**.

A aplicação permite que o usuário registre informações como:

* Quantidade de passos
* Frequência na academia
* Qualidade da alimentação
* Hidratação
* Qualidade do sono

Com base nesses dados, o sistema calcula uma **pontuação diária**, que pode ser utilizada futuramente em um sistema de gamificação com recompensas, badges e incentivos.

---

## 🎯 Objetivo

Aplicar conceitos fundamentais de programação em Python, incluindo:

* Entrada, processamento e saída de dados
* Estruturas de decisão e repetição
* Uso de listas e dicionários
* Modularização com funções e classes
* Boas práticas de programação

---

## 🧠 Lógica de Funcionamento

O sistema funciona em três etapas:

### 1. Entrada de dados

O usuário informa:

* Passos dados no dia
* Se foi à academia
* Se teve alimentação saudável
* Se se hidratou corretamente
* Se teve um sono adequado

---

### 2. Processamento

Os dados são enviados para uma classe responsável pelo cálculo da pontuação:

#### Regras de pontuação:

* Passos: 1 ponto a cada 100 passos
* Academia: +50 pontos
* Alimentação saudável: +30 pontos
* Hidratação: +20 pontos
* Sono adequado: +40 pontos

---

### 3. Armazenamento

Os dados são armazenados em uma **lista de dicionários**, permitindo manter um histórico diário enquanto o sistema estiver ativo. Não foi trabalhado a persistência dos dados.

Exemplo:

```python
{
    "passos": 8000,
    "academia": True,
    "alimentacao": True,
    "hidratacao": False,
    "sono": True,
    "pontos": 120
}
```

---

## 🗂️ Estrutura do Projeto

```
📁 projeto/
│
├── main.py          # Interface principal e controle do sistema
├── registrar.py     # Coleta de dados do usuário
├── pontos.py        # Cálculo da pontuação
```

---

## 🖥️ Funcionalidades

* Registrar atividades diárias
* Calcular pontuação automaticamente
* Armazenar histórico de atividades
* Visualizar histórico completo

---

## 🔄 Fluxo do Sistema

1. Usuário escolhe uma opção no menu
2. Insere os dados solicitados
3. O sistema calcula a pontuação
4. Os dados são armazenados no histórico
5. O usuário pode visualizar os registros

---

## 🧪 Tecnologias Utilizadas

* Python 3
* Programação orientada a objetos (POO)

---

## 📊 Conceitos Aplicados

* ✔ Entrada, processamento e saída
* ✔ Estruturas de decisão (if)
* ✔ Estruturas de repetição (while)
* ✔ Listas (armazenamento de histórico)
* ✔ Dicionários (estrutura dos dados)
* ✔ Funções e classes
* ✔ Modularização do código

---

## 🚀 Possíveis Melhorias Futuras

* Implementação de sistema de badges
* Persistência de dados (arquivo JSON ou banco de dados)
* Interface gráfica (GUI)
* API backend (Flask ou FastAPI)
* Ranking de usuários

---

## 👨‍💻 Autor

Projeto desenvolvido para a disciplina de **Computational Thinking with Python**.

---

## 📌 Considerações Finais

Este projeto demonstra a aplicação prática dos conceitos fundamentais de programação, com foco em organização, reutilização de código e modelagem de dados, servindo como base para sistemas mais complexos de gamificação e análise de comportamento.
