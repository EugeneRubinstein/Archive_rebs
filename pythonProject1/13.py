#
#
# ## 16 to 10
# hex_number = 444
# a = hex(hex_number)
# print(a)
#
# # ## 8 to 10
# # octal_number = "754"
# # decimal_number = int(octal_number, 8)
# #
# # ## 2 to 10 /////4 is not exist
# # octal_number = '10'
# # decimal_number = int(octal_number, 2)
# #
# # ##### 10 to 2
# # decimal_number = 4
# # binary_number = bin(decimal_number)
# #
# # ##### 10 to 8
# # decimal_number = 4
# # octal_number = oct(decimal_number)
#
# ##### 10 to 16
# decimal_number = 444
# hex_number = hex(decimal_number)
# print(hex_number)
#


#########################################

## 16 to 10
# hex_number = 444
# a = hex(hex_number)

### 10 to 16

# print(int("432AA1", 16))
#
# # decimal_number = 4
# # octal_number = oct(decimal_number)
# # print(octal_number)
#
# decimal_number = 4321324
# binary_number = bin(decimal_number)
# print(binary_number)





def defolt_to_bin(defolt):
    return print(bin(defolt))


def defolt_to_oct(defolt):
    return print(oct(defolt))


def defolt_to_hex(defolt):
    return print(hex(defolt))


def bin_to_defolt(defolt):
    plus = add_symbols("''",defolt,"''")
    return print(int(plus,2))


def oct_to_defolt(defolt):
    return print(int(defolt,8))


def hex_to_defolt(defolt):
    return print(int(defolt,16))

def add_symbols(s, before, after):
    return before + s + after



print("Напишите желаемую вам конвертацию . Вы можете выбрать из 10(обычное), 2(бинарное),  8 , 16")

ishodnoe = input("Введите исходное значение :")
zelevoe= input("Введите целевое значение :")
numbers= int(input("Введите число :"))


if ishodnoe == "10" and zelevoe == "2":
    defolt_to_bin(numbers)
elif ishodnoe == "10" and zelevoe == "8":
    defolt_to_oct(numbers)
elif ishodnoe == "10" and zelevoe == "16":
    defolt_to_hex(numbers)
elif ishodnoe == "2" and zelevoe == "10":
    bin_to_defolt(numbers)
elif ishodnoe == "8" and zelevoe == "10":
    oct_to_defolt(numbers)
elif ishodnoe == "16" and zelevoe == "10":
    hex_to_defolt(numbers)
else:
    raise TypeError("Не правильный вод, Исходное число должно быть 10 либо 2 либо 8 , либо 16 . Целевое так же ")
