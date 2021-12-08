#!/usr/bin/env python3
#
# 1:     c     f
# 4:   b c d   f
# 7: a   c     f
# 8: a b c d e f g
# 
# 2: a   c d e   g | 5 --> 2 by process of elimination
# 3: a   c d   f g | 5 --> only 5 with 1 contained inside it
# 5: a b   d   f g | 5 --> contained inside 6
# 
# 0: a b c   e f g | 6 --> only 6 with 1 contained inside it, but not 4
# 6: a b   d e f g | 6 --> 6 by process of elimination
# 9: a b c d   f g | 6 --> only 6 with 4 contained inside it

if __name__ == '__main__':
    data = open('input').read().splitlines()
    
    count = 0
    output_values = []
    for displays in data:
        inputs, outputs = displays.split('|')
        fives = []
        sixes = []
        mapping = {}
        for display in inputs.split():
            segments_on = len(display)

            if segments_on == 2:
                mapping['1'] = frozenset(display)
            elif segments_on == 4:
                mapping['4'] = frozenset(display)
            elif segments_on == 3:
                mapping['7'] = frozenset(display)
            elif segments_on == 7:
                mapping['8'] = frozenset(display)
            elif segments_on == 5:
                fives += [frozenset(display)]
            elif segments_on == 6:
                sixes += [frozenset(display)]
            else:
                raise f'Failure!  Unexpected size of input: len({display}) == {segments_on}'

        for sixer in sixes:
            if sixer.issuperset(mapping['1']) and not sixer.issuperset(mapping['4']):
                mapping['0'] = sixer
            elif sixer.issuperset(mapping['4']):
                mapping['9'] = sixer
            else:
                mapping['6'] = sixer

        for fiver in fives:
            if fiver.issuperset(mapping['1']):
                mapping['3'] = fiver
            elif fiver.issubset(mapping['6']):
                mapping['5'] = fiver
            else:
                mapping['2'] = fiver

        inverse_mapping = {v:k for k,v in mapping.items()}
        output_values += [int(''.join([ inverse_mapping[frozenset(output)] for output in outputs.split()]))]


    print(output_values)
    print(sum(output_values))
