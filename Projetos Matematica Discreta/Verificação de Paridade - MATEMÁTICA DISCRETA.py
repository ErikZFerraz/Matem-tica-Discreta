print("Verificação de Paridade - MATEMÁTICA DISCRETA")

def verificar_paridade(numero):
    return numero % 2 == 0

while True:
    try:
        numero = int(input("Digite um número inteiro para verificar a paridade: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        continue

    if verificar_paridade(numero):
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

    encerrarPrograma = input("Pressione Enter para finalizar ou qualquer outra tecla para voltar ao início: ").strip().lower()

    if encerrarPrograma == "":
        print("FINISH!")
        break
