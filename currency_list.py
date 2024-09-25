Currency = ['United States Dollar', 'British Pound Sterling', 'Japanese Yen', 'Canadian Dollar', 'Australian Dollar', 'Swiss Franc', 'Chinese Yuan', 'Indian Rupee', 'Brazilian Real', 'South African Rand']
print(Currency)

print("4th currency is: ", Currency[3])

Currency[6] = 'Euro'
print(Currency)

del Currency[8]
print(Currency)

print("Last currency is", Currency[-1])