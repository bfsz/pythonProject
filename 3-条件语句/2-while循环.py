# 使用
current = 1
while current <= 5:
    print(current)
    current += 1

# 标志
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n--------------(Enter 'q' when you are finished.) "
active = True
while active:
    msg = input(prompt)
    if msg == 'q':
        active = False
    else:
        print(msg)

# 使用 break 退出循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n--------------(Enter 'q' when you are finished.) "
while True:
    msg = input(prompt)
    if msg == 'q':
        break
    else:
        print(msg)

# 在循环中使用 continue
current_num = 0
while current_num < 10:
    current_num += 1
    if current_num % 2 == 0:
        continue
    print(current_num)
