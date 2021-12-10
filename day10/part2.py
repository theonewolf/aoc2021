#!/usr/bin/env python3

if __name__ == '__main__':
    data = open('input').read().splitlines()

    mapping = {'(':')', '[':']', '{':'}', '<':'>'}
    points = {')':3, ']':57, '}':1197, '>':25137}
    incomplete_points = {')':1, ']':2, '}':3, '>':4}
    score = 0
    total_scores = []

    for line in data:
        stack = []
        for delimiter in line:
            if delimiter in mapping:
                stack.append(delimiter)
            elif delimiter in mapping.values():
                expected = mapping[stack.pop()]
                if delimiter != expected:
                    score += points[delimiter]
                    print(f'Expected "{expected}", but got "{delimiter}" instead.')
                    stack = [] # discard corrupted lines
                    break
            else:
                raise 'Corrupted?'

        # Incomplete string
        if len(stack) != 0:
            total_score = 0
            while(len(stack) != 0):
                total_score *= 5
                print(f'Multiply total score by 5 to get {total_score}, ',)
                expected = mapping[stack.pop()]
                total_score += incomplete_points[expected]
                print(f'then add the value of {expected} to get {total_score}')
            total_scores += [total_score]

    print(f'Total score: {score}')
    print(len(total_scores))
    print(len(total_scores) // 2)
    print(f'Middle completion score: {sorted(total_scores)[len(total_scores)//2]}')
