print("Matemática Discreta - Bicondicional (<->)")
print("Analizando 'P se e somente se Q'.")

while True:
    p = input("Qual o valor de P (V para Verdadeiro, F para Falso): ").strip().upper()
    q = input("Qual o valor de Q (V para Verdadeiro, F para Falso): ").strip().upper()

    # Verifica se os valores inseridos estão corretos
    if p not in ['V', 'F'] or q not in ['V', 'F']:
        print("Valor inválido. Por favor, informe apenas 'V' ou 'F'.")
        continue

    # Calcula o resultado da implicação
    result = (p == q)

    # Imprime o resultado da implicação
    if result:
        print("P <-> Q = V")
    else:
        print("P <-> Q = F")

    encerrarPrograma = input("Pressione '*' para sair ou qualquer outra tecla para continuar: ")

    if encerrarPrograma.lower() == "*":
        print("Programa finalizado!")
        break
