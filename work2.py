# Напишите программу, которая принимает две строки вида “a/b” - дробь
# с числителем и знаменателем. Программа должна возвращать сумму
# и произведение* дробей. Для проверки своего кода используйте модуль fractions
from fractions import Fraction

a = input(str("Enter a fraction in the form a/b: \n"))
b = input(str("Again enter a fraction in the form a/b: \n"))
arr_a = a.split('/')
arr_b = b.split('/')

a1 = int(arr_a[0])
a2 = int(arr_a[1])
b1 = int(arr_b[0])
b2 = int(arr_b[1])

Fraction_a = Fraction(a1,a2)
Fraction_b = Fraction(b1,b2)
Сhecksum = Fraction_b + Fraction_a
Checkproduct = Fraction_b * Fraction_a


sum: float = (a1 * b2 + b1 * a2) / (a2 * b2)
multiplication: float = (a1 * b1) / (a2 * b2)

print("Sum = " , sum , "  ", (a1 * b2 + b1 * a2), "/" , (a2 * b2))
print( "Multiplication = ", multiplication, "   ",(a1 * b1) , "/" , (a2 * b2))

print ( "Сhecksum = ", Сhecksum)
print ( "Checkproduct = " , Checkproduct)