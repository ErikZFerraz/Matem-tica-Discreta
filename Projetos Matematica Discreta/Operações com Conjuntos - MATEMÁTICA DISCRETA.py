print("Operações com Conjuntos - MATEMÁTICA DISCRETA")

while True:
    elementosA = input("Informe os elementos do conjunto A (separe-os por uma vírgula): ").strip()
    elementosB = input("Informe os elementos do conjunto B (separe-os por uma vírgula): ").strip()

    conjuntoA = {elemento.strip().lower() for elemento in elementosA.split(',')}
    conjuntoB = {elemento.strip().lower() for elemento in elementosB.split(',')}

    print("O conjunto A é:", conjuntoA)
    print("O conjunto B é:", conjuntoB)

    uniao = conjuntoA | conjuntoB
    print("União:", uniao)

    intersecao = conjuntoA & conjuntoB
    print("Interseção:", intersecao)

    diferenca = conjuntoA - conjuntoB
    print("Diferença A - B:", diferenca)

    subconjunto = conjuntoB <= conjuntoA
    print("Conjunto B é subconjunto de A:", subconjunto)

    encerrarPrograma = input("Pressione Enter para finalizar ou qualquer outra tecla para voltar ao início: ").strip().lower()

    if encerrarPrograma == "":
        print("FINISH!")
        break
