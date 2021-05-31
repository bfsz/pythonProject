# 返回简单值
def get_formatted_name(f_name, l_name):
    return f_name + ' ' + l_name


name = get_formatted_name('李', '四')
print(name)


# 让实参变成可选的 返回字典
def get_datas(x_p, y_p, data=""):
    if data:
        msg = {'x': x_p, 'y': y_p, 'data': data}
    else:
        msg = {'x': x_p, 'y': y_p, 'data': 'null'}

    return msg


postions_a = get_datas(100, 200, "学校")
postions_b = get_datas(10, 20)
print(postions_a)
print(postions_b)

