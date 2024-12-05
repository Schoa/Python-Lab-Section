class Fraction:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator # Initialize Numerator
        self.__denominator = denominator # Iniatialize Denominator

    def display(self):
        """Prints the fraction in the form of numerator/denominator"""
        print(f"{self.__numerator}/{self.__denominator}")

    def add(self, other):
        new_numerator = self.__numerator * other.__denominator + self.__denominator * other.__numerator
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator, new_denominator)

    def multiply(self, other):
        """Multiplies this Fraction object with another and returns a new Fraction."""
        new_numerator = self.__numerator * other.__numerator
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator, new_denominator)

    def gcd(self, a, b):
        """Returns the greatest common divisor of a and b."""
        while b:
            a, b = b, a % b
        return a

    def simplify(self):
        """Simplifies the fraction."""
        common_divisor = self.gcd(self.__numerator, self.__denominator)
        self.__numerator //= common_divisor
        self.__denominator //= common_divisor


# Read input for two fractions
numerator1, denominator1 = map(int, input("").split())
numerator2, denominator2 = map(int, input("").split())

# Create two Fraction instances
frac1 = Fraction(numerator1, denominator1)
frac2 = Fraction(numerator2, denominator2)

# Calculate sum and product of fractions
sum_frac = frac1.add(frac2)
product_frac = frac1.multiply(frac2)

# Simplify results
sum_frac.simplify()
product_frac.simplify()

# Output results
sum_frac.display()  # Display the simplified sum
product_frac.display()  # Display the simplified product