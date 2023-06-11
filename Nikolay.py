class TriangleChecker:

   def __init__(self, a, b, c):
       self.a = a
       self.b = b
       self.c = c

   def is_triangle(self):

    a = self.a
    b = self.b 
    c = self.c  

    if (not isinstance(a, int)) or (not isinstance(b, int)) or (not isinstance(c, int)):
        return "Нужно вводить только числа!"
    elif a < 0 or b < 0 or c < 0:
        return "С отрицательными числами ничего не выйдет!"
    elif a + b > c and a + c > b and b + c > a:
        return "Ура, можно построить треугольник!"
    else:
        return "Жаль, но из этого треугольник не сделать"
tc = TriangleChecker(-1, 1, 5)
print(tc.is_triangle())
