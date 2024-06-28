print("Prova por Indução Matemática - MATEMÁTICA DISCRETA")

def soma_numeros(n):
    return n * (n + 1) // 2

def prova_inducao(n):
    soma_calculada = sum(range(1, n + 1))
    soma_formula = soma_numeros(n)
    return soma_calculada == soma_formula

while True:
    try:
        numero = int(input("Digite um número inteiro positivo para a prova: "))
        if numero < 1:
            print("Por favor, digite um número inteiro positivo.")
            continue
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro positivo.")
        continue

    if prova_inducao(numero):
        print(f"A soma dos primeiros {numero} números naturais é igual a {soma_numeros(numero)}, como esperado.")
        print(f"1 + 2 + 3 + ... + {numero} = {soma_numeros(numero)}")
    else:
        print(f"Houve um erro na prova por indução para n = {numero}.")

    encerrarPrograma = input("Pressione Enter para finalizar ou qualquer outra tecla para voltar ao início: ").strip().lower()

    if encerrarPrograma == "":
        print("FINISH!")
        break
