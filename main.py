print("_" * 10, "CALCULADORA", "_"*10)
opcao1 = input(
    "\n# PARA INICIAR O PROGRAMA DIGITE Y \n# PARA ENCERRAR O PROGRMA DIGITE N \n")


def soma(valor1, valor2):
    return valor1 + valor2


def subtracao(valor1, valor2):
    if valor1 < valor2:
        return valor2 - valor1
    else:
        return valor1 - valor2


def multiplicacao(valor1, valor2):
    return valor1 * valor2


def divisao(valor1, valor2):
    return valor1 / valor2


while True:

    if opcao1.upper() == "Y":
        print("\n# PROGRAMA INICIADO \n")
        definir_valor1 = float(input("Digite o valor1: "))
        definir_valor2 = float(input("Digite o valor2: "))
        print("1 : SOMA")
        print("2 : SUBITRACAO")
        print("3 : MULTIPLICACAO")
        print("4 : DIVISAO")

        opcao = int(input("Diga qual foi a opcao escolhida? "))
        

        if opcao == 1:
            
            resultado = soma(definir_valor1, definir_valor2)
            print("{:,.2f}".format(resultado))
            opcao2 = input(
                "\n# DESEJA REINICIALIZAR O PROGRAMA?\nY PARA SIM E N PARA NAO\n")

            if opcao2.upper() == "Y":
                print("\n# PROGRAMA REINICIADO")
                continue
            elif opcao2.upper() == "N":
                print("\n# PROGRAMA ENCERRADO")
                break
        elif opcao == 2:
            
            resultado = subtracao(definir_valor1, definir_valor2)
            print("{:,.2f}".format(resultado))
            opcao2 = input(
                "\n# DESEJA REINICIALIZAR O PROGRAMA?\nY PARA SIM E N PARA NAO\n")

            if opcao2.upper() == "Y":
                print("\n# PROGRAMA REINICIADO")
                continue
            elif opcao2.upper() == "N":
                print("\n# PROGRAMA ENCERRADO")
                break
        elif opcao == 3:
            
            resultado = multiplicacao(definir_valor1, definir_valor2)
            print("{:,.2f}".format(resultado))
            opcao2 = input(
                "\n# DESEJA REINICIALIZAR O PROGRAMA?\nY PARA SIM E N PARA NAO\n")

            if opcao2.upper() == "Y":
                print("\n# PROGRAMA REINICIADO")
                continue
            elif opcao2.upper() == "N":
                print("\n# PROGRAMA ENCERRADO")
                break
        elif opcao == 4:
            
            resultado = divisao(definir_valor1, definir_valor2)
            print("{:,.2f}".format(resultado))
            opcao2 = input(
                "\n# DESEJA REINICIALIZAR O PROGRAMA?\nY PARA SIM E N PARA NAO\n")

            if opcao2.upper() == "Y":
                print("\n# PROGRAMA REINICIADO")
                continue
            elif opcao2.upper() == "N":
                print("\n# PROGRAMA ENCERRADO")
                break
        else:
            print("erro, digite uma opcao valida.")
    elif opcao1.upper() == "N":
        print("\n# PROGRAMA ENCERRADO")
        break
    else:
        print("erro, digite uma opcao valida.")