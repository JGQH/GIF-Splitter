from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog
from PIL import Image
from os import path
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GIF Splitter")
        self.setFixedSize(300, 300)
        self.setup()

    def setup(self):
        lblSearch = QLabel(self)
        lblSearch.move(10, 12)
        lblSearch.resize(60, 20)
        lblSearch.setText("Search GIF:")

        btnSearch = QPushButton(self)
        btnSearch.move(75, 10)
        btnSearch.resize(100, 25)
        btnSearch.setText("Search")

        def searchGif():
            location = QFileDialog.getOpenFileName(None, "Open GIF file", "D:\\", "GIF files (*.gif)")[0]
            if(location == ""): return

            self.raw_gif = Image.open(location)
            btnSearch.setText("[%s]" % path.basename(location))

        btnSearch.clicked.connect(searchGif)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gif_splitter = MainWindow()
    gif_splitter.showMaximized()
    sys.exit(app.exec())