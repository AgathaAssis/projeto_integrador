continuar=True
while (continuar):

    produto=0
    CF=0
    CV=0
    IV=0
    ML=0
    lote=0
    Qlotes=0
    Plotes=0




    try:
            produto=float(input("\n\nDigite o valor do produto [Em $]\n"))
            CF=float(input("\n\nDigite o valor do Custo Fixo/Administrativo [Em %]\n"))
            CV=float(input("\n\nDigite o valor do Comissão de Vendas [Em %]\n"))
            IV=float(input("\n\nDigite o valor Impostos [Em %]\n"))
            ML=float(input("\n\nDigite o valor da margem de lucro [Em %]\n"))


    except: print('Digite apenas numeros!')


    while True:

            lote=input("\n\nO produto é vendido em lote? [s/n]\n").lower()

            if (lote == 'n' or lote == 's'):
                break

    if lote== "s":
        Qlotes=int(input("\n\nQuantos lotes foram comprandos?\n"))
        Plotes=int(input("\n\nQuantos produtos tem em cada lote?\n"))


        Venda=(produto/((1-((CF/100)+(CV/100)+(IV/100)+(ML/100)))/100)/100)


        Lucro = (Venda - produto) * (Qlotes * Plotes)
        llucro = int(((Lucro * 100) / (produto * (Qlotes * Plotes))))

        print('\n\nDescrição  [valor/%]')
        print("A.Venda: R${:.2f}".format(Venda), '100%')

        Pp=(produto*100/Venda)

        print("B.Produto: R${:.2f}".format(produto),int(Pp),'%')


        CADM=(CF*100/Venda)

        print("C.Custos adm: R${:.2f};".format(CADM),CF,'%')


        CVE=(CV*100/Venda)

        print("D.Comissão de Vendas: R${:.2f};".format(CVE),CV,'%')


        I=(IV*100/Venda)

        print("E.Imposto: R${:.2f};".format(I),IV,'%')

        RB = Venda - produto

        PRB = (RB * 100 / Venda)

        print("F.Receita Bruta: R${:.2f};".format(RB), int(PRB), '%')

        Oc = CADM + I + CVE

        POc = ((Oc / 100) * Venda)
        print("G.Outros Custos: R${:.2f};".format(Oc), int(POc), '%')

    else:
        Venda=(produto/((1-((CF/100)+(CV/100)+(IV/100)+(ML/100)))/100)/100)


        Lucro = Venda - produto
        llucro = int(((Lucro / 100) * produto))

        print('\n\nDescrição  [valor/%]')
        print("A.Venda: R${:.2f};".format(Venda), '100%')

        Pp=(produto*100/Venda)

        print("B.Produto: R${:.2f};".format(produto),int(Pp),'%')


        CADM=(CF/100*Venda)

        print("C.Custos adm: R${:.2f};".format(CADM),CF,'%')


        CVE=(CV/100*Venda)

        print("D.Comissão de Vendas: R${:.2f};".format(CVE),CV,'%')


        I=(IV/100*Venda)

        print("E.Imposto: R${:.2f};".format(I),IV,'%')

        RB = Venda - produto

        PRB = (RB*100/Venda)

        print("F.Receita Bruta: R${:.2f};".format(RB), int(PRB), '%')

        Oc = (CVE + I + CADM)

        POc = (Oc * 100 / Venda)
        print("G.Outros Custos: R${:.2f};".format(Oc), int(POc), '%')

        Ren=RB-Oc

        PRen = (Ren * 100 / Venda)

        print("H.Rentabilidade: R${:.2f}".format(Ren), int(PRen), '%')


    print("\nO valor do Lucro foi ",llucro,'%')
    print("O valor do Lucro foi R${:.2f}".format(Lucro))


    if(llucro<0):
        print('O valor do Lucro está negativo!')

    if llucro >= 20:
        print("O valor do Lucro foi alto")
    elif llucro >= 10:
        print("O valor do Lucro foi médio")
    elif llucro > 0:
        print("O valor do Lucro foi baixo")
    else:
        print('O valor do Lucro está equilibrado')

    while True:
        respostaContinuar = input('\nDeseja continuar? [S/N] ').lower()

        if(respostaContinuar == 'n' or respostaContinuar=='s'):
            break


    if respostaContinuar =='s':
        continuar=True
    elif respostaContinuar =='n':
        continuar=False
    else:
        continuar=False










