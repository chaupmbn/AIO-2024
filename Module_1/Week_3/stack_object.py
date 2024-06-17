"""
Thực hiện xây dựng class Stack với các phương thức (method) sau đây
• .initialization method nhận một input "capacity": dùng để khởi tạo stack với capacity là số
lượng element mà stack có thể chứa
• .is_empty(): kiểm tra stack có đang rỗng
• .is_full(): kiểm tra stack đã full chưa
• .pop(): loại bỏ top element và trả về giá trị đó
• .push(value) add thêm value vào trong stack
• .top() lấy giá trị top element hiện tại của stack, nhưng không loại bỏ giá trị đó
• Không cần thiết phải thực hiện với pointer như trong hình minh họa
"""


class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def push(self, value):
        if self.is_full():
            raise OverflowError("push to full stack")
        self.stack.append(value)

    def top(self):
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self.stack[-1]


if __name__ == "__main__":
    print("Stack is initialized with capacity = 3")
    stack1 = MyStack(capacity=3)
    print("Add number 1 to the stack")
    stack1.push(1)
    print("Add number 2 to the stack")
    stack1.push(2)
    print("Is stack full:", stack1.is_full())
    print("Top element:", stack1.top())
    print("Pop element:", stack1.pop())
    print("Top element after pop:", stack1.top())
    print("Pop element:", stack1.pop())
    print("Is stack empty?", stack1.is_empty())
