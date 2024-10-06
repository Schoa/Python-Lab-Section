def addition (*num):
    sum = 0
    for n in num:
        sum = n  + sum
    print ("num =", sum)

addition(9, 10, 11)