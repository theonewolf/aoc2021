#!/usr/bin/env python3

def oxygen_bit_criteria(position: int, data):
    counts = [0,0]
    
    for line in data:
        counts[int(line[position])] += 1

    if counts[0] > counts[1]:
        return [item for item in data if item[position] == '0']
    elif counts[1] > counts[0]:
        return [item for item in data if item[position] == '1']
    else:
        return [item for item in data if item[position] == '1']
        
def co2_bit_criteria(position: int, data):
    counts = [0,0]
    
    for line in data:
        counts[int(line[position])] += 1

    if counts[0] > counts[1]:
        return [item for item in data if item[position] == '1']
    elif counts[1] > counts[0]:
        return [item for item in data if item[position] == '0']
    else:
        return [item for item in data if item[position] == '0']
 

if __name__ == '__main__':
    data = open('input').read().splitlines()

    # Oxygen
    position = 0
    oxygen_list = oxygen_bit_criteria(position, data)
    
    while len(oxygen_list) > 1:
        position += 1
        oxygen_list = oxygen_bit_criteria(position, oxygen_list)

    # CO2
    position = 0
    co2_list = co2_bit_criteria(position, data)

    while len(co2_list) > 1:
        position += 1
        co2_list = co2_bit_criteria(position, co2_list)

    print(oxygen_list)
    print(co2_list)

    oxygen_rating = int(oxygen_list[0], 2)
    co2_rating = int(co2_list[0], 2)
    print(f'{oxygen_rating} * {co2_rating} == {oxygen_rating * co2_rating}')
