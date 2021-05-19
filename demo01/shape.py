class Shape():

    # 定义图形位置
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    # 移动图形的坐标
    def move(self, delta_x, delta_y):
        self.x = delta_x + self.x
        self.y = delta_y + self.y
