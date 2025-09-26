from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QHBoxLayout, QPushButton, QCheckBox, QMessageBox
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
import sys
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Learning")
        self.setGeometry(600,  350, 640, 480)
        self.setFixedSize(640, 480)
        self.setWindowIcon(QIcon("iconlearning.png"))
        self.InitColuums()
        self.initWatermelonbuttons()
        self.initcheckboxes()
        self.amount = 0
        pixmap = QPixmap("watermelon.png")
        self.label = QLabel(f"WaterMelons: {self.amount}", self)
        self.label.setFont(QFont("Arial", 30))
        self.label.setGeometry(0, 0, 640, 85)
        self.label.setStyleSheet("color: #1F1E1F;"
                            "background-color: #A9C78F;"
                            "font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter)
        label2 = QLabel(self)
        label2.setScaledContents(True)
        label2.setGeometry(-8, 12, 90, 60)
        label2.setPixmap(pixmap)
        label3 = QLabel(self)
        label3.setScaledContents(True)
        label3.setGeometry(565, 12, 90, 60)
        label3.setPixmap(pixmap)

    def initcheckboxes(self):
        self.checkbox = QCheckBox("Are you gay?", self)
        self.checkbox.setGeometry(139, 220, 114, 50)
        self.checkbox.setStyleSheet("background-color: #0000B2;"
                                    "font-weight: 500;"
                                    "color: white;"
                                    "border-radius: 5px;"
                                    "font-size: 11px;")
        self.checkbox.stateChanged.connect(self.checkbox_changed)

        self.checkbox2 = QCheckBox("Are you lgtv?", self)
        self.checkbox2.setGeometry(139, 280, 114, 50)
        self.checkbox2.setStyleSheet("background-color: #0000B2;"
                                    "font-weight: 500;"
                                    "color: white;"
                                    "border-radius: 5px;"
                                    "font-size: 11px;")
        self.checkbox2.stateChanged.connect(self.checkbox_changed2)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            time.sleep(1)
            self.show_popup("Program has crashed, Please try again later")

    def checkbox_changed2(self, state):
        if state == Qt.Checked:
            self.show_popup("If you was a TV you wouldnt be using this\n                     BOZOOOO")


    def show_popup(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error 404")
        msg.setText(message)
        msg.exec_()
        if message == "Program has crashed, Please try again later":
            self.checkbox.setChecked(False)
            while True:
                while True:
                    pass
        else:
            self.checkbox2.setChecked(False)
            sys.exit()

    def initWatermelonbuttons(self):
        WatermelonButton = QPushButton("+1 Watermelon", self)
        WatermelonButton.setGeometry(13, 160, 114, 50)
        WatermelonButton.clicked.connect(lambda: self.add_watermelon(1))
        WatermelonButton.raise_()
        WatermelonButton.setStyleSheet("background-color: #A30000;"
                                        "font-weight: 500;"
                                        "color: white;"
                                        "border-radius: 5px;")


        WatermelonButton2 = QPushButton("+10 Watermelon", self)
        WatermelonButton2.setGeometry(13, 220, 114, 50)
        WatermelonButton2.clicked.connect(lambda: self.add_watermelon(10))
        WatermelonButton2.raise_()
        WatermelonButton2.setStyleSheet("background-color: #A30000;"
                                        "font-weight: 500;"
                                        "color: white;"
                                        "border-radius: 5px;")


        WatermelonButton3 = QPushButton("+100 Watermelon", self)
        WatermelonButton3.setGeometry(13, 280, 114, 50)
        WatermelonButton3.clicked.connect(lambda: self.add_watermelon(100))
        WatermelonButton3.raise_()
        WatermelonButton3.setStyleSheet("background-color: #A30000;"
                                        "font-weight: 500;"
                                        "color: white;"
                                        "border-radius: 5px;"
                                        "font-size: 12px;")

        WatermelonButton4 = QPushButton("+1000 Watermelon", self)
        WatermelonButton4.setGeometry(13, 340, 114, 50)
        WatermelonButton4.clicked.connect(lambda: self.add_watermelon(1000))
        WatermelonButton4.raise_()
        WatermelonButton4.setStyleSheet("background-color: #A30000;"
                                        "font-weight: 500;"
                                        "color: white;"
                                        "border-radius: 5px;"
                                        "font-size: 12px;")
        
        WatermelonButton5 = QPushButton("Set to 0", self)
        WatermelonButton5.setGeometry(13, 100, 114, 50)
        WatermelonButton5.clicked.connect(lambda: self.add_watermelon(-self.amount))
        WatermelonButton5.raise_()
        WatermelonButton5.setStyleSheet("background-color: #A30000;"
                                        "font-weight: 500;"
                                        "color: white;"
                                        "border-radius: 5px;"
                                        "font-size: 12px;")
        
        WatermelonButton6 = QPushButton("x2 Watermelon", self)
        WatermelonButton6.setGeometry(13, 400, 114, 50)
        WatermelonButton6.clicked.connect(lambda: self.add_watermelon((self.amount*2) - self.amount))
        WatermelonButton6.raise_()
        WatermelonButton6.setStyleSheet("background-color: #A30000;"
                                        "font-weight: 500;"
                                        "color: white;"
                                        "border-radius: 5px;"
                                        "font-size: 12px;")

    def add_watermelon(self, Watermelons):
        self.amount += Watermelons
        self.label.setText(f"WaterMelons: {self.amount}")

    def InitColuums(self):
        centeral_widget = QWidget()
        self.setCentralWidget(centeral_widget)
        label1 = QLabel("")
        label2 = QLabel("")
        label3 = QLabel("")
        label4 = QLabel("")
        label5 = QLabel("")

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: blue;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: yellow;")
        label5.setStyleSheet("background-color: magenta;")

        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)
        hbox.addWidget(label5)

        centeral_widget.setLayout(hbox)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

