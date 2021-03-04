class ComplexNumber:
    def __init__(self, real_part, img_part):
        self.r_p = real_part
        self.i_p = img_part

    def __str__(self):
        if self.r_p != 0 and self.i_p > 0:
            return f'{self.r_p}+{self.i_p}i'
        elif self.r_p != 0 and self.i_p < 0:
            return f'{self.r_p}{self.i_p}i'
        elif self.r_p != 0 and self.i_p == 0:
            return f'{self.r_p}'
        else:
            return f'{self.i_p}i'

    def __add__(self, other):
        return ComplexNumber(self.r_p + other.r_p, self.i_p + other.i_p)

    def __mul__(self, other):
        return ComplexNumber(self.r_p * other.r_p - self.i_p * other.i_p,
                             self.r_p * other.i_p + self.i_p * other.r_p)

    def __sub__(self, other):
        return ComplexNumber(self.r_p - other.r_p, self.i_p - other.i_p)

    def __truediv__(self, other):
        div_r_p = round((self.r_p * other.r_p + self.i_p * other.i_p) /
                        (other.r_p ** 2 + other.i_p ** 2), 7)
        div_i_p = round((self.i_p * other.r_p - self.r_p * other.i_p) /
                        (other.r_p ** 2 + other.i_p ** 2), 7)
        return ComplexNumber(div_r_p, div_i_p)


a = ComplexNumber(1, -9)
b = ComplexNumber(-3, 4)
print(f'a = {a} , b = {b}')
print(f'a + b = {a + b}')
print(f'a - b = {a - b}')
print(f'a * b = {a * b}')
print(f'a / b = {a / b}')
