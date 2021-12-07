"""
Проверить строку со скобками на валидность
Right
"()[]{}"
"([{}]){}"
"{}{}{}{{{{{}}}}}"

Wrong
"{)"
"{[](}"
"{[](})"

"{} - Braces"
"[] - square brackets"
 "() - parentheses"

"""


def checker(word):
    braces = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []
    for c in word:
        if c in braces.values():
            stack.append(c)
        if c in braces.keys():
            if len(stack) == 0:
                return False
            if braces[c] != stack.pop():
                return False
    return len(stack) == 0


assert checker("()[]{}") == True
assert checker("([{}]){}") == True
assert checker("{}{}{}{{{{{}}}}}") == True

assert checker("{)") == False
assert checker("{[](") == False
assert checker("{[](}") == False

