"""
Нужно реализовать функцию OneEditApart ,
проверяющую, можно ли одну строку получить из другой не более,
чем за одно исправление (удаление, добавление, изменение символа):

f("ab", "ac") == True
f("abd", "act") == False
f("abad", "acat") == False
f("ab", "с") == False
f("ab", "b") == True
"""


# компактная реализация не проходящая по константной памяти
# def check_str(str_1, str_2):
#     for p in range(min(len(str_1), len(str_2))):
#         if str_1[p] != str_2[p]:
#             return str_1[p+1:] == str_2[p+1:] or str_1[p+1:] == str_2[p:] or str_1[p:] == str_2[p+1:]
#     return True


def check_str(str_1, str_2):
    def compare_from_p(p1, p2):
        min_len = min(len(str_1) - p1, len(str_2) - p2)
        max_len = max(len(str_1) - p1, len(str_2) - p2)
        if max_len - min_len > 0:
            return False
        for i in range(min_len):
            if str_1[p1] != str_2[p2]:
                return False
            p1 += 1
            p2 += 1
        return True
    
    if abs(len(str_1)-len(str_2)) > 1:
        return False

    for p in range(min(len(str_1), len(str_2))):
        if str_1[p] != str_2[p]:
            return compare_from_p(p+1, p+1) or \
                   compare_from_p(p, p + 1) or \
                   compare_from_p(p + 1, p)
    return True


assert check_str("ab", "ac") == True
assert check_str("abd", "act") == False
assert check_str("abad", "acat") == False
assert check_str("abad", "acad") == True
assert check_str("ab", "с") == False
assert check_str("ab", "b") == True
assert check_str("abb", "a") == False
