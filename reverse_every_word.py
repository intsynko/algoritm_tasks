
"""
Написать функцию, которая бы переварачивала каждое слово в строке, не 
меняя местами порядок слов


f("QUICK FOX JUMPS") == "KCIUQ XOF SPMUJ"
f("") == ""
f("QUICK") == "KCIUQ"
f(" QUICK ") == " KCIUQ "
"""


# def f(words):
#     return " ".join([word[::-1] for word in words.split(" ")])

"""
Теперь тоже самое, только расход по памяти должен быть O(1) и строку
мы меняем на массив символов

chars = list("QUICK FOX JUMPS")
# modify in-place

"""


def f(chars: str):
    def move_to_begin(i_):
        """функция, двигающая указатель в начало след. слова"""
        while i_ < len(chars) and chars[i_] == ' ':
            i_ += 1
        return i_

    chars = list(chars)
    i = move_to_begin(0)
    begin = i
    while i <= len(chars):
        if i == len(chars) or chars[i] == ' ':
            end = i-1            
            while begin < end:
                chars[begin], chars[end] = chars[end], chars[begin]
                begin += 1
                end -= 1
            i = move_to_begin(i)
            begin = i
        i += 1
    return "".join(chars)


assert f("QUICK FOX JUMPS") == "KCIUQ XOF SPMUJ"
assert f("") == ""
assert f("QUICK") == "KCIUQ"
assert f(" QUICK ") == " KCIUQ "

