#!/usr/bin/env python3

from collections import Counter
from pprint import pprint

# expand by 2 in all directions; simulate infinite grid
def expand_image(image):
    final_len = len(image[0]) + 4
    new_image = [['.' for _ in range(final_len)]]
    new_image += [['.' for _ in range(final_len)]]

    for row in image:
        new_image += [['.', '.'] + row + ['.', '.']]

    new_image += [['.' for _ in range(final_len)]]
    new_image += [['.' for _ in range(final_len)]]

    return new_image

def enhance(image, enhancement_lut):
    image = expand_image(image)
    new_image = [['.' for _ in row] for row in image]

    # we can just do 3x3 grids around the image because we expanded it
    for i in range(len(image) - 2):
        for j in range(len(image[0]) - 2):
            lut_bits_str = image[i][j] + image[i][j + 1] + image[i][j + 2]
            lut_bits_str += image[i + 1][j] + image[i + 1][j + 1] + image[i + 1][j + 2]
            lut_bits_str += image[i + 2][j] + image[i + 2][j + 1] + image[i + 2][j + 2]
            lut_bits = lut_bits_str.replace('.','0').replace('#','1')
            lut_int = int(lut_bits, 2)
            new_image[i + 1][j + 1] = enhancement_lut[lut_int]

    return new_image

def count_lit(image):
    c = Counter()

    for row in image:
        c.update(row)

    return c['#']

def image_str(image):
    imstr = ''
    for row in image:
        imstr += ''.join(row)
        imstr += '\n'
    return imstr

if __name__ == '__main__':
    data = open('input').read().splitlines()

    enhancement_lut = data[0]
    pprint(enhancement_lut)

    image = []
    for line in data[2:]:
        image += [[c for c in line]]

    pprint(image)
    for step in range(2):
        image = enhance(image, enhancement_lut)
        pprint(image)
    pprint(count_lit(image))

    print(image_str(image))
