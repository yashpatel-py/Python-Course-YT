a = ('apple', 'banana', 'coconut', 'apple')
print("This is tuple --> ", a)

# Convert tuple to list
convert_list = list(a)
print("This is list --> ", convert_list)

# Updating list
convert_list.append('Car')
print('Updated list --> ', convert_list)

# Convert list to tuple
tuple_1 = tuple(convert_list)
print("Updated tuple --> ", tuple_1)