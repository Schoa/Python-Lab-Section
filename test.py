Kok_Seng = input()
Wong = Kok_Seng.split("-")

def ah(Wong):
    """
    Year - Month - Day

    Year: 0
    Month: 1
    Day: 2
    """
    if int(Wong[1]) <= 12:
        month = True
    else:
        month = False

    if int(Wong[2]) <= 31: # day <= 31
        if int(Wong[1]) == ["1", "3", "5", "7", "8", "10", "12"]: # Month with 31 days
            if int(Wong[2]) <= 31:
                day = True
            else:
                day = False
        else:
            if int(Wong[1]) != 2: # Month with 30 days
                if int(Wong[2]) <= 30:
                    day = True
                else:
                    day = False
            else:
                if int(Wong[2]) <= 28: # Feburary
                    day = True
                else:
                    day = False
    else:
        day = False

    if month == True and day == True:
        print("True")
    else:
        print("False")

ah(Wong)