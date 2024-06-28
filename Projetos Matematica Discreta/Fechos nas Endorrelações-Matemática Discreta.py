print("Fechos nas Endorrelações - MATEMÁTICA DISCRETA")

def obter_elementos_relacao():
    while True:
        elementos = input("Informe os pares da relação no formato (a,b) separados por vírgulas (ex: (1,2),(2,3)): ").strip()
        try:
            # Remover parênteses externos e dividir os pares
            elementos = elementos.replace('(', '').replace(')', '').split(',')
            relacao = {(int(elementos[i]), int(elementos[i + 1])) for i in range(0, len(elementos), 2)}
            return relacao
        except:
            print("Entrada inválida. Certifique-se de seguir o formato correto (a,b). Tente novamente.")

def verifica_propriedades(relacao):
    simetrica = all((b, a) in relacao for (a, b) in relacao)
    anti_simetrica = all((b, a) not in relacao or a == b for (a, b) in relacao)
    reflexiva = all((i, i) in relacao for i in {x for x, y in relacao}.union({y for x, y in relacao}))
    irreflexiva = all((i, i) not in relacao for i in {x for x, y in relacao}.union({y for x, y in relacao}))
    transitiva = all((a, c) in relacao for (a, b) in relacao for (b2, c) in relacao if b == b2)

    print(f"Simétrica: {simetrica}")
    print(f"Antissimétrica: {anti_simetrica}")
    print(f"Reflexiva: {reflexiva}")
    print(f"Irreflexiva: {irreflexiva}")
    print(f"Transitiva: {transitiva}")

while True:
    relacao = obter_elementos_relacao()
    print("A relação fornecida é:", relacao)
    verifica_propriedades(relacao)

    encerrarPrograma = input("Pressione Enter para finalizar ou qualquer outra tecla para voltar ao início: ").strip().lower()

    if encerrarPrograma == "":
        print("FINISH!")
        break
