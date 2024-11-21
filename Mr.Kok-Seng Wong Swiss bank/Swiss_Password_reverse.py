# Reverse
def Seng_Kok(Wong):
    Wong = Wong.replace("XXXXXX", "secret")
    Wong = Wong.replace("@", "a")
    Wong = Wong.replace("3", "e")
    Wong = Wong.replace("!", "i")
    Wong = Wong.replace("0", "o")
    Wong = Wong.replace("v", "u")

    if len(Wong) % 2 ==0:
        mister = str(Wong.lower())
    else:
        mister = str(Wong.upper())
    
    return mister

# Input
Wong = str(input())

# Output
print(Seng_Kok(Wong))