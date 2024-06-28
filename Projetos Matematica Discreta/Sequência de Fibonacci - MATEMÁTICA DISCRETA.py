print("Sequência de Fibonacci - MATEMÁTICA DISCRETA")

def obter_quantidade_termos():
    while True:
        try:
            quantidade = int(input("Digite a quantidade de termos da sequência Fibonacci: ").strip())
            if quantidade < 0:
                print("Por favor, digite um número não negativo.")
            else:
                return quantidade
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def calcular_fibonacci(n):
    if n <= 1:
        return n
    anterior, atual = 0, 1
    for _ in range(2, n + 1):
        anterior, atual = atual, anterior + atual
    return atual

while True:
    quantidade_termos = obter_quantidade_termos()
    print(f"Os primeiros {quantidade_termos} termos da sequência de Fibonacci são:")
    for i in range(quantidade_termos):
        print(calcular_fibonacci(i), end=' ')
    print()  # Para adicionar uma nova linha após a sequência

    encerrarPrograma = input("Pressione Enter para finalizar ou qualquer outra tecla para calcular outra sequência: ").strip().lower()
    if encerrarPrograma == "":
        print("FINISH!")
        break
