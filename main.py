import time

lancamentos = [
    ['mouse', 'periférico', 34.99], 
    ['monitor', 'visual', 179.99],
    ['fone', 'audio', 78.99],
    ['teclado', 'periférico', 89.99],
    ['micro-tela', 'visual', 69.99]
    ]

while True:
    print("===== SHEETFLOW =====")
    print("1 - Listar lançamentos")
    print("2 - Adicionar lançamento")
    print("3 - Total geral")
    print("4 - Total de uma categoria")
    print("5 - Maior e menor lançamento")
    print("0 - Sair")

    
    opcao = input("Escolha uma opção: ")

    if opcao in ["1", "2", "3", "4", "5"]:
        print("Em construção, voltando ao menu....")
        time.sleep(1)
    
    elif opcao == "0":
        print("Saindo do sheetflow...")
        break

    else:
        print("Opção inválida, tente novamente...")
        time.sleep(1)