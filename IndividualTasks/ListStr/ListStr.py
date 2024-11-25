# Дана строка, заканчивающаяся нулем. Ноль в этой последовательности единственный, среди символов обязательно есть другие десятичные цифры. 
# Написать программу, которая составляет из  цифр этой строки число-палиндром максимальной длины. 
# Если таких чисел несколько, нужно вывести минимальное из них. Ноль является единственным символом, обозначающим конец ввода. 
# В числе не должно быть нулей, все имеющиеся цифры должны быть использованы. Например, если исходная последовательность была такая:
# for i:=99921 downto 20 
# то результат должен быть следующий:
# 29192

# Ввод строки
input_strings = input("Введите строку (заканчивается на '0'): ")
input_string = ''.join(char for char in input_strings if char.isdigit())
digit_count = [0] * 10 # массив с количеством цифр в числе
# Подсчет частоты цифр
for char in input_string:
    if char == '0':
        break
    digit_count[int(char)] += 1
half_palindrome = [] #половина палиндрома
middle_digit = None #серединный символ
# Формирование половины палиндрома
for digit in range(1, 10):
    count = digit_count[digit]
    if count == 1:
        if middle_digit == None or digit < middle_digit:
            middle_digit = digit
    else:
        for i in range(1, count//2+1):
            half_palindrome.append(digit)
# Формируем палиндром
palindrome = ''.join(map(str, half_palindrome))
if middle_digit is not None:
    palindrome += str(middle_digit)
palindrome += ''.join(map(str, half_palindrome[::-1]))
# Вывод результата
print(palindrome)