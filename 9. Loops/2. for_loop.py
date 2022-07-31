a = ['Banana', 'Cononut', 'Apple', 'Car', 'Bike', 'Truck', 'Train', 'Plain']
b = [1,2,3,4,5,6,7,8]

# for lists in a:
#     print(lists)
#     if lists == 'Bike':
#         break

# for a in range(1, 11, 2):
#     print(a)
# else:
#     print('Iteration done!')

for nums in b:
    for objs in a:
        print(str(nums) + '.' + objs)