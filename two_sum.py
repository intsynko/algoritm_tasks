"""
Данн массив целых чисел nums и целое число target, верните индекс двух чисел таких что их сумма равна target.
Вы можете полагаться, что для каждого набора входных данных существуе только одно решение и вы не можете 
использовать один и тот же элемент дважды.
Вы можете вернуть ответ в любом порядке.

Пример 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Пример 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Пример 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Ограничения:
2 <= nums.length <= 1.000.000.000
-109 <= nums[i] <= 109
-109 <= target <= 109
Существует только одно валидное решение.
"""


# самое простое решение в лоб полным перебором
# сложность тут O(n^2)
# но при этом память остается константой
# def get_target_indexes(nums, target):
#     for i in range(len(nums)):
#         for j in range(1, len(nums)-i):
#             print(i, i + j)
#             if nums[i] + nums[i+j] == target:
#                 return i, i+j


# используя хэш таблицу для хранения пройденых чисел
# тут сложность O(n)
# но при этом идет расход памяти на объект previous
def get_target_indexes(nums, target):
    previous = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        val = previous.get(complement)
        if val is not None:
            return val, i
        previous[nums[i]] = i


assert get_target_indexes(nums=[2, 7, 11, 15], target=9) == (0, 1)
assert get_target_indexes(nums=[2, 7, 11, 17, 15], target=11+15) == (2, 4)
