class Fraction:
    def __init__(self, numerator, denominator):
        # properties
        self.num = numerator
        self.den = denominator

    # methods
    
    def divide(self, second_fraction):
        result_numerator = self.num * second_fraction.den
        result_denominator = self.den * second_fraction.num
        return Fraction(result_numerator, result_denominator)
    
    def plus(self, second_fraction):
        result_numerator = self.num * second_fraction.den + second_fraction.num * self.den
        result_denominator = self.den * second_fraction.den
        return Fraction(result_numerator, result_denominator)

    def times(self, second_fraction):
        result_numerator = self.num * second_fraction.num
        result_denominator = self.den * second_fraction.den
        return Fraction(result_numerator, result_denominator)

    def minus(self, second_fraction):
        result_numerator = self.num * second_fraction.den - second_fraction.num * self.den
        result_denominator = self.den * second_fraction.den
        return Fraction(result_numerator, result_denominator)


fraction1 = Fraction(3, 7)
fraction2 = Fraction(2, 5)

result_division = fraction1.divide(fraction2)
result_addition = fraction1.plus(fraction2)
result_multiplication = fraction1.times(fraction2)
result_subtraction = fraction1.minus(fraction2)

print("The result of division:", result_division.num / result_division.den)
print("Next result:", result_addition.num / result_addition.den)
print("multiplication:", result_multiplication.num / result_multiplication.den)
print("The result of subtraction:", result_subtraction.num / result_subtraction.den)