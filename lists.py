List_numbers = [1, 2, 3, 4, 5]

list_names = ['Patience', 'Joyce', 'Mary', 'Grace']

list_list = [12, 'Jean', [1.2, 3.3, 6.0]]

mylist = ['banana', 'cherry', 99]

mylist.insert(2, 'orange')
print(mylist)

#print(list_list)
list_list.append('Joyce')
list_list.append(23)
#print(list_list)

removed = List_numbers.pop(3)
removed2 = List_numbers.pop(0)
print(List_numbers)

print(removed)
List_numbers.append(removed)
List_numbers.append(removed2)
print()
List_numbers.sort()
print(List_numbers)

List_numbers[2] = 'Patience'

print()
print(List_numbers)

