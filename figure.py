import math

# Line 클래스 정의(객체 생성)
class line:
    __length = 0
    # 생성자를 통해 초기 __length 값 지정 
    def __init__(self, length=0):
        self.__length = length
    # __length에 인자로 받은 값 저장
    def set_length(self, length):
        self.__length = length
    # __length의 값 반환 
    def get_length(self):
        return self.__length

# length를 매개 변수로 받아 정사각형의 넓이를 반환하는 함수
def area_square(length):
    return length ** 2

# length를 매개변수로 받아 원의 넓이를 반환하는 함수
def area_circle(length):
    return length ** 2 * math.pi

# length를 매개변수로 받아 정삼각형의 넓이를 반환하는 ㅎㅁ수
def area_regular_triangle(length):
    return math.sqrt(3) / 4 * length ** 2
