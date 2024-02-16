"""LZW_algorithm"""

class LZWAlgorithm:
    """LZW Algorithm"""
    def __init__(self, file_path=''):
        """
        Constructor
        Initializes the LZWAlgorithm class.
        param file_path: Path to the file(optional parameter)
        """
        self.file_path = file_path

    def encode(self, text):
        """
        Encodes text using the LZW algorithm.
        param text: Text to encode
        return: Encoded message and encoding dictionary
        """
        dictionary,encoded_message, next_code= {}, [], 0
        unique_symbols = set([*text])
        for symbol in unique_symbols:
            dictionary[symbol] = next_code
            next_code += 1

        current_sequence = ''
        for symbol in text:
            current_sequence += symbol
            if current_sequence not in dictionary:
                dictionary[current_sequence] = next_code
                encoded_message.append(dictionary[current_sequence[:-1]])
                current_sequence = symbol
                next_code += 1

        encoded_message.append(dictionary[current_sequence])
        solut = (encoded_message, dictionary)

        return solut

    def decode(self, encoded_message, dictionary):
        """
        Decodes an encoded message using an encoding dictionary.
        param encoded_message: Encoded message
        param dictionary: Encoding dictionary
        return: Decoded message
        """
        dictionary_keys = list(dictionary.keys())
        decoded_message = ''

        for code in encoded_message:
            decoded_message += dictionary_keys[code]
        return decoded_message
