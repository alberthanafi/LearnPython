manufacturer =  ['Honda', 'Toyota', 'Nissan', 'Kia', 'Hyundai', 'Kia']

print(type (manufacturer))
print(type(manufacturer[3]))

print('No. of Kia is ' + str(manufacturer.count('Kia')))
print('No. of Honda is ' + str(manufacturer.count('Honda')))

manufacturer.insert(3,'Daihatsu')
print(manufacturer)
