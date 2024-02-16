"""Lab8.3_Grayscale_Image_ADT"""
from PIL import Image, ImageOps
from arrays import Array2D
from LZW_algorithm import LZWAlgorithm as lzw

class Grayscale_Image_ADT:
    """"""
    def __init__(self, nrows, ncols):
        """
        Initializes the Grayscale_Image_ADT class.

        param nrows: The number of rows in the image.
        param ncols: The number of columns in the image.
        """
        self._nrows = nrows
        self._ncols = ncols
        self.image = Array2D(nrows, ncols)

    def width(self):
        """
        Returns the width (number of columns) of the image.
        """
        return self._ncols

    def height(self):
        """
        Returns the height (number of rows) of the image.
        """
        return self._nrows

    def clear(self, value):
        """
        Sets all pixels in the image to the specified grayscale value.

        param value: The grayscale value to set (0-255).
        """
        if 0 <= value <= 255:
            for row in range(self.height()):
                for col in range(self.width()):
                    self.image[row, col] = value

    def getitem(self, row, col):
        """
        Retrieves the grayscale value of a pixel at the specified row and column.

        param row: The row index.
        param col: The column index.
        return: The grayscale value of the pixel.
        """
        if 0 <= row < self.height() and 0 <= col < self.width():
            return self.image[row, col]

    def setitem(self, row, col, value):
        """
        Sets the grayscale value of a pixel at the specified row and column.

        param row: The row index.
        param col: The column index.
        param value: The grayscale value to set (0-255).
        """
        if 0 <= row < self.height() and 0 <= col < self.width() and 0 <= value <= 255:
            self.image[row, col] = value
    @staticmethod
    def from_file(path):
        """
        Loads a grayscale image from a file.

        param path: The path to the image file.
        return: The grayscale image.
        """
        image = Image.open(path)
        image_grayscale = ImageOps.grayscale(image)
        pixels = image_grayscale.load()
        nrows, ncols = image_grayscale.size
        grayscale_image = Grayscale_Image_ADT(nrows, ncols)
        for row in range(nrows):
            for col in range(ncols):
                grayscale_image.setitem(row, col, pixels[row, col])
        return grayscale_image
    @staticmethod
    def lzw_compression(image):
        """
        Performs LZW compression on the grayscale image.

        param image: The grayscale image to compress.
        return: The compressed LZW data.
        """
        res = ''
        for row in range(image.height()):
            res += str([image.getitem(row, col) for col in range(image.width())]) + '\n'
        return lzw().encode(res)
    @staticmethod
    def lzw_decompression(lst, dictionary):
        """
        Performs LZW decompression on the encoded LZW data.

        param lst: The encoded LZW data.
        param dictionary: The LZW dictionary.
        return: The decompressed grayscale image.
        """
        res = lzw().decode(lst, dictionary)
        res = res[:-1].split('\n')
        image = Grayscale_Image_ADT(len(res), len(res[0][1:-1].split(', ')))
        for row in range(image.height()):
            for col in range(image.width()):
                try:
                    image.setitem(row, col, int(res[row][1:-1].split(', ')[col]))
                except ValueError:
                    image.setitem(row, col, 255)
        return image

def converting_image_in_arrays(image):
    """
    Converts image to a 2d_array (list of lists)
    """
    res = []
    for row in range(image.height()):
        res.append([image.getitem(row, col) for col in range(image.width())])
    return res

if __name__ == '__main__':
    image = Grayscale_Image_ADT.from_file('image.png')
    compressed_image = Grayscale_Image_ADT.lzw_compression(image)
    decompressed_image = Grayscale_Image_ADT.lzw_decompression(*compressed_image)
    # Test Grayscale_Image_ADT:
    print(f"Number of pixels in original image:\t{image.width()*image.height()}")
    print(f"Number of pixels in encoded image:\t\
{len(compressed_image[0])+len(compressed_image[1])}")
    print(f"Image compression:\t\t\t\
{100-round((len(compressed_image[0])+len(compressed_image[1]))/(image.width()*image.height())*100, 2)}%")
    # check the image remained unchanged after encoding and decoding
    assert(converting_image_in_arrays(image) == converting_image_in_arrays(decompressed_image))
