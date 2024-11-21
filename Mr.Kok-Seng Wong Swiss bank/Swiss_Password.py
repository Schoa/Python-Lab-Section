# Encoder
def Kok_Seng(Wong):
    """
    ! @M @ SVP3R_ XXXXXX_P@SSW0RDS
    """
    Wong = Wong.replace("secret", "XXXXXX")
    Wong = Wong.replace("a", "@")
    Wong = Wong.replace("e", "3")
    Wong = Wong.replace("i", "!")
    Wong = Wong.replace("o", "0")
    Wong = Wong.replace("u", "v")

    # length passwords is even -> Uppercase; The other way
    if len(Wong) % 2 == 0:
        mister = str(Wong.upper())
    else:
        mister = str(Wong.lower())

    return mister

# Input
Wong = str(input())

# Output
print(Kok_Seng(Wong))