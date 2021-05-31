# 1 、位置实参
def dec_pet(pet_type, pet_name):
    print("pet_name:" + pet_name)
    print("pet_type:" + pet_type)


dec_pet('猫', 'lolo')
dec_pet('狗', 'yolo')


# 2、关键字实参
def dec_pet_b(pet_name, pet_type):
    print("petName:" + pet_name)
    print("petType:" + pet_type)


dec_pet_b(pet_name="欧珀", pet_type="狗")


# 3、默认值
def dec_pet_c(pet_name, pet_type="狗"):
    print("petName:" + pet_name)
    print("petType:" + pet_type)


dec_pet_c("达瓦")
dec_pet_c("达瓦", '猫')

