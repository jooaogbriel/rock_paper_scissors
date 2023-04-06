import random 

def get_choices():
    player_choice = input("Faça sua escolha: ")
    options = ["pedra", "papel", "tesoura"]
    computer_choice = random.choice(options)
    choices ={"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"Você escolheu {player}, Computer escolheu {computer}")

    if player == computer:
        return "empate"
    
    elif player == "pedra":
        if computer == "tesoura":
            return "pedra quebra tesoura! você ganhou"
        else:
            return "papel embrulha pedra! você perdeu"
        
    elif player == "papel":
        if computer == "pedra":
            return "papel embrulha pedra! você ganhou"
        else:
            return "tesoura corta papel! você perdeu"
        
    elif player == "tesoura":
        if computer == "papel":
            return "tesoura corta papel! você ganhou"
        else:
            return "pedra quebra tesoura! você perdeu"
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
