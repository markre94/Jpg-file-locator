def convertToStr(n: tuple):
    return ",".join(str(x) for x in n)

print(convertToStr((1, 2.345)))