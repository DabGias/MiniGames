import random


def rock_papers_scissors():
    print("----- Jogando: Jokempo -----")

    computer_tuple = ("Pedra", "Papel", "Tesoura")
    player_tuple = ("Pedra", "Papel", "Tesoura")
    random_index = random.randint(0, 2)
    player_index = int(input("""Opções: 
- Pedra (1)
- Papel (2)
- Tesoura (3)

Qual a sua escolha? """))
    while player_index > 3 or player_index < 1:
        print("Opção inválida!!!")
        player_index = int(input("""Opções: 
- Pedra (1)
- Papel (2)
- Tesoura (3)

Qual a sua escolha? """))

    computer_decision = computer_tuple[random_index]
    player_decision = player_tuple[player_index - 1]

    if computer_decision == player_decision:
        print("Você escolheu '{}' contra '{}'".format(player_decision, computer_decision))
        print("{}Empate!{}".format('\033[33m', '\033[0;0m'))

    elif computer_decision == "Pedra" and player_decision == "Tesoura":
        print("Você escolheu '{}' contra '{}'".format(player_decision, computer_decision))
        print("{}Você perdeu!{}".format('\033[31m', '\033[0;0m'))

    elif computer_decision == "Pedra" and player_decision == "Papel":
        print("Você escolheu '{}' contra '{}'".format(player_decision, computer_decision))
        print("{}Você ganhou!{}".format('\033[32m', '\033[0;0m'))

    elif computer_decision == "Papel" and player_decision == "Pedra":
        print("Você escolheu '{}' contra '{}'".format(player_decision, computer_decision))
        print("{}Você perdeu!{}".format('\033[31m', '\033[0;0m'))

    elif computer_decision == "Papel" and player_decision == "Tesoura":
        print("Você escolheu '{}' contra '{}'".format(player_decision, computer_decision))
        print("{}Você ganhou!{}".format('\033[32m', '\033[0;0m'))

    elif computer_decision == "Tesoura" and player_decision == "Papel":
        print("Você escolheu '{}' contra '{}'".format(player_decision, computer_decision))
        print("{}Você perdeu!{}".format('\033[31m', '\033[0;0m'))

    elif computer_decision == "Tesoura" and player_decision == "Pedra":
        print("Você escolheu '{}' contra '{}'".format(player_decision, computer_decision))
        print("{}Você ganhou!{}".format('\033[32m', '\033[0;0m'))
