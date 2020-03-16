class FourCal():
    def __init__(self, a, b):
        self.first = a
        self.second = b
    def __init__(self):
        self.first = 0
        self.second = 0
    def __del__(self):
        print("종료")
    def setdata(self,a, b):
        self.first = a
        self.second = b
    def add(self):
        return self.first + self.second
    def mul(self):
        return self.first * self.second
    def sub(self):
        return self.first - self.second
    def div(self):
        return self.first / self.second

class MoreFourCal(FourCal):
    def __init__(self, a, b):
        self.first = a
        self.second = b

    def __del__(self):
        print("종료")

    def pow(self):
        return self.first ** self.second



cal1 = FourCal()
print(cal1.add())
cal2 = MoreFourCal(2 ,10)
print(cal2.pow())
