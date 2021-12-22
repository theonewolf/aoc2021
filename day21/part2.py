#!/usr/bin/env python3

def dirac_die_roll():
    dirac_die = 1
    while True:
        yield dirac_die
        dirac_die += 1
        if dirac_die == 101: dirac_die = 1

def play(p1_position, p2_position, p1_score, p2_score, die_roll, p1_turn, p2_turn, p1_wins, p2_wins, depth):
    if p1_turn:
        for _ in range(die_roll):
            p1_position += 1
            if p1_position == 11:
                p1_position = 1
        p1_score += p1_position
        if p1_score >= 21:
            return p1_wins + 1, p2_wins

        # Counter({6: 7, 5: 6, 7: 6, 4: 3, 8: 3, 3: 1, 9: 1})
        r1_p1_wins, r1_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 3, False, True, p1_wins, p2_wins, depth + 1)
        r2_p1_wins, r2_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 4, False, True, p1_wins, p2_wins, depth + 1)
        r3_p1_wins, r3_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 5, False, True, p1_wins, p2_wins, depth + 1)
        r4_p1_wins, r4_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 6, False, True, p1_wins, p2_wins, depth + 1)
        r5_p1_wins, r5_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 7, False, True, p1_wins, p2_wins, depth + 1)
        r6_p1_wins, r6_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 8, False, True, p1_wins, p2_wins, depth + 1)
        r7_p1_wins, r7_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 9, False, True, p1_wins, p2_wins, depth + 1)
        p1_wins += r1_p1_wins + r2_p1_wins * 3 + r3_p1_wins * 6 + r4_p1_wins * 7 + r5_p1_wins * 6 + r6_p1_wins * 3 + r7_p1_wins
        p2_wins += r1_p2_wins + r2_p2_wins * 3 + r3_p2_wins * 6 + r4_p2_wins * 7 + r5_p2_wins * 6 + r6_p2_wins * 3 + r7_p2_wins
        return p1_wins, p2_wins

    if p2_turn:
        for _ in range(die_roll):
            p2_position += 1
            if p2_position == 11:
                p2_position = 1
        p2_score += p2_position
        if p2_score >= 21:
            return p1_wins, p2_wins + 1

        # Counter({6: 7, 5: 6, 7: 6, 4: 3, 8: 3, 3: 1, 9: 1})
        r1_p1_wins, r1_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 3, True, False, p1_wins, p2_wins, depth + 1)
        r2_p1_wins, r2_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 4, True, False, p1_wins, p2_wins, depth + 1)
        r3_p1_wins, r3_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 5, True, False, p1_wins, p2_wins, depth + 1)
        r4_p1_wins, r4_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 6, True, False, p1_wins, p2_wins, depth + 1)
        r5_p1_wins, r5_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 7, True, False, p1_wins, p2_wins, depth + 1)
        r6_p1_wins, r6_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 8, True, False, p1_wins, p2_wins, depth + 1)
        r7_p1_wins, r7_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 9, True, False, p1_wins, p2_wins, depth + 1)
        p1_wins += r1_p1_wins + r2_p1_wins * 3 + r3_p1_wins * 6 + r4_p1_wins * 7 + r5_p1_wins * 6 + r6_p1_wins * 3 + r7_p1_wins
        p2_wins += r1_p2_wins + r2_p2_wins * 3 + r3_p2_wins * 6 + r4_p2_wins * 7 + r5_p2_wins * 6 + r6_p2_wins * 3 + r7_p2_wins
        return p1_wins, p2_wins


if __name__ == '__main__':
    data = open('input').read().splitlines()

    p1_position = int(data[0].split(':')[1])
    p2_position = int(data[1].split(':')[1])

    print(p1_position)
    print(p2_position)

    p1_wins = 0
    p2_wins = 0
    p1_score = 0
    p2_score = 0
    p1_wins = 0
    p2_wins = 0
    depth = 0
    r1_p1_wins, r1_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 3, True, False, p1_wins, p2_wins, depth + 1)
    r2_p1_wins, r2_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 4, True, False, p1_wins, p2_wins, depth + 1)
    r3_p1_wins, r3_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 5, True, False, p1_wins, p2_wins, depth + 1)
    r4_p1_wins, r4_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 6, True, False, p1_wins, p2_wins, depth + 1)
    r5_p1_wins, r5_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 7, True, False, p1_wins, p2_wins, depth + 1)
    r6_p1_wins, r6_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 8, True, False, p1_wins, p2_wins, depth + 1)
    r7_p1_wins, r7_p2_wins = play(p1_position, p2_position, p1_score, p2_score, 9, True, False, p1_wins, p2_wins, depth + 1)
    p1_wins += r1_p1_wins + r2_p1_wins * 3 + r3_p1_wins * 6 + r4_p1_wins * 7 + r5_p1_wins * 6 + r6_p1_wins * 3 + r7_p1_wins
    p2_wins += r1_p2_wins + r2_p2_wins * 3 + r3_p2_wins * 6 + r4_p2_wins * 7 + r5_p2_wins * 6 + r6_p2_wins * 3 + r7_p2_wins
    print(f'p1_wins: {p1_wins}\np2_wins: {p2_wins}')


