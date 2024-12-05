import re

def parse_line(line):
    first_num = int(re.search(r'.....\s\s\s', line).group())
    second_num = int(re.search(r'\s\s\s.....', line).group())
    return first_num, second_num

def compute_similarity(nums1, nums2):
    nums1.sort()
    nums2.sort()

    total = 0
    for i in range(len(nums1)):
        x = 0
        for j in range(len(nums1)):
            if nums1[i] == nums2[j]:
                x += 1
        total += nums1[i] * x
    return total

first_nums = []
second_nums = []

with open('input') as f:
    lines = f.readlines()
    for line in lines:
        first_num, second_num = parse_line(line)
        first_nums.append(first_num)
        second_nums.append(second_num)

print(compute_similarity(first_nums, second_nums))
