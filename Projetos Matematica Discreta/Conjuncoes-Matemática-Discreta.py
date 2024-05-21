print("Matemática Discreta - Conjuncoes")
print("OBS: Para que P -> Q = F, P deve ser 'V' e Q deve ser 'F'")

while True:
    print("Considerando p e q, informe se são 'V' (verdadeiro) ou 'F' (falso): ")
    p = input("P: ").strip().lower()
    q = input("Q: ").strip().lower()

    # Verifica se os valores inseridos estão corretos
    if p not in ['v', 'f'] or q not in ['v', 'f']:
        print("Valor inválido. Por favor, informe apenas 'V', 'v', 'F' ou 'f'.")
        continue

    # Calcula o resultado da implicação
    if p == 'v' and q == 'f':
        result = 'F'
    else:
        result = 'V'

    # Imprime o resultado da implicação
    print(f"P -> Q = {result}")

    encerrarPrograma = input("Pressione 'k' para finalizar ou qualquer outra tecla para voltar ao início: ").strip().lower()

    if encerrarPrograma == 'k':
        print("FINISH!")
        break
