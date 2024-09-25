animal = ['Lion-80km/h', 'Greyhound-72km/h', 'Elk-72km/h', 'Horse-64km/h', 'African Wild Dog-60km/h', 'Zebra-64km/h', 'Kangaroo-64km/h', 'Bison-48km/h', 'American Antelope-88km/h', 'Domestic Cat-48km/h', 'Ostrich-72km/h', 'Elephant-40km/h']
print(animal)

print("7th animal and its spees is: ", animal[6])

animal[8] = 'Cheetah-120km/h'
print(animal)

del animal[9]
print(animal)

print(animal[2:8])

print("Last animal and its speed is: ", animal[-1])