from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QSpinBox, QSlider, QGridLayout
from PyQt6.QtCore import Qt

class View(QWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model
        grid = QGridLayout(self)

        self.a_label = QLabel("A")
        self.a_line = QLineEdit()
        self.a_spin = QSpinBox()
        self.a_slider = QSlider(Qt.Orientation.Horizontal)
        self.a_spin.setRange(self.model.get_min(), self.model.get_max())
        self.a_slider.setRange(self.model.get_min(), self.model.get_max())
        grid.addWidget(self.a_label, 0, 0)
        grid.addWidget(self.a_line, 1, 0)
        grid.addWidget(self.a_spin, 2, 0)
        grid.addWidget(self.a_slider, 3, 0)
        self.a_spin.valueChanged.connect(self.a_ref)
        self.a_slider.valueChanged.connect(self.a_ref)
        self.a_line.editingFinished.connect(self.a_ref_line)

        self.b_label = QLabel("B")
        self.b_line = QLineEdit()
        self.b_spin = QSpinBox()
        self.b_slider = QSlider(Qt.Orientation.Horizontal)
        self.b_spin.setRange(self.model.get_min(), self.model.get_max())
        self.b_slider.setRange(self.model.get_min(), self.model.get_max())
        grid.addWidget(self.b_label, 0, 1)
        grid.addWidget(self.b_line, 1, 1)
        grid.addWidget(self.b_spin, 2, 1)
        grid.addWidget(self.b_slider, 3, 1)
        self.b_spin.valueChanged.connect(self.b_ref)
        self.b_slider.valueChanged.connect(self.b_ref)
        self.b_line.editingFinished.connect(self.b_ref_line)

        self.c_label = QLabel("C")
        self.c_line = QLineEdit()
        self.c_spin = QSpinBox()
        self.c_slider = QSlider(Qt.Orientation.Horizontal)
        self.c_spin.setRange(self.model.get_min(), self.model.get_max())
        self.c_slider.setRange(self.model.get_min(), self.model.get_max())
        grid.addWidget(self.c_label, 0, 2)
        grid.addWidget(self.c_line, 1, 2)
        grid.addWidget(self.c_spin, 2, 2)
        grid.addWidget(self.c_slider, 3, 2)
        self.c_spin.valueChanged.connect(self.c_ref)
        self.c_slider.valueChanged.connect(self.c_ref)
        self.c_line.editingFinished.connect(self.c_ref_line)

        self.model.valuesChanged.connect(self.ref)
        self.ref()

        self.setWindowTitle("A B C")

    def ref(self):
        self.a_line.setText(str(self.model.get_a()))
        self.a_spin.setValue(self.model.get_a())
        self.a_slider.setValue(self.model.get_a())
        
        self.b_line.setText(str(self.model.get_b()))
        self.b_spin.setValue(self.model.get_b())
        self.b_slider.setValue(self.model.get_b())

        self.c_line.setText(str(self.model.get_c()))
        self.c_spin.setValue(self.model.get_c())
        self.c_slider.setValue(self.model.get_c())

    def a_ref(self, x):
        self.model.set_a(x)
        self.ref()
    def b_ref(self, x):
        self.model.set_b(x)
        self.ref()
    def c_ref(self, x):
        self.model.set_c(x)
        self.ref()

    def a_ref_line(self):
        text = self.a_line.text()
        if text.isdigit():
            self.model.set_a(int(text))
        self.ref()

    def b_ref_line(self):
        text = self.b_line.text()
        if text.isdigit():
            self.model.set_b(int(text))
        self.ref()

    def c_ref_line(self):
        text = self.c_line.text()
        if text.isdigit():
            self.model.set_c(int(text))
        self.ref()

