from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Learning")
        self.setGeometry(600,  350, 640, 480)
        self.setWindowIcon(QIcon("iconlearning.png"))
        self.InitColuums()
        pixmap = QPixmap("watermelon.png")
        label = QLabel("WaterMelon", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 640, 85)
        label.setStyleSheet("color: #1F1E1F;"
                            "background-color: #A9C78F;"
                            "font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)
        label2 = QLabel(self)
        label2.setScaledContents(True)
        label2.setGeometry(107, 12, 90, 60)
        label2.setPixmap(pixmap)
        label3 = QLabel(self)
        label3.setScaledContents(True)
        label3.setGeometry(445, 12, 90, 60)
        label3.setPixmap(pixmap)

    def InitColuums(self):
        centeral_widget = QWidget()
        self.setCentralWidget(centeral_widget)
        label1 = QLabel("#1")
        label2 = QLabel("#2")
        label3 = QLabel("#3")
        label4 = QLabel("#4")
        label5 = QLabel("#5")

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: blue;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: yellow;")
        label5.setStyleSheet("background-color: pink;")

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

