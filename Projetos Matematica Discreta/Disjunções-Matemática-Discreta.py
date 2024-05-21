print("Disjunções - MATEMÁTICA DISCRETA")
print("OBS: Para que P v Q = V, pelo menos 1 dos valores precisa ser = V.")

while True:
    print("Considerando p e q, informe se são 'V' (verdadeiro) ou 'F' (falso): ")
    p = input("P: ").strip().lower()
    q = input("Q: ").strip().lower()

    # Verifica se os valores inseridos estão corretos
    if p not in ['v', 'f'] or q not in ['v', 'f']:
        print("Valor inválido. Por favor, informe apenas 'V', 'v', 'F' ou 'f'.")
        continue

    # Calcula o resultado da disjunção
    if p == 'v' or q == 'v':
        result = 'V'
    else:
        result = 'F'

    # Imprime o resultado da disjunção
    print(f"P v Q = {result}")

    encerrarPrograma = input("Pressione Enter para finalizar ou qualquer outra tecla para voltar ao início: ").strip().lower()

    if encerrarPrograma == "":
        print("Finish!")
        break
