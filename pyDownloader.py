from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import urllib.request


class Downloader(QDialog):

    def __int__(self, parent):
        super.__init__(parent)

        layout = QVBoxLayout()

        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        download = QPushButton("Download")

        self.url.setPlaceholderText("Type URL Here")
        self.save_location.setPlaceholderText("File Save Location")

        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setLayout(layout)

        self.setWindowTitle("PyDownloader")
        self.setFocus()

        download.clicked(self.download)

    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()
        urllib.request.urlretrieve(url, save_location, self.report)


    def report(self, blocknum, blocksize, totalsize):
        readSoFar = blocknum * blocksize
        if totalsize > 0:
            percent = readSoFar * 100 / totalsize
            self.progress.setValue(int(percent))



app = QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()

