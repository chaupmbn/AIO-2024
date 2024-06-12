"""
Khoảng cách Levenshtein.
Viết chương trình tính khoảng cách chỉnh sửa tối thiểu Levenshtein. Khoảng cách Levenshtein thể
hiện khoảng cách khác biệt giữa 2 chuỗi ký tự. Khoảng cách Levenshtein giữa chuỗi S và chuỗi T
là số bước ít nhất biến chuỗi S thành chuỗi T thông qua 3 phép biến đổi là:
• Xoá một ký tự
• Thêm một ký tự
• Thay thế ký tự này bằng ký tự khác
Khoảng cách này được sử dụng trong việc tính toán sự giống và khác nhau giữa 2 chuỗi, như
chương trình kiểm tra lỗi chính tả của winword spellchecker. Ví dụ: Khoảng cách Levenshtein
giữa 2 chuỗi "kitten" và "sitting" là 3, vì phải dùng ít nhất 3 lần biến đổi. Trong đó:
• kitten -> sitten (thay "k" bằng "s")
• sitten -> sittin (thay "e" bằng "i")
• sittin -> sitting (thêm ký tự "g")
"""
def levenshtein_distance(s, t):
    m, n = len(s), len(t)
    current_row = range(m + 1)
    for i in range(1, n + 1):
        previous_row, current_row = current_row, [i] + [0] * m
        for j in range(1, m + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if s[j - 1] != t[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[m]

source = "yu"
target = "you"
print(f"Levenshtein distance between '{source}' and '{target}' is {levenshtein_distance(source, target)}")
