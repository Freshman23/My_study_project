class Matrix:
    def __form_matrix_list(self, seq_iter_obj):
        """Принимает коллекцию итерируемых объектов и формирует список списков матричных элементов(строк элементов).
        Если количества элементов строк не равны, то дополняет нулями строки,
        меньшие чем строка с максимальным количеством элементов, для формирования столбцов."""
        max_len_row = max([len(row) for row in seq_iter_obj])
        for row in seq_iter_obj:
            row = list(row)
            if len(row) == max_len_row:
                self.matrix_list.append(row)
            else:
                for _ in range(max_len_row - len(row)):
                    row.append(0)
                self.matrix_list.append(row)

    def __form_matrix_view(self):
        """Формирует строку для отображения матрицы в проямоугольной форме."""
        width_col = [max([len(str(el)) for el in col]) for col in zip(*self.matrix_list)]
        for row in self.matrix_list:
            for i, col in enumerate(row):
                if 0 < i < (len(row) - 1):
                    self.matrix_view += f' {col:{width_col[i]}} '
                elif i == 0:
                    self.matrix_view += f'| {col:{width_col[i]}} '
                else:
                    self.matrix_view += f' {col:{width_col[i]}} |\n'

    def __init__(self, seq_iter_obj):
        self.matrix_list = []
        self.__form_matrix_list(seq_iter_obj)
        self.matrix_view = ''
        self.__form_matrix_view()

    def __str__(self):
        return self.matrix_view

    def __add__(self, other):
        """Принимает два объекта класса Matrix для суммирования и возвращает объект того же класса."""
        sum_matrix_list = []
        try:
            for ind_row, row in enumerate(self.matrix_list):
                new_row = []
                for ind_col, col in enumerate(row):
                    new_row.append(self.matrix_list[ind_row][ind_col] + other.matrix_list[ind_row][ind_col])
                sum_matrix_list.append(new_row)
        except IndexError as err:
            print('Error:', err)
            print('Matrices must have an equal number of rows and columns to be added.')
        except TypeError as err:
            print('Error:', err)
            print('Matrices must have a numeric entries.')
        except AttributeError as err:
            print('Error:', err)
            print('It must be a matrix to be added.')
        else:
            return Matrix(sum_matrix_list)


m = Matrix(((12, 2, 0.35), {4, 5.2}, (1000, 2, 3, -4.89), {5: 6, -7: 8}))
print(m.matrix_list)
print(m)
a = Matrix([(1, 2, 3, 4), (2, 3, 4), (5, 6, 7)])
b = Matrix([(1, 9, 3), (1, 3, 5), (2, 4, 10, 7)])
print(a, end='')
print('       +')
print(b, end='')
print('       =')
print(a + b)
