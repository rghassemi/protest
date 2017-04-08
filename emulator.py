from numpy import zeros
import numpy
from PIL import BdfFontFile
from rgbmatrix import graphics, RGBMatrixOptions, RGBMatrix
fp = open('6x10.bdf','rb')
b = BdfFontFile.BdfFontFile(fp)
fp.close()

def get_ascii_pixels(character, rotate=None):
    ascii_value = ord(character)

    im = b.glyph[ascii_value][3]
    pixels = list(im.getdata())
    width, height = im.size
    temp =  [pixels[i * width:(i + 1) * width] for i in range(height)]
    if rotate:
        #temp = numpy.flip(temp, 1)
        #temp = numpy.flipud(temp)
        #temp = numpy.flip(temp, 1)
        #temp = list(zip(*temp[::-1]))
        #temp = list(zip(*temp[::-1]))
        #temp = list(zip(*temp[::-1]))
        pass
    return temp
def print_letter(letter):
    for row in letter:
        temp = ''
        for char in row:
            temp += '*' if char else ' '
        print(temp)

a = [[1, 1, 1, 1],
     [1, '', '', ''],
     [1, '', '', ''],
     [1, '', '', ''],
     [1, '', '', '']]


class LineCursor(object):
    def __init__(self, canvas, line_number, get_letter=get_ascii_pixels, rotated=False):
        self.canvas = canvas
        self.rotated = rotated
        self.line_number = line_number
        self.get_letter = get_letter

        if self.rotated:
            self.start_column = 127
            self.increment = -1
        else:
            self.start_column = 0
            self.increment = 1
        self.current_column = self.start_column
        self.current_row = self.line_number

    def reset(self):
        self.current_row = self.start_row
        self.current_column = self.start_column

    def draw_line(self, text):
        for letter in text:
            self.draw_letter(letter)

    def draw_letter(self, letter):
        pixels = self.get_letter(letter)
        row_length = len(pixels)
        column_length = len(pixels[0])
        start_column = self.current_column

        for row in range(row_length):
            for column in range(column_length):
                if pixels[row][column]:
                    self.canvas.SetPixel(self.current_column, self.current_row, 0, 255, 0)
                self.current_column += self.increment
            self.current_column = start_column
            self.current_row += self.increment

        self.current_column += column_length * self.increment
        self.current_row = self.line_number

class Matrix(object):
    def __init__(self, columns=128, rows=32, panels=2):
        self.max_columns = columns
        self.max_rows = rows
        self.panels = 1
        self.clear()
        self.forward_lines = []
        self.reverse_lines = []
        self.hardware = Cocktapus()
        self.canvas = self.hardware.canvas
        self.forward_lines.append(LineCursor(self.canvas, 0))
        self.forward_lines.append(LineCursor(self.canvas, 10))
        self.forward_lines.append(LineCursor(self.canvas, 20))

        self.reverse_lines.append(LineCursor(self.canvas, 31, rotated=True))
        self.reverse_lines.append(LineCursor(self.canvas, 21, rotated=True))
        self.reverse_lines.append(LineCursor(self.canvas, 11, rotated=True))

    def draw_the_line(self, line_number, text):
        self.forward_lines[line_number].draw_line(text)
        self.reverse_lines[line_number].draw_line(text)
        #self.hardware.matrix.SwapOnVSync(self.canvas)

    def show(self):
        #rotated = numpy.rot90(self.pixels[1], 2)
        for row in range(self.max_rows):
            temp = ''
            for column in range(self.max_columns):
                if self.pixels[0][column][row] == 1:
                    temp += '*'
                else:
                    temp += ' '
            #for column in range(self.max_columns):
            #    if rotated[column][row] == 1:
            #        temp += '*'
            #    else:
            #        temp += ' '
            print(temp)


    def clear(self):
        self.pixels = []
        for i in range(self.panels):
            self.pixels.append([])
            self.pixels[i] = zeros((self.max_columns, self.max_rows))

    def draw_letter_rotated(self, column, row, letter):
        letter = get_ascii_pixels(letter, True)
        print_letter(letter)
        #for rows in letter:
        #    print(rows)

        column_length = len(letter[0])
        row_length = len(letter)
        start_column = column
        start_row = row

        for i in range(column_length):
            start_column = column
            for j in range(row_length):
                value = letter[j][i]
                #print(j, i)
                if value:
                    self.set_pixel(start_column, start_row, 1)
                start_column -= 1
            start_row -= 1

        return (start_row, start_column-1)

    def draw_letter(self, column, row, letter):
        letter = get_ascii_pixels(letter)
        column_length = len(letter[0])
        row_length = len(letter)

        for i in range(column_length):
            for j in range(row_length):
                value = letter[j][i]
                if value:
                    self.set_pixel(column+i, row+j, 1)
        return (column+i, column+j-2)

    def draw_line(self, start_row, start_column, text):
        row = start_row
        column = start_column
        for char in text:
            (foo, column) = self.draw_letter(column, row, char)

    def draw_line_rotated(self, start_row, start_column, text):
        row = start_row
        column = start_column
        for char in text:
            (foo, column) = self.draw_letter_rotated(column, row, char)

    def test(self):
        print(self.draw_letter_rotated(127,31, 'A'))
        #self.draw_line(0, 0, 'Life')
        #self.draw_line(10,0, 'Before')
        #self.draw_line(20,0, 'Party')
        #self.draw_line_rotated(31, 127, 'Life')
        #self.draw_line_rotated(21, 127, 'Before')
        #self.draw_line_rotated(11, 127, 'Party')
        self.show()
        #self.draw_line(0,0, 'Life')
        #self.draw_line(10, 0, 'Before')
        #self.draw_line(20, 0, 'Party')

    def set_pixel(self, column, row, value):
        #print(column, row)
        for panel in self.pixels:
            panel[column][row] = value
        #self.pixels[column][row] = value


def test():
    m = Matrix()
    m.draw_the_line(0, "Life")
    m.draw_the_line(1, "Before")
    m.draw_the_line(2, "Party")
    
    m.hardware.matrix.SwapOnVSync(m.canvas)
    while True:
        pass
    #m.forward_lines[0].draw_line('Life')
    #m.forward_lines[1].draw_line('Before')
    #m.forward_lines[2].draw_line('Party')
    #m.reverse_lines[0].draw_line('Life')
    #m.reverse_lines[1].draw_line('Before')
    #m.reverse_lines[2].draw_line('Party')
    #m.show()
    return m

class Cocktapus(object):
    def __init__(self):
        self.options = RGBMatrixOptions()
        self.options.hardware_mapping = 'adafruit-hat'
        self.options.rows = 32
        self.options.parallel = 1
        self.options.chain_length = 4
        self.options.pwm_bits = 11
        self.options.brightness = 100
        self.options.pwm_lsb_nanoseconds = 130
        self.matrix = RGBMatrix(options = self.options)
        self.canvas = self.matrix.CreateFrameCanvas()
        self.default_color = graphics.Color(255,0,0)
        #self.emulator = Matrix()
        #self.emulator.test()

    def test(self):

        for row in xrange(len(self.emulator.pixels[0])):
            for column in xrange(len(self.emulator.pixels[0][0])):
                if self.emulator.pixels[0][column][row]:
                    self.matrix.set_pixel(column, row, self.default_color)
        self.matrix.SwapOnVSync(self.canvas)
        while True:
            pass
        #self.font = graphics.Font()
        #self.font.LoadFont('6x10.bdf')

if __name__ == "__main__":
    test()
