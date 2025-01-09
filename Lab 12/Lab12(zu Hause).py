class Polynomial:
    def __init__(self, coefficients):
        """Constructor to initialize the list of coefficients."""
        self.coefficients = coefficients

    def __add__(self, other):
        """Overload the + operator to add two polynomials"""
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coeffs = [0] * max_len

        for i in range(max_len):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs[i] = coeff1 + coeff2

        return Polynomial(new_coeffs)
    
    def __mul__(self, other):
        """Overload the * operator to multiply two polynomials."""
        new_degree = len(self.coefficients) + len(other.coefficents) - 1
        new_coeffs = [0] * new_degree

        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                new_coeffs[i + j] += self.coefficients[i] * other.coefficients[j]

        return Polynomial(new_coeffs)
    
    def degree(self):
        """Return the degree of the polynomial."""
        for i in reversed(range(len(self.coefficients))):
            if self.coefficients[i] != 0:
                return i
            return -1 # If all coefficients are zero


# Input
poly1_coeffs = list(map(int, input().split()))
poly2_coeffs = list(map(int, input().split()))

# Create Polynomial instances
poly1 = Polynomial(poly1_coeffs)
poly2 = Polynomial(poly2_coeffs)

# Calculate sum and product of polynomials
sum_poly = poly1 + poly2_coeffs
product_poly = poly1 * poly2

print(sum_poly)