# 使用函数 range()
for value in range(1, 7):
    print(value)

# 使用 range()创建数字列表
numbers = list(range(1, 7))
print(numbers)
# 使用函数range()时，还可指定步长
even_numbers = list(range(1, 7, 2))
print(even_numbers)

squares = []
for value in range(1, 10):
    square = value ** 2
    squares.append(square)
print(squares)

# 对数字列表执行简单的统计计算
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares)
