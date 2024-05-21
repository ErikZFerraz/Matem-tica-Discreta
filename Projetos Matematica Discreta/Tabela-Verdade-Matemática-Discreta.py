print("Tabela Verdade - MATEMÁTICA DISCRETA")

def evaluate_expression(p, q, expression):
    # Substitui P e Q na expressão pelos seus valores booleanos
    expr = expression.replace("P", str(p)).replace("Q", str(q))
    # Avalia a expressão lógica
    return eval(expr)

def generate_truth_table(expression):
    print(f"Tabela Verdade para a expressão: {expression}")
    print(f"{'P':<5}{'Q':<5}{'Resultado':<10}")
    print("-" * 20)

    for p in [True, False]:
        for q in [True, False]:
            result = evaluate_expression(p, q, expression)
            p_str = 'V' if p else 'F'
            q_str = 'V' if q else 'F'
            result_str = 'V' if result else 'F'
            print(f"{p_str:<5}{q_str:<5}{result_str:<10}")

print("Gerador de Tabela Verdade - MATEMÁTICA DISCRETA")

while True:
    expression = input("Informe uma expressão lógica como P and Q ou P or not Q, usando P e Q (use 'and', 'or', 'not'): ").strip()
    
    if not expression:
        print("Nenhuma expressão informada. Por favor, informe uma expressão lógica.")
        continue

    generate_truth_table(expression)
            
    encerrarPrograma = input("Pressione Enter para finalizar ou qualquer outra tecla para continuar: ").strip().lower()

    if encerrarPrograma == "":
        print("FINISH!")
        break

