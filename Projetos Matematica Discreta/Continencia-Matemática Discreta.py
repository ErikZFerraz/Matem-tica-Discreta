print("Continencia - MATEMÁTICA DISCRETA")

while True:
    elementosA = input("Informe os elementos do conjunto A (separe-os por uma vírgula): ").strip()
    elementosB = input("Informe os elementos do conjunto B (separe-os por uma vírgula): ").strip()

    conjuntoA = {elemento.strip().lower() for elemento in elementosA.split(',')}
    conjuntoB = {elemento.strip().lower() for elemento in elementosB.split(',')}

    print("O conjunto A é:", conjuntoA)
    print("O conjunto B é:", conjuntoB)

    if conjuntoA <= conjuntoB:
        print("O conjunto A é um subconjunto de B.")
    else:
        print("O conjunto A não é um subconjunto de B.")

    if conjuntoB <= conjuntoA:
        print("O conjunto B é um subconjunto de A.")
    else:
        print("O conjunto B não é um subconjunto de A.")

    encerrarPrograma = input("Pressione '*' para finalizar ou qualquer outra tecla para voltar ao início: ").strip().lower()

    if encerrarPrograma == "*":
        print("FINISH!")
        break
