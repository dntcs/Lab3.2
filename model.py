from PyQt6.QtCore import QObject, pyqtSignal

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

m = Model()
print(m.get_a(), m.get_b(), m.get_c())