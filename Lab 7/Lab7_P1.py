# Input from the user
Wong = int(input())

# Draw Pyramid
def Kok_Seng(Wong):
    # Loop through each row
    for Vinuni in range(Wong):
        # Leading space for aligment
        print(" " * (Wong - Vinuni - 1), end="")

        # Print stars
        print("*" * (2 * Vinuni + 1))

print(Kok_Seng(Wong))