import random

def roll_dice():
    min_val = 1
    max_val = 6
    return random.randint(min_val, max_val)

while True:
    players = input("How many players?(2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number between 2 and 4.")
    else:
        print("Please enter a valid number.")

print(f'Number of players: {players}')

max_score = 50
score_board = [0 for _ in range(players)]

while max(score_board) < max_score:

    for player in range(players):
        print(f'\nPlayer #{player + 1}\'s turn.')
        print(f'Your total score is: {score_board[player]}.\n')
        current_score = 0

        while True:
            should_roll = input("Whould you like to roll the dice? (y/n): ")
            if should_roll.lower() != 'y':
                break

            value = roll_dice()
            if value == 1:
                print("You lose your turn!")
                current_score = 0
                break
            else:
                current_score += value
                print(f'You rolled a {value}.')
            print(f'Your score is {current_score}.')
        
        score_board[player] += current_score
        print(f'Player #{player +1} - Your total score is {score_board[player]}.')

max_score = max(score_board)
winning_player = score_board.index(max_score) + 1
print(f'\nPlayer #{winning_player} wins with {max_score} points!')