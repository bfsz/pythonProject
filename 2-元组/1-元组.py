# 定义 不能给元组的元素赋值
xyz = (1, 21, 34)
print(xyz[0] + xyz[1] + xyz[2])

# 遍历元组中的所有值
for num in xyz:
    print(num)

# 修改元组变量(虽然不能修改元组的元素，但可以给存储元组的变量赋值)
xyz = (2, 31, 21)
for num in xyz:
    print(num)
