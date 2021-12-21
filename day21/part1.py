#!/usr/bin/env python3

def dirac_die_roll():
    dirac_die = 1
    while True:
        yield dirac_die
        dirac_die += 1
        if dirac_die == 101: dirac_die = 1

if __name__ == '__main__':
    data = open('input').read().splitlines()
    points = [i + 1 for i in range(10)]
    player1_points = 0
    player2_points = 0

    print(data)
    print(points)

    player1_position = int(data[0].split(':')[1])
    player2_position = int(data[1].split(':')[1])

    print(player1_position)
    print(player2_position)

    dirac_rolls = 0
    dirac_die = dirac_die_roll()
    while player1_points < 1000 and player2_points < 1000:
        rolled = next(dirac_die) + next(dirac_die) + next(dirac_die)
        for _ in range(rolled):
            player1_position += 1
            if player1_position == 11:
                player1_position = 1
        player1_points += player1_position
        print(f'Player 1 total points: {player1_points}')

        if player1_points >= 1000:
            dirac_rolls += 3
            break
        
        rolled = next(dirac_die) + next(dirac_die) + next(dirac_die)
        for _ in range(rolled):
            player2_position += 1
            if player2_position == 11:
                player2_position = 1
        player2_points += player2_position
        print(f'Player 2 total points: {player2_points}')

        if player2_points >= 1000:
            dirac_rolls += 6
            break
        
        dirac_rolls += 6

    winning_score, losing_score = (player2_points, player1_points) if player1_points < player2_points else (player1_points, player2_points)
    print(f'Winning score: {winning_score}\nLosing score: {losing_score}\nDirac Die Rolls: {dirac_rolls}\nLosing * Rolls = {losing_score * dirac_rolls}')
