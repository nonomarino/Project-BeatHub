from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QMainWindow, QSizePolicy)
from PyQt5.QtGui import QIcon, QPixmap

class BaseWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(500, 800)
        self.setWindowTitle("BeatHub")
        self.setWindowIcon(QIcon("images/logo_win.png"))
        self.initUI()

    def initUI(self):
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Add blue header image at the top
        self.add_top_image()

    def add_top_image(self):
        header_label = QLabel(self)
        pixmap = QPixmap('images/logo_screen.png')  # Add the correct path to your image
        # Scale the pixmap to fit the width of the window
        header_label.setPixmap(pixmap.scaled(self.width(), 150, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        header_label.setAlignment(Qt.AlignTop)
        header_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        header_label.setFixedHeight(150)

        self.main_layout.addWidget(header_label, alignment=Qt.AlignTop)

    def addContent(self, layout):
        self.main_layout.addLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = BaseWindow()
    window.show()
    app.exec_()
