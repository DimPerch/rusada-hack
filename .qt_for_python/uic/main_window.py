# Form implementation generated from reading ui file 'c:\Users\Dimitry\My projects\rusada-hack\UI\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 260)
        MainWindow.setMinimumSize(QtCore.QSize(480, 260))
        MainWindow.setMaximumSize(QtCore.QSize(480, 260))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(10, 10, 150, 150))
        self.run_button.setObjectName("run_button")
        self.settings_buuton = QtWidgets.QPushButton(self.centralwidget)
        self.settings_buuton.setGeometry(QtCore.QRect(10, 170, 150, 30))
        self.settings_buuton.setObjectName("settings_buuton")
        self.about_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_button.setGeometry(QtCore.QRect(10, 210, 150, 30))
        self.about_button.setObjectName("about_button")
        self.info = QtWidgets.QTextBrowser(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(170, 170, 301, 70))
        self.info.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.info.setObjectName("info")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(320, 10, 150, 150))
        self.image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.image.setObjectName("image")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.run_button.setText(_translate("MainWindow", "Запустить"))
        self.settings_buuton.setText(_translate("MainWindow", "Калибровать"))
        self.about_button.setText(_translate("MainWindow", "О программе"))
        self.image.setText(_translate("MainWindow", "Изображение\n"
"появится\n"
"после\n"
"калибровки"))
