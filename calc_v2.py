def calcular_lucro(produto, CF, CV, IV, ML, Qlotes=0, Plotes=0):
    Venda = (produto / ((1 - ((CF / 100) + (CV / 100) + (IV / 100) + (ML / 100))) / 100) / 100)

    if Qlotes > 0:
        Venda *= Qlotes * Plotes

    llucro = int(((Venda - produto) * 100) / produto)
    
    return Venda, llucro

def imprimir_resultados(Venda, produto, CF, CV, IV, llucro):
    print('\n\nDescrição [valor/%]')
    print("A. Venda: R${:.2f}".format(Venda), '100%')
    Pp = (produto * 100 / Venda)
    print("B. Produto: R${:.2f}".format(produto), int(Pp), '%')
    CADM = (CF * 100 / Venda)
    print("C. Custos adm: R${:.2f};".format(CADM), CF, '%')
    CVE = (CV * 100 / Venda)
    print("D. Comissão de Vendas: R${:.2f};".format(CVE), CV, '%')
    I = (IV * 100 / Venda)
    print("E. Imposto: R${:.2f};".format(I), IV, '%')

    if llucro >= 0:
        print("O valor do Lucro foi ", llucro, '%')
    else:
        print('O valor do Lucro está negativo!')

    if llucro >= 20:
        print("O valor do Lucro foi alto")
    elif llucro >= 10:
        print("O valor do Lucro foi médio")
    elif llucro > 0:
        print("O valor do Lucro foi baixo")
    else:
        print('O valor do Lucro está equilibrado')

def main():
    while True:
        produto, CF, CV, IV, ML = 0, 0, 0, 0, 0

        try:
            produto = float(input("\n\nDigite o valor do produto [Em $]\n"))
            CF = float(input("\n\nDigite o valor do Custo Fixo/Administrativo [Em %]\n"))
            CV = float(input("\n\nDigite o valor do Comissão de Vendas [Em %]\n"))
            IV = float(input("\n\nDigite o valor Impostos [Em %]\n"))
            ML = float(input("\n\nDigite o valor da margem de lucro [Em %]\n"))
        except ValueError:
            print('Digite apenas números!')

        while True:
            lote = input("\n\nO produto é vendido em lote? [s/n]\n").lower()
            if lote in ['s', 'n']:
                break

        if lote == "s":
            Qlotes = int(input("\n\nQuantos lotes foram comprados?\n"))
            Plotes = int(input("\n\nQuantos produtos tem em cada lote?\n"))
            Venda, llucro = calcular_lucro(produto, CF, CV, IV, ML, Qlotes, Plotes)
        else:
            Venda, llucro = calcular_lucro(produto, CF, CV, IV, ML)

        imprimir_resultados(Venda, produto, CF, CV, IV, llucro)

        respostaContinuar = input('\nDeseja continuar? [S/N] ').lower()
        if respostaContinuar != 's':
            break

if __name__ == "__main__":
    main()
