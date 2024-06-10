"""
Viết function trả về một dictionary đếm số lượng chữ xuất hiện trong một từ, với key là chữ cái
và value là số lần xuất hiện
    • Input: một từ
    • Output: dictionary đếm số lần các chữ xuất hiện
    • Note: Giả sử các từ nhập vào đều có các chữ cái thuộc [a-z] hoặc [A-Z]
"""
def char_counting(str):
    print("-----------------------------------------")
    print(f"String = '{str}'")
    count = dict()
    for char in str:
        if char not in count.keys():
            count[char] = 1
        else:
            count[char] += 1
    return count

for str in ["Happiness", "smiles"]:
    print("count_chars(string):", char_counting(str))