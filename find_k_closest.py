"""
Массив целых чисел "a" отсортирован по неубыванию.

0 <= k <= len(a)
0 <= index < len(a)
len(a) > 0

Вернуть в произвольном порядке k ближайших к a[index] по значению элементов
"""

find_k_closest(a=[5, 5, 5, 5, 5, (5)], index=3, k=2) -> [5, 5]
find_k_closest(a=[2, 3, 5, 7, 11], index=3, k=2) -> [5, 7]
find_k_closest(a=[4, 12, 15, 15, 24], index=1, k=3) -> [12, 15, 15]
find_k_closest(a=[2, 3, 5, 7, 11], index=2, k=2) -> [3, 5] или [5, 7]
find_k_closest(a=[2, 3, 3, 5, 5, 5, 7, 7, 11], index=4, k=2) -> [5, 5]
find_k_closest(a=[2, 3, 3, 5, 5, 5, 7, 7, 11], index=4, k=3) -> [5, 5, 5]
find_k_closest(a=[2, 3, 3, 5, 5, 5, 7, 7, 11], index=4, k=4) -> [3, 5, 5, 5] или [7, 5, 5, 5]



def find_k_closest(nums: list[int], index: int, k: int):
    if k == 0:
        return []
    digit = nums[index]
    left, right = index, index
    result = [digit,]
    k -=1

    while k > 0:
        if left - 1 >= 0 and digit == nums[left - 1]:
            left -= 1
            result.append(nums[left])
            k-=1
        elif right + 1 < len(nums) and digit == nums[right + 1]:
            right += 1
            result.append(nums[right])
            k-=1
        else:
            break
           
    while k > 0:
        if left - 1 >= 0 and right + 1 < len(nums):
            if abs(digit - nums[left - 1]) < abs(digit - nums[right + 1]):
                left -= 1
                result.append(nums[left])
                k -= 1
            else:
                right += 1
                result.append(nums[right])
                k -= 1
        else:
            if left - 1 >= 0:
                left -= 1
                result.append(nums[left])
                k -= 1
            else:
                right += 1
                result.append(nums[right])
                k -= 1

    return result
