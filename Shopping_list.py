#C:/Users/pedro/AppData/Local/Programs/Python/Python312/python.exe c:/Users/pedro/OneDrive/Documentos/commit/linkedlist/Shopping_list.py
import random

class Node:
    def __init__(self, item_name):
        self.item_name = item_name
        self.next = None

class ShoppingList:
    def __init__(self):
        self.head = None
    def add_itens(self, item_name):
        new_item = Node(item_name)
        if not self.head:
            self.head = new_item
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = new_item
    def traveser(self):
        if not self.head:
            print('Sem itens na lista.')
        else:
            pointer = self.head
            print("Shopping List: ")
            while pointer:
                print(f"- {pointer.item_name} -")
                pointer = pointer.next
    def delete(self, item_name):
        if self.head == None:
            raise ValueError("is not in list")
        elif self.head.item_name == item_name:
            self.head = self.head.next
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.item_name == item_name:
                  ancestor.next = pointer.next
                  pointer.next = None

                ancestor = pointer
                pointer = pointer.next
            return True
    def search(self, item_name):
        pointer = self.head
        while pointer:
            if pointer.item_name == item_name:
                return print(f"{item_name} está na lista.")
            pointer = pointer.next
        return print(f"{item_name} nã oestá na lista.")


Caixa = ShoppingList()   
carrinho = []
quantidade_de_produtos = random.randint(2,11)

print("_" * 10, "SHOPPING LIST", "_"*10)
opcao1 = input(
    "\n# PARA INICIAR O PROGRAMA DIGITE Y \n# PARA ENCERRAR O PROGRMA DIGITE N \n")

while True:
    if opcao1.upper() == "Y":
        print("\n# PROGRAMA INICIADO \n")
        
        print("1 : ADICONAR ITENS A LISTA")
        print("2 : VER LISTA")
        print("3 : DELETAR ITEM DA LISTA")
        print("4 : CONFERIR ITEM NA LISTA")
        print("5 : ENCHAERRAR PROGRAMA")

        opcao = int(input("Diga qual foi a opcao escolhida? "))

        if opcao == 1:
            print("Adiconando itens ao seu carinho.")
            for i in range(quantidade_de_produtos):
                produtos = input("Escolha o seus produtos.")
                carrinho.append(produtos)
            for produto in carrinho:
                Caixa.add_itens(produto)
            print('Itens adcionados. ')
            opcao2 = input(
                "\n# DESEJA REINICIALIZAR O PROGRAMA?\nY PARA SIM E N PARA NAO\n")

            if opcao2.upper() == "Y":
                print("\n# PROGRAMA REINICIADO")
                continue
            elif opcao2.upper() == "N":
                print("\n# PROGRAMA ENCERRADO")
                break

        elif opcao == 2:
            Caixa.traveser()
            opcao2 = input(
                "\n# DESEJA REINICIALIZAR O PROGRAMA?\nY PARA SIM E N PARA NAO\n")

            if opcao2.upper() == "Y":
                print("\n# PROGRAMA REINICIADO")
                continue
            elif opcao2.upper() == "N":
                print("\n# PROGRAMA ENCERRADO")
                break

        elif opcao == 3:
            
            opcao3 = input("item que deseja remover:")

            Caixa.delete(opcao3)
        
            opcao2 = input(
                "\n# DESEJA REINICIALIZAR O PROGRAMA?\nY PARA SIM E N PARA NAO\n")

            if opcao2.upper() == "Y":
                print("\n# PROGRAMA REINICIADO")
                continue
            elif opcao2.upper() == "N":
                print("\n# PROGRAMA ENCERRADO")
                break

        elif opcao == 4:
            
            opcao4 = input("item que deseja conferir:")

            Caixa.delete(opcao4)
        
            opcao2 = input(
                "\n# DESEJA REINICIALIZAR O PROGRAMA?\nY PARA SIM E N PARA NAO\n")

            if opcao2.upper() == "Y":
                print("\n# PROGRAMA REINICIADO")
                continue
            elif opcao2.upper() == "N":
                print("\n# PROGRAMA ENCERRADO")
                break


        elif opcao == 5:
            print("Programa encherrado")
            break

    elif opcao1.upper() == "N":
        print("\n# PROGRAMA ENCERRADO")
        break
    else:
        print("erro, digite uma opcao valida.")