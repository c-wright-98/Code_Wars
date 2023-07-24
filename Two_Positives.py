def two_positives(a,b,c):
    if a > 0 and b > 0:
        return c <= 0
    if a > 0 and c > 0:
        return b <=0
    if c > 0 and b > 0:
        return a <= 0
    else:
        return False