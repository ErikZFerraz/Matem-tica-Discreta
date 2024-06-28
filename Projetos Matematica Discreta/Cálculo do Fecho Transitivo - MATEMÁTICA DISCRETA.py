print("Cálculo do Fecho Transitivo - MATEMÁTICA DISCRETA")

def obter_matriz_adjacencia():
    while True:
        try:
            n = int(input("Digite o tamanho da matriz de adjacência (n x n): ").strip())
            if n <= 0:
                print("Por favor, digite um número positivo.")
                continue
            matriz = []
            for i in range(n):
                linha = input(f"Digite a linha {i+1} da matriz, separada por espaços: ").strip().split()
                if len(linha) != n:
                    print(f"A linha deve conter exatamente {n} elementos.")
                    break
                matriz.append([int(x) for x in linha])
            if len(matriz) == n:
                return matriz
            else:
                print("Houve um erro na entrada da matriz. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros.")

def calcular_fecho_transitivo(matriz):
    tamanho = len(matriz)
    fecho_transitivo = [linha[:] for linha in matriz]

    for k in range(tamanho):
        for i in range(tamanho):
            for j in range(tamanho):
                fecho_transitivo[i][j] |= fecho_transitivo[i][k] & fecho_transitivo[k][j]

    print("Fecho Transitivo:")
    for linha in fecho_transitivo:
        print(' '.join(map(str, linha)))

while True:
    matriz_adjacencia = obter_matriz_adjacencia()
    print("A matriz de adjacência fornecida é:")
    for linha in matriz_adjacencia:
        print(' '.join(map(str, linha)))

    calcular_fecho_transitivo(matriz_adjacencia)

    encerrarPrograma = input("Pressione Enter para finalizar ou qualquer outra tecla para calcular outro fecho transitivo: ").strip().lower()
    if encerrarPrograma == "":
        print("FINISH!")
        break
