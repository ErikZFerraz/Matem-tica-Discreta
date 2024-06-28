print("Permutações - MATEMÁTICA DISCRETA")

def gerar_permutacoes(elementos):
    resultado = []
    gerar(elementos, 0, resultado)
    return resultado

def gerar(elementos, indice, resultado):
    if indice >= len(elementos):
        resultado.append(elementos[:])
        return
    for i in range(indice, len(elementos)):
        elementos[indice], elementos[i] = elementos[i], elementos[indice]
        gerar(elementos, indice + 1, resultado)
        elementos[indice], elementos[i] = elementos[i], elementos[indice]

while True:
    elementos = input("Informe os elementos do conjunto (separe-os por uma vírgula): ").strip()

    conjunto = [elemento.strip() for elemento in elementos.split(',')]
    
    try:
        conjunto = [int(elemento) for elemento in conjunto]
    except ValueError:
        print("Por favor, insira apenas números inteiros.")
        continue

    permutacoes = gerar_permutacoes(conjunto)
    
    print("Todas as permutações:")
    for permutacao in permutacoes:
        print(permutacao)

    encerrarPrograma = input("Pressione Enter para finalizar ou qualquer outra tecla para voltar ao início: ").strip().lower()

    if encerrarPrograma == "":
        print("FINISH!")
        break
