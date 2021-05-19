from shape import Shape

class Circle(Shape):  #类的继承
    
    PI = 3.14
    all_circles = [] # 把所有的初始化实例放到这个类属性中

    def __init__(self, r=1, x=0,  y=0) -> None:
        super().__init__(x, y)  #通过super() 调用父类的 __init__() 方法。
        self.radius = r
        # self.all_circles.append(self)  #可以用实例调用 类属性
        # print(self.__class__) == Circle
        # self.__class__.all_circles.append(self)
        Circle.all_circles.append(self)  #也可以用类

    @classmethod
    def totle_area(cls): #类方法  cls 
        area = 0
        for circle in cls.all_circles:
            area += cls.circle_area(circle.radius)  #使用类直接调用静态方法
        return area

    @staticmethod
    def circle_area(radius):  #静态方法， 第一个参数 不用像实例和类方法
        return Circle.PI * radius * radius


if __name__ == '__main__':

    c1 = Circle()
    print(c1.radius, c1.all_circles, Circle.totle_area())
    c2 = Circle(2)
    print(c2.radius, c2.all_circles, Circle.totle_area())