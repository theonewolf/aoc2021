#!/usr/bin/env python3

if __name__ == '__main__':
    data = open('input').read().splitlines()

    mapping = {'(':')', '[':']', '{':'}', '<':'>'}
    points = {')':3, ']':57, '}':1197, '>':25137}
    score = 0
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
            else:
                raise 'Corrupted?'
    print(f'Total score: {score}')
