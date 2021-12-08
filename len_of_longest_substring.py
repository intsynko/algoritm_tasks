"""
Найти длину самой длинной подстроки с неповторяющимися символами.
Пример:
    f("abcabcbb") = 3 (abc) 
    f("bbbbb") = 1 (b)
    f("pwwkew") = 3 (wke)
    f("") = 1 ("")
"""


def len_of_longest_substring(s):
    max_len = 0
    stack = list()
    for i in range(len(s)):
        if s[i] not in stack:
            stack.append(s[i])
        elif s[i] == stack[0]:
            stack = stack[1:] + [stack[0],]
        else:
            if len(stack) > max_len:
                max_len = len(stack)
            stack = stack[stack.index(s[i])+1:] + [s[i],]
    if len(stack) > max_len:
        max_len = len(stack)
    return max_len


assert len_of_longest_substring("abcabcbb") == 3
assert len_of_longest_substring("bbbbb") == 1
assert len_of_longest_substring("pwwkew") == 3
assert len_of_longest_substring("") == 0
assert len_of_longest_substring("ggububgvfk") == 6
