num = 0

def JogoAdivinhacao(num):

    import random

    num = random.randint(1,100)
    Tentativas = 3
    while(Tentativas > 0):
        Tentativas = Tentativas - 1
        Usuario = int(input("Digite qualquer número de 1 a 100:"))

        if(num > Usuario):
            print("O número secreto é maior que este!")
        elif(num < Usuario):
            print("O número secreto é menor que este!")
        elif(num == Usuario):
            print("Parabéns, você conseguiu acertar qual era o número secreto!")
            

        if(Tentativas == 0):
            print("Você perdeu, não foi dessa vez!")
            print("O número secreto era:",num)

            print("Digite 1 para Jogar Novamente ou 2 para Sair do jogo!")
            Opcao = int(input(""))
            if(Opcao == 1):
                JogoAdivinhacao(num)
            elif(Opcao == 2):
                print("Fim de Jogo!")
        elif(Tentativas == -1):
            input()

def menu():
    print("Digite 1 para Jogar ou 2 para as Regras!")
    OpcaoMenu = int(input(""))
    if(OpcaoMenu == 1):
        JogoAdivinhacao(num)
    elif(OpcaoMenu == 2):
        print("As regras do jogo são bastante simples!")
        print("A máquina irá sortear um número de 1 a 100!")
        print("E o usuário (você) terá que adivinhar qual será esse número secreto!")
        print("Ah!,e você terá apenas 3 chances!")

        print("Digite 1 para Jogar ou 2 para Sair do Jogo!")
        OpcaoMenu = int(input(""))
        if(OpcaoMenu == 1):
            JogoAdivinhacao(num)
        elif(OpcaoMenu == 2):
            print("Fim de jogo!")
menu()

        

    
