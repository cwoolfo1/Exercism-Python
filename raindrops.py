def convert(number):
    if number%3 == 0:
        str_num = str_num + "pling"
    if number%5 == 0:
        str_num = str_num + "plang"
    if number%7 == 0:
        str_num = str_num + "plong"

    return str_num if result else str(number)
