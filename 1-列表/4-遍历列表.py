dogs = ["a1", "a3", "a2", "b1", "b3", "b2"]

# 遍历
for dog in dogs:
    print(dog)

# 在 for 循环中执行更多的操作
for dog in dogs:
    print(dog.title() + " 是一只狗！")

# 在 for 循环结束后执行一些操作
for dog in dogs:
    print(dog + "狗")
print("结束...")
