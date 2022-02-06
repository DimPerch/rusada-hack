from PyQt6 import QtCore


class Updater(QtCore.QObject):
    image_update = QtCore.pyqtSignal()
    button_check = QtCore.pyqtSignal()
 
    def run(self):
        while True:
            self.image_update.emit()
            self.button_check.emit()
            QtCore.QThread.msleep(100)
