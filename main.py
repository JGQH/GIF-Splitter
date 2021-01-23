from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QPlainTextEdit
from PIL import Image, ImageDraw
from os import path
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GIF Splitter")
        self.setFixedSize(200, 200)
        self.setup()
        self.lastDir = "D:\\"

    def setup(self):
        lblSearch = QLabel(self)
        lblSearch.move(10, 12)
        lblSearch.resize(60, 20)
        lblSearch.setText("Search GIF:")

        btnSearch = QPushButton(self)
        btnSearch.move(90, 10)
        btnSearch.resize(100, 25)
        btnSearch.setText("Search")

        lblPreview = QLabel(self)
        lblPreview.move(10, 40)
        lblPreview.setText("GIF Data:")
        lblPreview.adjustSize()

        qptPreview = QPlainTextEdit(self)
        qptPreview.move(10, 60)
        qptPreview.resize(180, 95)

        btnSplit = QPushButton(self)
        btnSplit.move(50, 165)
        btnSplit.resize(100, 25)
        btnSplit.setText("Get Spritesheet")
        btnSplit.setEnabled(False)

        def searchGif():
            location = QFileDialog.getOpenFileName(None, "Open GIF file", self.lastDir, "GIF files (*.gif)")[0]
            if(location == ""): return

            self.lastDir = path.dirname(location)
            btnSearch.setText("[%s]" % path.basename(location))
            qptPreview.setPlainText(self.processGif(location))
            btnSplit.setEnabled(True)
        btnSearch.clicked.connect(searchGif)

        def splitGif():
            location = QFileDialog.getSaveFileName(None, "Save Spritesheet", path.join(self.lastDir, "Sprite_From_GIF"), "PNG file (*.png)")[0]
            if(location == ""): return

            output = Image.new('RGBA', (self.final_width, self.height), (0, 0, 0, 0))
            for i in range(len(self.frames)):
                frame = self.frames[i]
                output.paste(frame, (i * self.width, 0))
            output.save(location)
        btnSplit.clicked.connect(splitGif)

    def processGif(self, location:str)->str:
        raw_gif = Image.open(location)
        frames = []
    
        try:
            while True:
                raw_gif.seek(raw_gif.tell() + 1)

                frame = Image.new('RGBA', raw_gif.size, (0, 0, 0, 0))
                frame.paste(raw_gif)
                frames.append(frame)
        except:
            pass
        
        self.frames = frames
        self.width, self.height = raw_gif.size
        self.final_width = self.width * len(frames)
        return "-Total Frames: {frames}\n-Frame Size: {frame_width}x{frame_height}\n-Spritesheet size:{total_width}x{frame_height}".format(
            frames=len(frames),
            frame_width=self.width,
            frame_height=self.height,
            total_width=self.final_width
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gif_splitter = MainWindow()
    gif_splitter.showMaximized()
    sys.exit(app.exec())