class Polynomial:
    def __init__(self, coefficients):
        """Constructor to initialize the list of coefficients."""
        self.coefficients = coefficients  # Store coefficients in ascending order of powers

    def __add__(self, other):
        """Overload the + operator to add two polynomials."""
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coeffs = [0] * max_len
        
        for i in range(max_len):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs[i] = coeff1 + coeff2
        
        return Polynomial(new_coeffs)

    def __mul__(self, other):
        """Overload the * operator to multiply two polynomials."""
        new_degree = len(self.coefficients) + len(other.coefficients) - 1
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
        return -1  # If all coefficients are zero

    def __str__(self):
        """Return polynomial in standard mathematical notation."""
        terms = []
        for i, coeff in enumerate(self.coefficients):
            if coeff != 0:
                if i == 0:
                    terms.append(f"{coeff}")  # Constant term
                elif i == 1:
                    terms.append("x") if coeff == 1 else terms.append(f"{coeff}x")  # Linear term
                else:
                    if coeff == 1:
                        terms.append(f"x^{i}")  # Coefficient is 1
                    elif coeff == -1:
                        terms.append(f"- x^{i}")  # Coefficient is -1
                    else:
                        terms.append(f"{coeff}x^{i}")  # Higher degree terms
        
        # Join terms with proper formatting for negative signs
        formatted_poly = ""
        for term in terms:
            if formatted_poly == "":
                formatted_poly += term  # First term
            else:
                if term.startswith('-'):
                    formatted_poly += f" {term}"  # Negative term
                else:
                    formatted_poly += f" + {term}"  # Positive term

        return formatted_poly if formatted_poly else "0"


# Read input for two polynomials
poly1_coeffs = list(map(int, input().split()))
poly2_coeffs = list(map(int, input().split()))

# Create Polynomial instances
poly1 = Polynomial(poly1_coeffs)
poly2 = Polynomial(poly2_coeffs)

# Calculate sum and product of polynomials
sum_poly = poly1 + poly2
product_poly = poly1 * poly2

# Output results
print("Sum:", sum_poly)
print("Product:", product_poly)