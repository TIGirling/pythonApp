from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class Downloader(QDialog):

    def __int__(self, parent):
        super.__init__(parent)

        layout = QVBoxLayout()

        url = QLineEdit()
        save_location = QLineEdit()
        progress = QProgressBar()
        download = QPushButton("Download")

        url.setPlaceholderText("Type URL Here")
        save_location.setPlaceholderText("File Save Location")

        progress.setValue(0)
        progress.setAlignment(Qt.AlignCenter)

        layout.addWidget(url)
        layout.addWidget(save_location)
        layout.addWidget(progress)
        layout.addWidget(download)

        self.setLayout(layout)

        self.setWindowTitle("PyDownloader")
        self.setFocus()

app = QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()

