#lists
item= ['table','book', 'pen']
print(item)
numbers= ['23','42','12']
print(numbers)
#sorting items in list
numbers.sort()

numbers.append(24)
numbers.append(-62)
numbers.append(1)

print(numbers)

#inserting at a specific position
numbers.insert(0,26)
numbers.insert(5,12)
print(numbers)

#deletion of items in list
numbers.remove(24)
print(numbers)
numbers.pop()
print(numbers)

print("reverse",numbers[::-1])
print("Alternative", numbers[::-2])