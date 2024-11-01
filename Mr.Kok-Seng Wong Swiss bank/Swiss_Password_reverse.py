# Reverse
def Ali(Baba):
    Baba = Baba.replace("XXXXXX", "secret")
    Baba = Baba.replace("@", "a")
    Baba = Baba.replace("3", "e")
    Baba = Baba.replace("!", "i")
    Baba = Baba.replace("0", "o")
    Baba = Baba.replace ("v", "u")

    if len(Baba) % 2 == 0:
        Kok_Seng = str(Baba.lower())
    else:
        Kok_Seng = str(Baba.upper())

    return Kok_Seng

# Input
Baba = str(input())

# Print result
print(Ali(Baba))