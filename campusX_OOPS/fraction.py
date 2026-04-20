class Fraction:
    def __init__(self,x,y):
        # print("Hello Bachha")
        self.num = x
        self.den = y
    def __str__(self):
        return f"{self.num}/{self.den}"
    def __add__(self,other):
        new_num = self.num*other.den + self.den*other.num
        new_den = self.den*other.den
        return '{}/{}'.format(new_num, new_den)
    def __sub__(self, other):
        new_num = self.num*other.den - other.num*self.den
        new_den = self.den*other.den
        return '{}/{}'.format(new_num, new_den)
    def __convert_to_decimal(self):
        return self.num/self.den
    def __mul__(self, other):
        new_num = self.num*other.num
        new_den = self.den*other.den
        return '{}/{}'.format(new_num, new_den)
    def __truediv__(self, other):
        new_num = self.num*other.den
        new_den = self.den*other.num
        return '{}/{}'.format(new_num, new_den)
frac1 = Fraction(1,2)
frac2 = Fraction(1,2)
print(frac1+frac2)
print(frac1-frac2)
print(frac1*frac2)
print(frac1/frac2)  
print(frac1._Fraction__convert_to_decimal())
# print(frac1.num)
# print(frac1.den)
# print(frac1)
# print(frac2)