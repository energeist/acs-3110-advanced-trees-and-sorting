def raise_power(base, power):
    # base case
    # if power is 0, return 1
    if power == 0:
        return 1

    # otherwise, go through recursive cases
    else:    
    # positive power case
    # if power is greater than 0
    # return the base number multiplied by a recursive call to to raise_power with
    # parameters that are the base number power - 1
        if power > 0:
            return base * raise_power(base, power - 1)
    # negative power case
    # call with raise_power(4, -3)
        else:
            return 1 / (base * raise_power(base, -power - 1))
    # if power is less than 0
    # return 1 divided by the result of the base number multipled by a recursive call to
    # raise power function with with base number and negative value of our power
    
# positive base positive power test cases
print(raise_power(4,2)) # 16
print(raise_power(3,3)) # 27
print(raise_power(10,2)) # 100

# negative base positive power test cases
print(raise_power(-4,2)) # 16
print(raise_power(-3,3)) # -27
print(raise_power(-10,2)) # 100

# positive base negative power test cases
print(raise_power(4,-2)) # 1/16 (0.0625)
print(raise_power(3,-3)) # 1/27 (0.037 repeating)
print(raise_power(10,-2)) # 1/100 (0.01)

# negative base negative power test cases
print(raise_power(-4,-2)) # 1/16 (0.0625)
print(raise_power(-3,-3)) # 1/-27 (-0.037 repeating)
print(raise_power(-10,-2)) # 1/100 (0.01)