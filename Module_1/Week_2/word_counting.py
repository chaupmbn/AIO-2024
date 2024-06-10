"""
Viết function đọc các câu trong một file txt, đếm số lượng các từ xuất hiện và trả về một dictionary
với key là từ và value là số lần từ đó xuất hiện.
    • Input: Đường dẫn đến file txt
    • Output: dictionary đếm số lần các từ xuất hiện
    • Note:
        - Giả sử các từ trong file txt đều có các chữ cái thuộc [a-z] hoặc [A-Z]
        - Không cần các thao tác xử lý string phức tạp nhưng cần xử lý các từ đều là viết
    thường
        - Các bạn dùng lệnh này để download
        !gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
"""

def word_counting(file_path):
    content = open(file_path, "r") # Read file from the path
    words = content.read().split() # Create a list of separated words
    count = dict() # Create a emply dictionary
    for word in words:
        if word.lower() not in count.keys():
            count[word.lower()] = 1
        else:
            count[word.lower()] += 1
    return count

file_path = "/Users/chaupham/Data_Science/AIO-2024/Module_1/Week_2/P1_data.txt"
print("word_count(file_path): \n", word_counting(file_path))