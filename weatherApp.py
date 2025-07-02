from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
import sys
import requests
import time

class MainWindow(QMainWindow):
    def __init__(self, apikey):
        super().__init__()
        self.apikey = apikey
        self.setWindowTitle("Weather App")
        self.setGeometry(600,  350, 420, 580)
        self.setFixedSize(420, 580)
        self.initInputBox()
        self.initbuttons()
        self.label = QLabel("Enter City Name: ", self)
        font = QFont("Arial", 20)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setGeometry(0, 10, 420, 70)
        self.label.setStyleSheet("color: #1F1E1F;"
                            "font-weight: italic;")
        self.label.setAlignment(Qt.AlignCenter)

        self.label2 = QLabel("", self)
        font = QFont("Arial", 55)
        font.setBold(True)
        font.setItalic(False)
        self.label2.setFont(font)
        self.label2.setGeometry(0, 190, 420, 100)
        self.label2.setAlignment(Qt.AlignCenter)

        self.label3 = QLabel("", self)
        font = QFont("Arial", 25)
        font.setBold(False)
        font.setItalic(False)
        self.label3.setFont(font)
        self.label3.setGeometry(0, 500, 420, 100)
        self.label3.setAlignment(Qt.AlignCenter)

        self.label4 = QLabel("", self)
        font = QFont("Segoe UI Emoji", 105)
        font.setBold(False)
        font.setItalic(False)
        self.label4.setFont(font)
        self.label4.setGeometry(0, 280, 420, 230)
        self.label4.setAlignment(Qt.AlignCenter)

    def Get_weather(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.apikey}&units=imperial"
        try:
            response = requests.get(url)
            if response.status_code == 401:
                print("Invalid API key.")
                self.label2.setText("Invalid API key.")
                time.sleep(2)
                sys.exit()
            elif response.status_code == 404:
                print("Invalid city.")
                font = QFont("Arial", 45)
                font.setBold(False)
                font.setItalic(False)
                self.label2.setFont(font)
                self.label2.setText("Invalid city.")
                self.label3.setText("")
                self.label4.setText("")
            else:
                font = QFont("Arial", 50)
                font.setBold(True)
                font.setItalic(False)
                self.label2.setFont(font)
                data = response.json()
                weather = data['weather'][0]['description']
                temp = data['main']['temp']
                self.label2.setText(f"{temp} ℉")
                self.label3.setText(f"{weather}")
                if "thunder" in weather:
                    self.label4.setText("🌩️")
                elif "cloud" in weather:
                    self.label4.setText("☁️")
                elif "rain" in weather:
                    self.label4.setText("🌧️")
                elif "drizzle" in weather:
                    self.label4.setText("🌦️")
                elif "snow" in weather:
                    self.label4.setText("❄️")
                elif "clear" in weather:
                    self.label4.setText("☀️")
                elif "atmosphere" in weather:
                    self.label4.setText("🌫️")
        except Exception as e:
            print("Error:", e)

    def initbuttons(self):
        self.button = QPushButton("Get Weather", self)
        self.button.setGeometry(20, 140, 380, 45)
        self.button.setStyleSheet("""
                                    QPushButton {
                                        border: 1px solid black;
                                        background-color: white;
                                    }
                                    QPushButton:hover {
                                        background-color: #e0e0e0;
                                    }
                                    """)
        font = QFont("Arial", 14)
        font.setBold(True)
        self.button.setFont(font)
        self.button.clicked.connect(lambda: self.Get_weather(self.input.text().capitalize().strip()))

    def initInputBox(self):
            self.input = QLineEdit(self)
            self.input.setGeometry(20, 70, 380, 60)
            self.input.setStyleSheet("border: 1px solid black;")
            self.input.setPlaceholderText("")
            font = QFont("Arial", 20)
            self.input.setFont(font)
            self.input.setAlignment(Qt.AlignCenter)

def main(apikey):
    app = QApplication(sys.argv)
    window = MainWindow(apikey)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    apikey = input("Api key:").strip()
    main(apikey)
