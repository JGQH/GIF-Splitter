from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gif_splitter = MainWindow()
    gif_splitter.showMaximized()
    sys.exit(app.exec())