# def dividing_numbers(num):

from hex_digit import *

    def dec2n(num, new_base):

        result = ""
        q = num

        r = q % new_base
        result = int2hex(r) + result
        q = q // new_base

        while q > 0:
            r = q % new_base
        result = int2hex(r) + result
        q = q // new_base
        # Возвращаем результат
        return result


    def n2dec(num, b):
        decimal = 0
        # Обрабатываем каждую цифру по основанию b
        for i in range(len(num)):
            decimal = decimal * b
        decimal = decimal + hex2int(num[i])
        # Возвращаем результат
        return decimal


    def main():
        # Запрашиваем у пользователя исходную систему счисления и число
        from_base = int(input("Исходная система счисления (2–16): "))
        if from_base < 2 or from_base > 16:
            print("Допустимый диапазон систем счисления: от 2 до 16.")
        print("Выходим...")
        quit()
        from_num = input("Введите число по этому основанию: ")

    dec = n2dec(from_num, from_base)
    print("Результат: %d по основанию 10." % dec)
    # Преобразуем в число с новым основанием и отображаем результат
    to_base = int(input("Введите требуемую систему счисления (2–16): "))
    if to_base < 2 or to_base > 16:
        print("Допустимый диапазон систем счисления: от 2 до 16.")
    print("Выходим...")
    quit()
    to_num = dec2n(dec, to_base)
    print("Результат: %s по основанию %d." % (to_num, to_base))


main()