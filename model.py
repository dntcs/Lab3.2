from PyQt6.QtCore import QObject, pyqtSignal

def norm(x, l, h):
    if x<l:
        return l
    elif x>h:
        return h
    else:
        return x

class Model(QObject):
    valuesChanged = pyqtSignal()
    def __init__(self):
        super().__init__(parent=None)
        self.__a = 1
        self.__b = 2
        self.__c = 3

    def get_min(self):
        return 0
    def get_max(self):
        return 100
    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b
    def get_c(self):
        return self.__c

    def check(self, a, b, c):
        a = norm(a, self.get_min(), self.get_max())
        c = norm(c, self.get_min(), self.get_max())
        if a>c:
            a, c = c, a
        b = norm(b, a, c)
        if self.__a == a and self.__c == c and self.__b == b:
            return
        self.__a = a
        self.__b = b
        self.__c = c
        self.valuesChanged.emit()

    def set_a(self, x):
        a = norm(x, self.get_min(), self.get_max())
        b = max(self.__b, a)
        c = max(self.__c, b)
        self.check(a,b,c)
    def set_c(self, x):
        c = norm(x, self.get_min(), self.get_max())
        b = min(self.__b, c)
        a = min(self.__a, b)
        self.check(a,b,c)
    def set_b(self, x):
        b = norm(x, self.__a, self.__c)
        self.check(self.__a, b, self.__c)
        
m = Model()
m.set_a(30)
print(m.get_a(), m.get_b(), m.get_c())
m.set_b(20)
print(m.get_a(), m.get_b(), m.get_c())
m.set_c(80)
m.set_b(10)
print(m.get_a(), m.get_b(), m.get_c())
m.set_b(900)
print(m.get_a(), m.get_b(), m.get_c())