# 方法 sort()对列表进行永久性排序
dogs = ["a1", "a3", "a2", "b1", "b3", "b2"]
print(dogs)
dogs.sort()
print(dogs)
# 序相反的顺序排列
dogs.sort(reverse=True)
print(dogs)

# 使用函数 sorted()对列表进行临时排序
cats = ["a1", "a3", "a2", "b1", "b3", "b2"]
print(cats)
print(sorted(cats))
print(sorted(cats, reverse=True))
print(cats)

# 倒着打印列表
cats.reverse()
print(cats)

# 确定列表的长度
catsLen = len(cats)
print(catsLen)
