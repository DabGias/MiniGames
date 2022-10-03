from games.gtn import guess_number
from games.rps import rock_papers_scissors
from games.wordle import wordle

if __name__ == "__main__":
    option = input("""----- Jogos -----
    - Adivinhe o número (1)
    - Jokempo (2)
    - Wordle (3)
    - Sair (4 ou 'Q')
    
    Escolha um jogo: """).upper().strip()

    while option != "5" and option != "Q":
        while int(option) > 6 or int(option) < 1:
            print("Opção inválida!!!")
            option = input("""----- Jogos -----
    - Adivinhe o número (1)
    - Jokempo (2)
    - Wordle (3)
    - Conecte quatro (4)
    - Jogo da velha (5)
    - Sair (4 ou 'Q')
    
    Escolha um jogo: """).upper().strip()

        if option == "1":
            guess_number()

        if option == "2":
            rock_papers_scissors()

        if option == "3":
            wordle()

        option = input("""----- Jogos -----
    - Adivinhe o número (1)
    - Jokempo (2)
    - Wordle (3)
    - Sair (4 ou 'Q')
    
    Escolha um jogo: """).upper().strip()

    print("Saindo da aplicação!")
