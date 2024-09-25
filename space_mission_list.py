mission = ['Voyager 1', 'Voyager 2', 'Mars Rover Curiosity', 'Hubble Space Telescope', 'International Space Station', 'Chandrayaan-1', 'New Horizons', 'Mars Exploration Rover Spirit', 'Gemini 12', 'Juno']
print(mission)

print("7th space mission is: ", mission[6])

mission[3] = 'Apollo 11'
print(mission)

del mission[5]
print(mission)

print("Last space mission is: ", mission[-1])