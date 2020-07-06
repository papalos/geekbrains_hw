# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.


class NotCorrectMatrix(Exception):
    msg = 'it is not a correct matrix'


class MatrixIsNotEqual(Exception):
    msg = 'The matrices is not equal'


class MatrixX:
    # если было бы можно, этот метод лучше сделать статическим, т.к. ему ненужна self по идее не нужна
    def _check_matrix(self, matrix):
        if isinstance(matrix, list):
            for i in matrix:
                if isinstance(i, list):
                    if len(i) == len(matrix[0]):
                        for j in i:
                            if isinstance(j, (int, float)):
                                ...
                            else:
                                return False
                    else:
                        return False
                else:
                    return False
        else:
            return False
        return True

    def __init__(self, matrix):
        if not self._check_matrix(matrix):
            raise NotCorrectMatrix
        self._dimension = len(matrix), len(matrix[0])
        self._matrix = matrix

    # Это же не будет неправильным решением, если я воспользуюсь методом __str__ списка и уберу из него лишние символы?
    def __str__(self):
        mx_str = self._matrix.__str__().replace('], [', '\n')
        mx_str = mx_str.replace('[', '')
        mx_str = mx_str.replace(']', '')
        mx_str = mx_str.replace(',', '')
        return mx_str

    def __add__(self, other):
        if type(other) != type(self) or other._dimension != self._dimension:
            raise MatrixIsNotEqual
        new_mx = []
        for i in range(self._dimension[0]):
            new_mx.append([])
            for j in range(self._dimension[1]):
                new_mx[i].insert(j, self._matrix[i][j] + other._matrix[i][j])
        return MatrixX(new_mx)


if __name__ == '__main__':
    a = MatrixX([[1, 1, 1], [2, 2, 2]])
    b = MatrixX([[3, 3, 3], [4, 4, 4]])
    print(a._dimension)
    print('')
    print(a)
    print('')
    print(b)
    print('')
    print(a+b)
