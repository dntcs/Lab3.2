from PyQt6.QtWidgets import QApplication
from model import Model
from view import View
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = Model()
    v = View(m)
    v.show()
    sys.exit(app.exec())