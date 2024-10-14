"""
Дан массив целых чисел, нужно найти непустой подотрезок (непрерывную подпоследовательность)
с заданной суммой target, либо сказать, что это невозможно.
find_target([9, -6, 5, 1, 4, 7], 10) -> (2, 4)
"""


def kek(nums, target):
    inter_sum = 0
    prefix_sum = []
    prefix_sum_map = defultdict(defult=list())
    for index, value in enumerate(nums):
        if value == target:
            return index, index
        inter_sum += value
        prefix_sum.append(inter_sum)
        prefix_sum_map[inter_sum].append(index)
    
    for index, value in enumerate(prefix_sum):
        if value == target:
            return 0, index
        if prefix_sum_map.get(value + target):
            if prefix_sum_map[value + target][-1] > index+1:
                return (index+1, prefix_sum_map[value + target][-1])
    
    return None, None




















