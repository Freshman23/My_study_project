def cell_oper_dec(cell_met):
    def wrapper(self, other):
        try:
            return_value = cell_met(self, other)
        except AttributeError as err:
            print('Error:', err)
            print('It must be Cell object to perform an operation.')
        else:
            return return_value
    return wrapper


class Cell:
    def __init__(self, number):
        try:
            if (type(number) is int) and (number > 0):
                self.cells_number = number
            else:
                raise TypeError("not positive 'int'")
        except TypeError as err:
            print('Error:', err)
            print('It must be a positive integer to initialize cells.')
            self.cells_number = 0

    def __str__(self):
        return str(self.cells_number)

    @cell_oper_dec
    def __add__(self, other):
        return Cell(self.cells_number + other.cells_number)

    @cell_oper_dec
    def __sub__(self, other):
        if self.cells_number > other.cells_number:
            return Cell(self.cells_number - other.cells_number)
        else:
            print('The first cell must be greater than the second one to subtract.')

    @cell_oper_dec
    def __mul__(self, other):
        return Cell(self.cells_number * other.cells_number)

    @cell_oper_dec
    def __truediv__(self, other):
        if self.cells_number > other.cells_number:
            return Cell(round(self.cells_number / other.cells_number))
        else:
            print('The first cell must be greater than the second one to divide.')
            return

    def make_order(self, row_num):
        cells_str = ((row_num * '*') + '\n') * (self.cells_number // row_num)
        if (self.cells_number % row_num) != 0:
            cells_str += '*' * (self.cells_number % row_num)
        else:
            cells_str = cells_str[:-1]
        return cells_str


cell_1 = Cell(86)
cell_2 = Cell(5)
res_cell = cell_1 / cell_2
print('The result cell of two cell division is:\n', res_cell.make_order(5), sep='')
