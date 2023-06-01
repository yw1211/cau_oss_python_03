import math

# Line 클래스 정의(객체 생성)
class line:
    __width = 0
    __height = 0
    # 생성자를 통해 초기 __width, __height 지정 
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    # __width, __height 에 인자로 받은 값 저장
    def set_length(self, width, height):
        self.__width = width
        self.__height = height
    # __width, __height의 값 반환 
    def get_length(self):
        return self.__width, self.__height

# 길이를 입력받아 직사각형 넓이 구하기
def area_rectangle(width, height):
    if width <= 0 or height <= 0: raise ValueError
    return width * height

# 길이를 입력받아 타원의 넓이 구하기
def area_ellipse(width, height):
    if width <= 0 or height <= 0: raise ValueError
    return width * height * math.pi

# 길이를 입력받아 직각삼각형 넓이 구하기
def area_right_triangle(width, height):
    if width <= 0 or height <= 0: raise ValueError
    return width * height / 2
