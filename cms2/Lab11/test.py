class LZSS:
    def __init__(self, window_size, lookahead_buffer_size):
        self.window_size = window_size
        self.lookahead_buffer_size = lookahead_buffer_size

    def compress(self, data):
        compressed_data = []
        i = 0
        while i < len(data):
            match_length, match_offset = self.find_longest_match(data, i)
            if match_length > 2:
                compressed_data.append((match_length, match_offset))
                i += match_length
            else:
                compressed_data.append((0, data[i]))
                i += 1
        return compressed_data

    def find_longest_match(self, data, current_index):
        end_index = min(current_index + self.lookahead_buffer_size, len(data))
        best_length = 0
        best_offset = 0

        for offset in range(1, self.window_size + 1):
            start_index = max(0, current_index - self.window_size)
            substring = data[current_index:current_index + offset]

            for j in range(start_index, current_index):
                match_length = 0
                while (
                    current_index + match_length < end_index and
                    data[j + match_length] == data[current_index + match_length]
                ):
                    match_length += 1

                if match_length > best_length:
                    best_length = match_length
                    best_offset = current_index - j

        return best_length, best_offset

    def decompress(self, compressed_data):
        decompressed_data = []
        for token in compressed_data:
            length, offset = token
            if length > 0:
                start_index = len(decompressed_data) - offset
                for i in range(length):
                    decompressed_data.append(decompressed_data[start_index + i])
            else:
                decompressed_data.append(offset)
        return decompressed_data


# Приклад використання
lzss = LZSS(window_size=10, lookahead_buffer_size=5)
data = "ABRACADABRA"
compressed_data = lzss.compress(data)
print("Compressed data:", compressed_data)

decompressed_data = lzss.decompress(compressed_data)
print("Decompressed data:", "".join(map(str, decompressed_data)))

# class Lz78:
#     '''Lz78 class'''
#     def compress(self, uncompressed):
#         """Compress a string to a list of output symbols."""

#         # Build the dictionary.
#         dict_size = 256
#         dictionary = dict((chr(i), chr(i)) for i in range(dict_size))
#         # in Python 3: dictionary = {chr(i): chr(i) for i in range(dict_size)}

#         current_prefix = ""
#         result = []
#         for current_symbol in uncompressed:
#             current_phrase = current_prefix + current_symbol
#             if current_phrase in dictionary:
#                 current_prefix = current_phrase
#             else:
#                 result.append(dictionary[current_prefix])
#                 # Add current_phrase to the dictionary.
#                 dictionary[current_phrase] = dict_size
#                 dict_size += 1
#                 current_prefix = current_symbol

#         # Output the code for current_prefix.
#         if current_prefix:
#             result.append(dictionary[current_prefix])
#         return result


#     def decompress(self, compressed):
#         """Decompress a list of output symbols to a string."""

#         # Build the dictionary.
#         dict_size = 256
#         dictionary = dict((chr(i), chr(i)) for i in range(dict_size))
#         # in Python 3: dictionary = {chr(i): chr(i) for i in range(dict_size)}

#         # use StringIO, otherwise this becomes O(N^2)
#         # due to string concatenation in a loop
#         result = str()
#         current_prefix = compressed.pop(0)
#         result += current_prefix
#         for current_symbol in compressed:
#             if current_symbol in dictionary:
#                 current_entry = dictionary[current_symbol]
#             elif current_symbol == dict_size:
#                 current_entry = current_prefix + current_prefix[0]
#             else:
#                 raise ValueError('Bad compressed symbol: %s' % current_symbol)
#             result += current_entry

#             # Add current_prefix + current_entry[0] to the dictionary.
#             dictionary[dict_size] = current_prefix + current_entry[0]
#             dict_size += 1

#             current_prefix = current_entry
#         return result



# # How to use:
# lz78 = Lz78()
# compressed = lz78.compress('TOBEORNOTTOBEORTOBEORNOT')
# print(compressed)
# decompressed = lz78.decompress(compressed)
# print(decompressed)
# print('TOBEORNOTTOBEORTOBEORNOT')