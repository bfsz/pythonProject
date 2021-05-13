# 切片
names = ['a', 'b', 'c', 'd', '121']
print(names[0:3])
# 没有指定第一个索引，Python将自动从列表开头开始：
print(names[:3])
# 让切片终止于列表末尾
print(names[1:])
# 输出名单上的最后三个
print(names[-3:])
# 遍历切片
for name in names[:3]:
    print(name)
# 复制列表
cp_names = names[:]
print(cp_names)
