#!/usr/bin/env python3

if __name__ == '__main__':
    data = open('input').read().splitlines()
    
    count = 0
    for displays in data:
        _, output_displays = displays.split('|')
        for display in output_displays.split():
            segments_on = len(display)

            if segments_on == 2 or segments_on == 4 or segments_on == 3 or segments_on == 7:
                count += 1

    print(f'{count}')
