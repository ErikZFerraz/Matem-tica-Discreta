print("Matemática Discreta - Condicional (->)")
print("Analisando 'P implica Q'.")

while True:
    p = input("Qual o valor de P (V para Verdadeiro, F para Falso): ").strip().lower()
    q = input("Qual o valor de Q (V para Verdadeiro, F para Falso): ").strip().lower()

    # Verifica se os valores inseridos estão corretos
    if p not in ['v', 'f'] or q not in ['v', 'f']:
        print("Valor inválido. Por favor, informe apenas 'V', 'v', 'F' ou 'f'.")
        continue

    # Calcula o resultado da implicação
    result = (p == 'f' or q == 'v')

    # Imprime o resultado da implicação
    if result:
        print("P -> Q = V")
    else:
        print("P -> Q = F")

    encerrarPrograma = input("Pressione '*' para sair ou qualquer outra tecla para continuar: ")

    if encerrarPrograma.lower() == "*":
        print("Programa finalizado!")
        break
