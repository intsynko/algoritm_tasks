"""
Написать функцию производящую поиск по строке индекса начала заданаго шаблона за линейную сложность.
Шалон задается в виде словаря с ключами - символами и значениями - цифрами (сколько раз должна
встретиться данная буква)
Пример:

assert get_pattern_index(str_: "aaababa", pattern={'a':2, 'b': 2}) == 2
"""


def get_pattern_index(str_: str, pattern: dict):
    i = 0
    pattern_sum = sum(pattern.values())
    while i < len(str_):
        if str_[i] in pattern.keys():
            pattern_copy = pattern.copy()
            j = 0
            while sum(pattern_copy.values()) > 0:
                if pattern_copy.get(str_[i]) is None:
                    break
                if pattern_copy[str_[i]] == 0:
                    # если текеущий символ != символу с которого начался шаблон
                    if pattern_copy[str_[i]] != pattern_copy[str_[i-j]]:
                        break
                else:
                    pattern_copy[str_[i]] -= 1
                i += 1
                j += 1
            if sum(pattern_copy.values()) == 0:
                return i-pattern_sum
        i += 1
    return -1


assert get_pattern_index(str_="lsddksl12", pattern={'d': 2, 'k': 1}) == 2
assert get_pattern_index(str_="aaabbbaccc", pattern={'a': 1, 'c': 2}) == 6
assert get_pattern_index(str_="aaabbbccc", pattern={'d': 2}) == -1
assert get_pattern_index(str_="aaabbcbccc", pattern={'b': 2, 'c': 2}) == 4
assert get_pattern_index(str_="aaabbacbbccc", pattern={'b': 2, 'c': 2}) == 6
