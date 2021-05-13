students = ['jim', 'tom', 'tim']

# 获取元素索引，指定该元素的值
students[-1] = "kit"
print(students)

# 在列表末尾添加元素
students.append("eureka")
print(students)

# 在列表中插入元素
students.insert(1, "luna")
print(students)

# 从列表中删除元素
del students[0]
print(students)

# 使用方法pop()删除元素,方法pop()可删除列表末尾的元素，并让你能够接着使用它
poped_students1 = students.pop()
print(students)
print(poped_students1)

# 弹出列表中任何位置处的元素
poped_students2 = students.pop(0)
print(students)
print(poped_students2)

# 根据值删除元素
nums = [1, 2, 3, 4, 5, 6]
print(nums)
nums.remove(4)
print(nums)
