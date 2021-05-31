# 字典列表
user_0 = {'name': 'luna', 'age': 11}
user_1 = {'name': 'eureka', 'age': 21}
user_2 = {'name': 'momo', 'age': 15}

users = [user_2, user_1, user_0]

for user in users:
    print(user)

# 在字典中存储列表
users_1 = {
    'name': 'luna',
    'datas': ['a', 'b'],
    'age': 14
}

print("名字：" + users_1['name'])
print(users_1['datas'])
for data in users_1['datas']:
    print("数据：" + data)

# 在字典中存储字典
users_2 = {
    'luna': {
        'data': ['1', '2']
    },
    'eureka': {
        'data': ['3', '4']
    }
}

for name, user in users_2.items():
    print("姓名：" + name)
    print(user['data'])
