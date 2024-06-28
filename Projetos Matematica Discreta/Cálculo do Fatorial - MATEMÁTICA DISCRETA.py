print("Cálculo do Fatorial - MATEMÁTICA DISCRETA")

def obter_numero():
    while True:
        try:
            numero = int(input("Digite um número para calcular o fatorial: ").strip())
            if numero < 0:
                print("Por favor, digite um número não negativo.")
            else:
                return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

while True:
    numero = obter_numero()
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é: {resultado}")

    encerrarPrograma = input("Pressione Enter para finalizar ou qualquer outra tecla para calcular outro fatorial: ").strip().lower()
    if encerrarPrograma == "":
        print("FINISH!")
        break
