class 도형:
    원주율 = 3.14

    def 삼각형넓이(self, a, b):
        결과 = a * b / 2
        return 결과

    def 사각형넓이(self, a, b):
        결과 = a * b
        return 결과

    def 곱하기(self, a, b):
        결과 = a * b
        return 결과

    def 나누기(self, a, b):
        결과 = a / b
        return 결과


도형의넓이 = 도형()
print(도형의넓이.삼각형넓이(3, 4))
도형의넓이 = 도형()
print(도형의넓이.사각형넓이(10, 5))


첫번째수 = input("첫번째수는:")
두번째수 = input("두번째수는:")
print(f"첫번째수가 {첫번째수}이고, 두번째수가 {두번째수}이면 삼각형의 넓이는~?! {도형의넓이.삼각형넓이(int(첫번째수),int(두번째수))}")
print(f"첫번째수가 {첫번째수}이고, 두번째수가 {두번째수}이면 사각형의 넓이는~?! {도형의넓이.사각형넓이(int(첫번째수),int(두번째수))}")
