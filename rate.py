from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QRadioButton, QTextEdit
from PyQt5.QtCore import Qt

class Rate(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('BeatHub')
        self.setGeometry(100, 100, 350, 600)  # Set the geometry of the main window

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.label_title = QLabel("BeatHub", alignment=Qt.AlignCenter)
        self.layout.addWidget(self.label_title)

        self.rate_button = QPushButton('Rate event')
        self.layout.addWidget(self.rate_button)

        self.events_label = QLabel('Local events')
        self.layout.addWidget(self.events_label)

        self.events = ['Event 1', 'Event 2', 'Event 3', 'Event 4']
        for event in self.events:
            radio_button = QRadioButton(event)
            self.layout.addWidget(radio_button)

        self.feedback_area = QTextEdit('Your feedback')
        self.layout.addWidget(self.feedback_area)

        self.central_widget.setLayout(self.layout)

if __name__ == '__main__':
    app = QApplication([])
    window = Rate()
    window.show()
    app.exec_()
