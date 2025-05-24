import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from Planeti_Ui import Ui_MainWindow


class PlanetInfoApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Данные о планетах
        self.planet_data = {
            "Венера": {
                "Ves": "4.87 × 10²⁴ кг",
                "radius": "6052 км",
                "Plotnost": "5.24 г/см³",
                "IMG": "venera.png"
            },
            "Меркурий": {
                "Ves": "3.33 × 10²³ кг",
                "radius": "2440 км",
                "Plotnost": "5.43 г/см³",
                "IMG": "mercury.png"
            },
            "Марс": {
                "Ves": "6.42 × 10²³ кг",
                "radius": "3390 км",
                "Plotnost": "3.93 г/см³",
                "IMG": "mars.png"
            },
            "Юпитер": {
                "Ves": "1.90 × 10²⁷ кг",
                "radius": "69911 км",
                "Plotnost": "1.33 г/см³",
                "IMG": "jupiter.png"
            }
        }
        self.comboBox.addItems(self.planet_data.keys())
        self.comboBox.currentTextChanged.connect(self.update_info)
        self.update_info()

    def update_info(self):
        planet = self.comboBox.currentText()
        data = self.planet_data.get(planet, {})
        self.label_6.setText(data.get("Ves", "Нет данных"))
        self.label_7.setText(data.get("radius", "Нет данных"))
        self.label_8.setText(data.get("Plotnost", "Нет данных"))
        IMG_path = data.get("IMG", "")
        if IMG_path:
            try:
                pixmap = QPixmap(IMG_path)
                self.label_9.setPixmap(pixmap.scaled(
                    130, 130,
                    QtCore.Qt.KeepAspectRatio,
                    QtCore.Qt.SmoothTransformation
                ))
            except:
                self.label_9.setText("Ошибка загрузки")
        else:
            self.label_9.setText("Нет изображения")


app = QtWidgets.QApplication(sys.argv)
window = PlanetInfoApp()
window.setWindowTitle("Планеты Солнечной системы")
window.show()
sys.exit(app.exec_())