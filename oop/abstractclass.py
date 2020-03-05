# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     def __init__(self, color,  brand):
#         self.color = color
#         self.brand = brand
        
#     @abstractmethod
#     def show(self):
#         pass
    

# class Car(Vehicle):
    
#     def __init__(self, color, brand):
#         super().__init__(color, brand)
    
#     def show(self):
#         print(self.color, self.brand)

# if __name__ == "__main__":
#     c = Car('red', 'maruti')
#     c.show()

# from collections import Counter

# l = [1, 3, 5, 1, 0, 1, 4, 6, 6, 8]

# c = Counter(l)
# print(c)

from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    def __init__(self):
        # super().__init__()
        print('I am init')
    @abstractmethod
    def draw(self):
        self
    @abstractmethod
    def set_color(self):
        self
    
class Circle(Shape):
    # def __init__(self):
    #     super().__init__()
    def draw_shape(self):
        print('draw shape')

if __name__ == '__main__':
    c  = Circle()
        
        
    