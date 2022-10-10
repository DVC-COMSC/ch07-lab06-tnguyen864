# Get values for list 
inputvalues = input('Enter all elements values: ')
numbers1 = inputvalues.split() 
for i in range(len(numbers1)):
	numbers1[i] = int(numbers1[i]) 

# Print old list
print("The original list:", numbers1)

# New list
numbers2 = []

# Get elements from first list and add to new list in reverse
i = 0
for i in range(len(numbers1)):
	num = numbers1.pop()
	numbers2.append(num)

# Print old and new list
print("The new list:", numbers2)