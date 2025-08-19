# compare 2 lists in python for similar numbers
list1 = [6, 3, 22, 21, 18, 29, 24, 18, 22, 13]
list2 = [3, 1, 13, 25, 7, 14, 23, 25, 22, 29]

new_list = list(set(list1) & set(list2))
print(f"&: {new_list}")

common_numbers = [num for num in list1 if num in list2]
print(set(common_numbers))
