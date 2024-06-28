print("Conversor de Binários - MATEMÁTICA DISCRETA")

def decimal_para_binario(numero):
    return bin(numero)[2:]

def binario_para_decimal(binario):
    return int(binario, 2)

while True:
    escolha = input("Escolha a conversão:\n1. Decimal para Binário\n2. Binário para Decimal\n-> ").strip()

    if escolha == "1":
        try:
            numero = int(input("Digite um número decimal: "))
            if numero < 0:
                print("Por favor, digite um número inteiro não negativo.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue

        resultado = decimal_para_binario(numero)
        print(f"O número decimal {numero} em binário é: {resultado}")

    elif escolha == "2":
        binario = input("Digite um número binário: ").strip()
        if not all(c in '01' for c in binario):
            print("Entrada inválida. Por favor, digite um número binário válido.")
            continue

        resultado = binario_para_decimal(binario)
        print(f"O número binário {binario} em decimal é: {resultado}")

    else:
        print("Escolha inválida. Por favor, digite '1' ou '2'.")
        continue

    encerrarPrograma = input("Pressione Enter para finalizar ou qualquer outra tecla para voltar ao início: ").strip().lower()

    if encerrarPrograma == "":
        print("FINISH!")
        break
