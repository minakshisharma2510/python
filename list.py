# animals = ["dog", "cat", "cow", "fox", "bear"]
# print(animals)
# print(type(animals))

# nums = [1, 2, 3, 4, 5]
# print(nums)
# print(type(nums))
# nums[2]=100
# print(nums)
# nums[4]=22
# print(nums)
# nums [3]= 11
# print(nums)
# nums[0]= "hello"
# print(nums)
# nums[0]= 99
# print(nums)

# num = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# del num[2]
# print(num)
# num.remove(10)
# print(num)
# num.pop(1)
# print(num)
# num.pop()
# print(num)
# num.clear()
# print(num)

# num = [1, 2, 3, 4, 5, 9]
# num[num.index(9)] = 99
# print(num)

# nums = [3, 6, 9, 12, 15]
# nums[nums.index(9)] = 99
# print(nums)

# a = [1, 2, 3]
# b = a
# b.append(4)
# print("a =", a)
# print("b =", b)           #yhan a or b alg alag list nhi bni hai jbki a or b dono ik hi list ko refrence kr rahe hai, b = a is tarah se list asign hoti hai na ki list ki copy nhi banti hai, refrence share hota hai

# a = [3,5,7,  (b:= (4, 6))]
# print(a)
# print(b)
# print("b has", type(b), "type")

# color = ["red", "blue", "green"]
# b = [1, 2, 3]
# color.insert(1, "yellow")
# color.append("black")
# # color.sort(reverse=False)
# color.extend(b)
# color.insert(4, "blue")
# color.pop(0)
# color.index(1, 4)
# print(color)

# item = [1, 2, 3, 4, 5]
# for i in item:
#     if i % 2 == 0:
#      item.remove(i)
# print(item)

# item = [1, 2, 3, 4, 5]
# result = []

# for i in item:
#     if i % 2 != 0:
#         result.append(i)

# print(result)  # Output: [1, 3, 5]
# print(type(result))
# item.

my_list  = [1, 2, 3, 4]
# my_list = my_list[::-1]
reversed(my_list)
print(my_list)