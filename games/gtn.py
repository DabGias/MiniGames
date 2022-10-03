import random


def guess_number():
    print("----- Jogando: Adivinha o número -----")

    count_tries = 1
    random_num = random.randint(0, 100)
    guess = int(input("Digite o seu chute: "))

    while guess != random_num:
        if guess > random_num:
            print("O seu chute é maior que o número secreto!")
            guess = int(input("Digite o seu chute: "))

        if guess < random_num:
            print("O seu chute é menor que o número secreto!")
            guess = int(input("Digite o seu chute: "))

        count_tries += 1

    print("{}Você acertou!!!{} O número secreto era {}{}{} e você precisou de {}{}{} tentativa(s)"
          .format('\033[32m', '\033[0;0m', '\033[32m', random_num, '\033[0;0m', '\033[34m', count_tries, '\033[0;0m'))
