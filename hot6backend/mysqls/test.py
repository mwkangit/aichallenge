class MyClass:
    global global_variable  # 전역 변수를 클래스 내부에서 사용하기 위해 선언

    def __init__(self, value):
        self.instance_variable = value  # 인스턴스 변수

    def print_values(self):
        print(f"Global Variable: {global_variable}")
        print(f"Instance Variable: {self.instance_variable}")

    def modify_global_variable(self, new_value):
        global global_variable  # 전역 변수임을 명시
        global_variable = new_value
# 전역 변수 선언
global_variable = 100

# 클래스 인스턴스 생성
obj1 = MyClass(20)
obj2 = MyClass(30)

# 각 객체에서 클래스 변수와 인스턴스 변수 출력
obj1.print_values()
obj2.print_values()

# 클래스 메서드를 통해 전역 변수 변경
obj1.modify_global_variable(200)

# 변경된 전역 변수 확인
obj1.print_values()
obj2.print_values()