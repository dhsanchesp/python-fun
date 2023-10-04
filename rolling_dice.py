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
        current_player = player + 1
        print(f'\nPlayer #{current_player}\'s turn.')
        print(f'#{current_player} - Your total score is: {score_board[player]}.\n')
        current_score = 0

        while True:
            should_roll = input(f'#{current_player} - Whould you like to roll the dice? (y/n): ')
            if should_roll.lower() != 'y':
                break

            value = roll_dice()
            if value == 1:
                print(f'#{current_player} - You lose your turn!')
                current_score = 0
                break
            else:
                current_score += value
                print(f'#{current_player} - You rolled a {value}.')
            print(f'#{current_player} - Your score for this turn is {current_score}.')
        
        score_board[player] += current_score
        print(f'Player #{current_player} - Your total score is {score_board[player]}.')

max_score = max(score_board)
winning_player = score_board.index(max_score) + 1
print(f'\nPlayer #{winning_player} wins with {max_score} points!')