# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class Complex:
    def __init__(self,  real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def _imaginary(self):
        return ('-' if self.imaginary < 0 else '+') + str(abs(self.imaginary)) + 'i'

    def __add__(self, other):
        if type(other) != type(self):
            return 0
        return Complex(self.real+other.real, self.imaginary+other.imaginary)

    def __mul__(self, other):
        if type(other) != type(self):
            return 0
        return Complex(self.real*other.real + self.imaginary*other.imaginary*-1,
                       self.real*other.imaginary + self.imaginary*other.real)

    def __str__(self):
        return f'{self.real}{self._imaginary()}'


if __name__ == '__main__':
    a = Complex(1, -1)
    b = Complex(3, 6)
    print(a+b)
    print(a*b)
    print('--------------------------------')
    a = Complex(1, 3)
    b = Complex(4, -5)
    print(a + b)
    print(a * b)
