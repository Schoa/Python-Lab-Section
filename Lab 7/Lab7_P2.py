# Input
Wong = list(map(int, input().split()))

# Using a for loop
def smallest_integer_for(Wong):
    # Create a Set of Positive intergers
    Kok_Seng = set((num for num in Wong if num > 0))

    # Start checking from 1 upwards
    for Vinuni in range(1, len(Kok_Seng) + 2): # +2 to cover the case where all numbers are present
        if Vinuni not in Kok_Seng:
            
            return Vinuni

def smallest_integer_while(Wong):
    # Create a Set of Positive intergers
    Kok_Seng = set((num for num in Wong if num > 0))

    Alibaba = 1 #Starter

    while Alibaba in Kok_Seng:
        Alibaba += 1

    return Alibaba
    
# Print result
print(smallest_integer_for(Wong))
print(smallest_integer_while(Wong))