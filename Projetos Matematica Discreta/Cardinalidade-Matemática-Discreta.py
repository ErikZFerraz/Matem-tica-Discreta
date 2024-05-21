print("Cardinalidade - MATEMÁTICA DISCRETA")

while True:
    elementos = input("Informe os elementos do conjunto (obs: adicione vírgulas entre os elementos): ").strip()
    
    if not elementos:
        print("Nenhum elemento informado. Por favor, informe os elementos do conjunto.")
        continue

    conjunto = {elemento.strip().lower() for elemento in elementos.split(",")}
    cardinalidade = len(conjunto)
    
    print("O conjunto informado possui a cardinalidade =", cardinalidade)
            
    encerrarPrograma = input("Pressione Enter para finalizar ou qualquer outra tecla para voltar ao início: ").strip().lower()

    if encerrarPrograma == "":
        print("FINISH!")
        break
