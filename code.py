# pip install PyQt5

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
import os

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("imgviewer.ui", self)

        default_file = "default.png"
        self.current_file = default_file
        self.setWindowTitle(default_file)
        
        self.show()

        pixmap = QtGui.QPixmap(self.current_file)
        pixmap = pixmap.scaled(self.width(), self.height())
        #pixmap = pixmap.scaled(self.width())
        
        self.label.setPixmap(pixmap)
        self.label.setMinimumSize(1,1)
        self.file_list = None
        self.file_counter = None
        self.actionOpen_Image.triggered.connect(self.open_image)
        self.actionOpen_Directory.triggered.connect(self.open_directory)
        self.actionNext_Image.triggered.connect(self.previous_image)
        self.actionPrevious_Image.triggered.connect(self.next_image)
        
    def resizeEvent(self, event):
        try:
            pixmap = QtGui.QPixmap(self.current_file)
        except:
            pixmap = QtGui.QPixmap("default.png")
        pixmap = pixmap.scaled(self.width(), self.height())
        #pixmap = pixmap.scaled(self.width())
        self.label.setPixmap(pixmap)
        self.label.resize(self.width(), self.height())

    def open_image(self):
        options = QFileDialog.Options()
        # filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Image Files (*.png, *.jpg, *.jpeg)", options = options)
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Image Files (*.*)", options = options)
        if filename != "":
            self.current_file = filename
            pixmap = QtGui.QPixmap(self.current_file)
            pixmap = pixmap.scaled(self.width(), self.height())
            #pixmap = pixmap.scaled(self.width())
            self.label.setPixmap(pixmap)
            self.setWindowTitle(os.path.basename(self.current_file))

    def open_directory(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.file_list=[directory+"/"+ f for f in os.listdir(directory) if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg")]
        self.file_counter = 0
        self.current_file = self.file_list[self.file_counter]
        pixmap = QtGui.QPixmap(self.current_file)
        pixmap = pixmap.scaled(self.width(), self.height())
        #pixmap = pixmap.scaled(self.width())
        self.label.setPixmap(pixmap)
        self.setWindowTitle(os.path.basename(self.current_file))

    def next_image(self):
        if self.file_counter is not None:
            self.file_counter += 1
            self.file_counter %= len(self.file_list)
            self.current_file = self.file_list[self.file_counter]
            pixmap = QtGui.QPixmap(self.current_file)
            pixmap = pixmap.scaled(self.width(), self.height())
            #pixmap = pixmap.scaled(self.width())
            self.label.setPixmap(pixmap)
            self.setWindowTitle(os.path.basename(self.current_file))
            

    def previous_image(self):
        if self.file_counter is not None:
            self.file_counter -= 1
            self.file_counter %= len(self.file_list)
            self.current_file = self.file_list[self.file_counter]
            pixmap = QtGui.QPixmap(self.current_file)
            pixmap = pixmap.scaled(self.width(), self.height())
            #pixmap = pixmap.scaled(self.width())
            self.label.setPixmap(pixmap)
            self.setWindowTitle(os.path.basename(self.current_file))

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == "__main__":
    main()