import random

# In this game, there are two dice.
# Suppose two dice rolling randomly between number 1 to 6.
def roll_dice():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    return dice_1, dice_2

# Define the play turn of single player:
def play_turn(player_name, current_score):
    input(f'{player_name}, press Enter to roll dice.')
    dice_1, dice_2 = roll_dice()
    total_points = dice_1 + dice_2
    print(f'{player_name} rolled {dice_1} and {dice_2}. Total points of two dice is {total_points}.')

    if total_points % 2 == 1:
        current_score += total_points
        print(f"Odd number! {player_name} gains {total_points} points!")
    else:
        if current_score >= 3:
            current_score -= 3
        else:
            current_score = 0
        print(f"Even number! {player_name} loses 3 points!")

    print(f"{player_name}'s current points is {current_score}.\n")
    return current_score

# Play the full game. (Two players roll two dice.)
def play_game(player1_name, player2_name):
    score_1 = 0
    score_2 = 0
    while True:
        score_1 = play_turn(player1_name, score_1)
        if score_1 >= 30:
            print(f'{player1_name} wins the game! Congratulations!\n')
            break
        score_2 = play_turn(player2_name, score_2)
        if score_2 >= 30:
            print(f'{player2_name} wins the game! Congratulations!\n')
            break

def main():
    print('Welcome to the Dice Roll Battle Game!')
    player1_name = input("Enter name for Player 1: ")
    player2_name = input('Enter name for Player 2: ')
    while True:
        play_game(player1_name, player2_name)
        again_game = input('Do you want to play again? (yes/no): ').strip().lower()
        if again_game == 'no':
            print('Thanks for playing!')
            break
        elif again_game == 'yes':
            continue
        else:
            print('Invalid input. Exiting the game.')
            break

if __name__ == '__main__':
    main()

