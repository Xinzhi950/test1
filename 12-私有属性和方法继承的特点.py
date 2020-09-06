# 私有属性和方法不能继承
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 100

    def __bar(self):
        print('我是父类的方法' + self.name)

    def test(self):
        print(f'余额{self.__money}')
        self.__bar()


class Student(Person):
    def demo(self):
        print('姓名' + self.name)
        # print(f'有{self.__money}元钱')
        # self.__bar()


s = Student('张三', 18)
s.demo()
