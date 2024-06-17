"""
Thực hiện xây dựng class Queue với các chức năng (method) sau đây
• initialization method nhận một input "capacity": dùng để khởi tạo queue với capacity là
số lượng element mà queue có thể chứa
• .is_empty(): kiểm tra queue có đang rỗng
• .is_full(): kiểm tra queue đã full chưa
• .dequeue(): loại bỏ first element và trả về giá trị đó
• .enqueue(value) add thêm value vào trong queue
• .front() lấy giá trị first element hiện tại của queue, nhưng không loại bỏ giá trị đó
• Không cần thiết phải thực hiện với các pointers như trong hình minh họa
"""


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.q = []

    def is_empty(self):
        return len(self.q) == 0

    def is_full(self):
        return len(self.q) == self.capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.q.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("enqueue to full queue")
        self.q.append(value)

    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.q[0]


if __name__ == "__main__":
    print("Queue is initialized with capacity = 5")
    queue1 = Queue(5)
    print("Add number 1 to the queue")
    queue1.enqueue(1)
    print("Add number 2 to the queue")
    queue1.enqueue(2)
    print("Is queue full?", queue1.is_full())
    print("Front element:", queue1.front())
    print("Dequeue element:", queue1.dequeue())
    print("Front element:", queue1.front())
    print("Dequeue element:", queue1.dequeue())
    print("Is queue empty?", queue1.is_empty())
