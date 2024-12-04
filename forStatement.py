temperature =  [23, 25, 30, 32, 28, 29, 25]
print(type(temperature[1]))
for t in temperature:
    if t < 30: print(str(t) + ': Temperature is less than 30') #convert int to str bcoz combine with words afterward