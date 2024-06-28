print("Cálculo de Função - MATEMÁTICA DISCRETA")

def calcular_funcao(x):
    return x ** 2 + 3 * x - 7

while True:
    try:
        x = float(input("Digite um valor para x: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        continue

    resultado = calcular_funcao(x)
    print(f"O resultado da função f(x) = x^2 + 3x - 7 é: {resultado}")

    encerrarPrograma = input("Pressione Enter para finalizar ou qualquer outra tecla para voltar ao início: ").strip().lower()

    if encerrarPrograma == "":
        print("FINISH!")
        break
