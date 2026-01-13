file = open("numbers.txt")

for line in file:
	number = int(line)
	print(number * 2)

file.close()