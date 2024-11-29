def power8(n):
    return (n>0) and (n&(n-1)==0)and (n % 3 == 1)
print(power8(8))
print(power8(64))
print(power8(512))
print(power8(10))
print(power8(100))
print(power8(130))