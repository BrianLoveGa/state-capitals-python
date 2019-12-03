from capitals import states
import random

# correct +=1
# wrong +=5

# print(f"# correct = {correct} and number incorrect = {wrong} \n")
# print(states)
print("Welcome to the states and Capitals game. You'll be given a State, enter the Capital if you know it. Type it with a Cap letter where appropriate... ex...atlanta incorrect Atlanta correct")

def states_caps_game():
    random.shuffle(states)
    correct = 0
    wrong = 0
    hint = 'hint'

    for state in states:
        this_state = state['name']
        this_capital = state['capital']
        print("remember to Capatialize .. atlanta incorrect but Atlanta correct")
        print(" Your current question is below ... ")
        user_input = input(
            f"What is the capital of {this_state}? You stuck? type hint for a clue\n")

        if user_input == hint:
            user_input = input(
                f"What is the capital of {this_state}? ... hint it starts with ... {this_capital[0]}{this_capital[1]}{this_capital[2]}\n")
            if user_input == this_capital:
                correct += 1
                print(
                    f" you got it right ... # correct = {correct} and number incorrect = {wrong} \n")
            else:
                wrong += 1
                print(
                    f" that was not right it was {this_capital}... # correct = {correct} and number incorrect = {wrong} \n")
        elif user_input == this_capital:
            correct += 1
            print(
                f" you got it right ... # correct = {correct} and number incorrect = {wrong} \n")
        else:
            wrong += 1
            print(
                f" that was not right it was {this_capital}... # correct = {correct} and number incorrect = {wrong} \n")

    print(
        f"That's all of them . Final score for you was ... # correct = {correct} and number incorrect = {wrong} \n")

    play_again = input("Wanna do it all over again? type yes or no \n")
    if play_again == "yes":
        states_caps_game()
    else:
        print("Well so long now and bye-bye then... thanks for playing")
        exit()

states_caps_game()
