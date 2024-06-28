print("Operações Lógicas - MATEMÁTICA DISCRETA")

def input_bool(mensagem):
    while True:
        entrada = input(mensagem).strip().lower()
        if entrada == "true":
            return True
        elif entrada == "false":
            return False
        else:
            print("Entrada inválida. Digite 'true' ou 'false'.")

def input_int(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Escolha inválida. Digite um número entre {minimo} e {maximo}.")
        except ValueError:
            print(f"Entrada inválida. Digite um número entre {minimo} e {maximo}.")

while True:
    p = input_bool("Digite o valor de verdade para P (true/false): ")
    q = input_bool("Digite o valor de verdade para Q (true/false): ")
    escolha = input_int("Escolha a operação lógica:\n1. Negação (~)\n2. Conjunção (˄)\n3. Disjunção (˅)\n4. Condicional (→)\n5. Bicondicional (↔)\n-> ", 1, 5)

    if escolha == 1:
        print(f"Negação de P: {not p}")
        print(f"Negação de Q: {not q}")
    elif escolha == 2:
        print(f"Conjunção de P e Q: {p and q}")
    elif escolha == 3:
        print(f"Disjunção de P e Q: {p or q}")
    elif escolha == 4:
        print(f"Condicional de P para Q: {not p or q}")
    elif escolha == 5:
        print(f"Bicondicional de P para Q: {p == q}")

    encerrarPrograma = input("Pressione Enter para finalizar ou qualquer outra tecla para voltar ao início: ").strip().lower()

    if encerrarPrograma == "":
        print("FINISH!")
        break
