class LZ77:
    def __init__(self, window_size=256, lookahead_size=64):
        self.window_size = window_size
        self.lookahead_size = lookahead_size

    def compress(self, data):
        compressed_data = []
        i = 0
        while i < len(data):
            # Find the longest match within the window
            match_length = 0
            match_offset = 0
            for j in range(max(0, i - self.window_size), i):
                length = 0
                while i + length < len(data) and data[j + length] == data[i + length] and length < self.lookahead_size:
                    length += 1
                if length > match_length:
                    match_length = length
                    match_offset = i - j

            # Add the match to the compressed data
            if match_length > 0:
                try:
                    compressed_data.append((match_offset, match_length, data[i + match_length]))
                except IndexError:
                    compressed_data.append((match_offset, match_length, ''))
                i += match_length + 1
            else:
                compressed_data.append((0, 0, data[i]))
                i += 1

        return compressed_data

    def decompress(self, compressed_data):
        decompressed_data = []
        for match in compressed_data:
            offset, length, char = match
            if length > 0:
                for i in range(length):
                    decompressed_data.append(decompressed_data[-offset])
            decompressed_data.append(char)

        return ''.join(decompressed_data)

lz77 = LZ77()
st = "abracadabradabra"
compressed_data = lz77.compress(st)
print(compressed_data)

# [(0, 0, 'a'), (0, 0, 'b'), (1, 1, 'r'), (2, 3, 'c'), (4, 3, 'd'), (7, 1, 'b'), (4, 2, 'r'), (2, 2, 'a')]

original_data = lz77.decompress(compressed_data)
print(original_data)
print(st)
assert (original_data == st)
# abracadabradabra