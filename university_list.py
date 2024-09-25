university = ['Stanford University', 'Massachusetts Institute of Technology', 'California Institute of Technology', 'University of Chicago', 'Columbia University', 'Princeton University', 'Yale University', 'University of Cambridge', 'University of Oxford', 'University of California, Berkeley']
print(university)

print("6th university is: ", university[5])

university[3] = 'Harvard University'
print(university)

del university[8]
print(university)

print("Last university is: ", university[-1])