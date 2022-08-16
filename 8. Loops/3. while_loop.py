a = 1

# Simple while loop
# while a < 6:
#     print(a)
#     a+=1

# if loop in while loop
while a < 6:
    print(a)
    a += 1
    if a == 2:
        # break
        continue
else:
    print("All numbers less than 6 are printed")
