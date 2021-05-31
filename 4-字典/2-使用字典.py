alien_0 = {'color': 'green', 'points': 5}

# 访问
print(alien_0['color'])

# 添加
alien_0['x_p'] = 0
alien_0['y_p'] = 25
print(alien_0)

# 创建空字典
alien_1 = {}
alien_1['xp'] = 12
alien_1['yp'] = 23
print(alien_1)

# 修改
alien_0['color'] = 'red'
print(alien_0)

# 删除
del alien_0['color']
print(alien_0)

# 由类似对象组成的字典
fv_lns = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(fv_lns)

# 遍历
for key, value in fv_lns.items():
    print('key:' + key)
    print('value:' + value)

for key in sorted(fv_lns.keys()):
    print('key:' + key)

for value in fv_lns.values():
    print('value:' + value)
