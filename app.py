print('Bem-vindo ao nosso sistema de estoque')

def desenhar_coracao():
    coracao = [
        "  ***    ***  ",
        " *****  ***** ",
        "*************",
        " *********** ",
        "  *********  ",
        "   *******   ",
        "    *****    ",
        "     ***     ",
        "      *      "
    ]
    for linha in coracao:
        print(linha)

def main():
    resposta = input("Você quer que eu desenhe um coração? (sim/não): ")
    if resposta.lower() == "sim":
        desenhar_coracao()
    else:
        print("Ok, talvez da próxima vez!")

if __name__ == "__main__":
    main()


print('Obrigado por usar nosso programa')