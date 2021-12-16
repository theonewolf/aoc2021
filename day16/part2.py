#!/usr/bin/env python3

from math import prod

class Packet():
    def __init__(self, bytestream):
        self.bytestream = bytestream
        self.parse_header()
        self.literal = None

        self.sub_packets = []

        # literal type
        if self.packet_type == 4:
            self.parse_literal()
        # operator type
        else:
            self.length_type = int(self.bytestream[0], 2)
            self.bytestream = self.bytestream[1:]
            if self.length_type == 0:
                self.sub_packet_bits = int(self.bytestream[0:15], 2)
                self.bytestream = self.bytestream[15:]
                while self.sub_packet_bits > 0:
                    self.sub_packets += [Packet(self.bytestream)]
                    self.sub_packet_bits -= len(self.bytestream) - len(self.sub_packets[-1].bytestream)
                    self.bytestream = self.sub_packets[-1].bytestream
            elif self.length_type == 1:
                num_packets = int(self.bytestream[0:11], 2)
                self.bytestream = self.bytestream[11:]
                for _ in range(num_packets):
                    self.sub_packets += [Packet(self.bytestream)]
                    self.bytestream = self.sub_packets[-1].bytestream

    def parse_header(self):
        self.version = int(self.bytestream[0:3], 2)
        self.bytestream = self.bytestream[3:]
        self.packet_type = int(self.bytestream[0:3], 2)
        self.bytestream = self.bytestream[3:]

    def parse_literal(self):
        continue_group = self.bytestream[0] == '1'
        self.bytestream = self.bytestream[1:]
        literal = ''
        while continue_group:
            literal += self.bytestream[0:4]
            self.bytestream = self.bytestream[4:]
            continue_group = self.bytestream[0] == '1'
            self.bytestream = self.bytestream[1:]
        literal += self.bytestream[0:4]
        self.bytestream = self.bytestream[4:]
        self.literal = int(literal, 2)

    def __str__(self):
        return f'Packet\n\t.version = {self.version},\n\t.packet_type = {self.packet_type},\n\t.literal = {self.literal},\n\t.sub_packets = {self.sub_packets}\n\t.bytestream = { self.bytestream }'

def sum_versions(packet):
    total = packet.version

    for packet in packet.sub_packets:
        total += sum_versions(packet)

    return total

def compute(packet):
    if packet.packet_type == 0:
        return sum([compute(sub_packet) for sub_packet in packet.sub_packets])
    elif packet.packet_type == 1:
        return prod([compute(sub_packet) for sub_packet in packet.sub_packets])
    elif packet.packet_type == 2:
        return min([compute(sub_packet) for sub_packet in packet.sub_packets])
    elif packet.packet_type == 3:
        return max([compute(sub_packet) for sub_packet in packet.sub_packets])
    elif packet.packet_type == 4:
        return packet.literal
    elif packet.packet_type == 5:
        return 1 if compute(packet.sub_packets[0]) > compute(packet.sub_packets[1]) else 0
    elif packet.packet_type == 6:
        return 1 if compute(packet.sub_packets[0]) < compute(packet.sub_packets[1]) else 0
    elif packet.packet_type == 7:
        return 1 if compute(packet.sub_packets[0]) == compute(packet.sub_packets[1]) else 0
    else:
        print(f'Packet type: {packet.packet_type}')
        raise 'ERROR: unknown packet type!'

if __name__ == '__main__':
    data = open('input').read().splitlines()

    packets = []

    for line in data:
        print(f'Processing: {line}')
        binarystr = bin(int(line, 16))[2:]
        binarystr = binarystr.zfill(len(line) * 4)
        packets += [Packet(binarystr)]
        print(f'Computed value: {compute(packets[-1])}')

