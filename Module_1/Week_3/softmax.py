"""
Viết class và cài phương thức softmax.
Trong pytorch, torch.nn.Module là lớp cơ bản để từ đó xây dựng lên các mô hình hoặc các phương
thức kích hoạt (activation funtion) như sigmoid, softmax,... Trong phần này, chúng ta xây dựng
class Softmax và softmax_stable nhận đầu vào là mảng 1 chiều (tensor 1 chiều) dựa vào kế thừa
từ lớp Module và ghi đè vào phương thức forward():
"""
import torch
import torch.nn as nn

# Define Softmax class


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        return exp_x / torch.sum(exp_x)

# Define SoftmaxStable class


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x - torch.max(x))
        return exp_x / torch.sum(exp_x)


if __name__ == "__main__":
    x = torch.tensor([1, 2, 3])
    print("data :", x)

    softmax = Softmax()
    print("Softmax result:", softmax(x))

    softmax_stable = SoftmaxStable()
    print("SoftmaxStable result:", softmax_stable(x))
