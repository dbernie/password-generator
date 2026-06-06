import random
import string

# Fazer gerador de senhas com letras, números e caracteres especiais
options = input(
    "Quantos tipos de caracteres você deseja incluir na senha? (1 a 3): ").strip()

tipos_disponiveis = {
    "1": ("Letras", string.ascii_letters),
    "2": ("Números", "0123456789"),
    "3": ("Caracteres Especiais", "!@#$%^&*()")
}

selecoes = []

if options == "1":
    while True:
        escolha = input(
            "Escolha o tipo de caractere:\n1 - Letras\n2 - Números\n3 - Caracteres Especiais\nDigite a opção: ").strip()
        if escolha in tipos_disponiveis:
            selecoes.append(escolha)
            break
        print("Opção inválida. Digite 1, 2 ou 3.")

elif options == "2":
    while len(selecoes) < 2:
        escolha = input(
            f"Escolha o {len(selecoes) + 1}º tipo de caractere:\n"
            "1 - Letras\n"
            "2 - Números\n"
            "3 - Caracteres Especiais\n"
            "Digite a opção: "
        ).strip()
        if escolha not in tipos_disponiveis:
            print("Opção inválida. Digite 1, 2 ou 3.")
            continue
        if escolha in selecoes:
            print("Você já escolheu esse tipo. Escolha um tipo diferente.")
            continue
        selecoes.append(escolha)

elif options == "3":
    selecoes = ["1", "2", "3"]

else:
    print("Opção inválida. Será usada a combinação de letras, números e caracteres especiais.")
    selecoes = ["1", "2", "3"]

caracteres = ""
for selecao in selecoes:
    caracteres += tipos_disponiveis[selecao][1]

if not caracteres:
    caracteres = string.ascii_letters + "0123456789" + "!@#$%^&*()"

try:
    tamanho = int(input("Digite a quantidade de caracteres da senha: "))
except ValueError:
    tamanho = 12
    print("Entrada inválida. Será gerada uma senha com 12 caracteres.")


def gerar_senha(tamanho):
    senha = ""
    for _ in range(tamanho):
        senha += random.choice(caracteres)
    return senha


print(f"Sua senha é: {gerar_senha(tamanho)}")
 