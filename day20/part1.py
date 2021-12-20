#!/usr/bin/env python3

from collections import Counter
from pprint import pprint

# expand by 2 in all directions; simulate infinite grid
def expand_image(image,factor,filler):
    assert factor % 2 == 0
    final_len = len(image[0]) + factor
    new_image = [[filler for _ in range(final_len)]]
    new_image += [[filler for _ in range(final_len)]]

    for row in image:
        new_image += [[filler for _ in range(factor // 2)] + row + [filler for _ in range(factor // 2)]]

    new_image += [[filler for _ in range(final_len)]]
    new_image += [[filler for _ in range(final_len)]]

    return new_image

# drop 1 in all dimensions
def crop(image):
    image = image[1:-1]
    new_image = []
    for row in image:
        new_image += [row[1:-1]]
    return new_image

def enhance(image, enhancement_lut):
    if step % 2 == 0:
        image = expand_image(image, 4, filler='.')
    else:
        image = expand_image(image, 4, filler=enhancement_lut[0])
    new_image = [['.' for _ in row] for row in image]

    # we can just do 3x3 grids around the image because we expanded it
    for i in range(0, len(image) - 2):
        for j in range(0, len(image[0]) - 2):
            lut_bits_str = image[i][j] + image[i][j + 1] + image[i][j + 2]
            lut_bits_str += image[i + 1][j] + image[i + 1][j + 1] + image[i + 1][j + 2]
            lut_bits_str += image[i + 2][j] + image[i + 2][j + 1] + image[i + 2][j + 2]
            lut_bits = lut_bits_str.replace('.','0').replace('#','1')
            lut_int = int(lut_bits, 2)
            new_image[i + 1][j + 1] = enhancement_lut[lut_int]

    new_image = crop(new_image)
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

    print(image_str(image))
    pprint(count_lit(image))
    print(enhancement_lut[511])
