# 🔐 Gerador de Senhas em Python

Gerador de senhas simples e interativo via terminal. Permite personalizar os tipos de caracteres e o tamanho da senha gerada.

---

## ✨ Funcionalidades

- Escolha entre **1, 2 ou 3 tipos** de caracteres na senha
- Tipos disponíveis:
  - 🔤 Letras (maiúsculas e minúsculas)
  - 🔢 Números (0–9)
  - 🔣 Caracteres especiais (`!@#$%^&*()`)
- Tamanho da senha totalmente personalizável
- Geração aleatória segura com o módulo `random`

---

## ▶️ Como usar

### Pré-requisitos

- Python 3.x instalado

### Executando

```bash
python main.py
```

### Exemplo de uso

```
Quantos tipos de caracteres você deseja incluir na senha? (1 a 3): 2
Escolha o 1º tipo de caractere:
1 - Letras
2 - Números
3 - Caracteres Especiais
Digite a opção: 1
Escolha o 2º tipo de caractere:
...
Digite a opção: 3
Digite a quantidade de caracteres da senha: 16
Sua senha é: aB!kXm@qPz#nLw&j
```

---

## 🗂️ Estrutura do projeto

```
.
└── main.py   # Script principal do gerador de senhas
```

---

## 🛠️ Tecnologias

- **Python 3** — linguagem principal
- **`random`** — geração aleatória de caracteres
- **`string`** — conjunto de letras e caracteres ASCII

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.
