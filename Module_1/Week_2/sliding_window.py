"""
Cho một list các số nguyên num_list và một sliding window có kích thước size k di
chuyển từ trái sang phải. Mỗi lần dịch chuyển 1 vị trí sang phải có thể nhìn thấy
đươc k số trong num_list và tìm số lớn nhất trong k số này sau mỗi lần trượt k phải
lớn hơn hoặc bằng 1
Input: num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1] với k=3
Output: [5, 5, 5, 5, 10, 12, 33, 33]
"""
# Define a function to find maximum number in a list
def max_finding(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

# Define the main function


def sliding(num_list, k):
    n = len(num_list)
    result = []
    for i in range(n - k + 1):
        window = num_list[i: (i+k)]
        result.append(max_finding(window))
    return result


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(sliding(num_list, k))