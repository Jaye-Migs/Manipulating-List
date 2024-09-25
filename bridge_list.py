bridge = ['Tower Bridge', 'Brooklyn Bridge', 'Sydney Harbour Bridge', 'London Bridge', 'Charles Bridge', 'Forth Bridge', 'Pont du Gard', 'Akashi Kaikyou Bridge']
print(bridge)

print("3rd bridge is: ", bridge[2])

bridge[5] = 'Golden Gate Bridge'
print(bridge)

del bridge[6]
print(bridge)

print("Last bridge is: ", bridge[-1])