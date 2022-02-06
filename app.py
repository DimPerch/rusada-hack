import pyautogui
from datetime import date
from PIL import ImageDraw
from PIL.ImageQt import ImageQt
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QFontDatabase, QIcon, QPixmap

from screens import main_window
from thread import Updater


class App(QtWidgets.QMainWindow):
    """
    The main class of app
    """
    def __init__(self):
        super(App, self).__init__()

        # load stylesheet
        file = QtCore.QFile("resourses/style.qss")
        file.open(QtCore.QIODeviceBase.OpenModeFlag.ReadOnly | QtCore.QIODeviceBase.OpenModeFlag.Text)
        stream = QtCore.QTextStream(file)
        self.setStyleSheet(stream.readAll())

        # load font
        font = QFontDatabase.addApplicationFont('resourses/RobotoSlab-Regular.ttf')
        if font == -1:
            print("ERROR: failed to connect font")

        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("RUSADA-hack")
        self.setWindowIcon(QIcon('resourses/icon.ico'))

        self.run = False
        self.set = False
        self.size = 20
        self.pos = None

        # loading buutons
        self.ui.run_button.clicked.connect(self.start_and_stop)
        self.ui.settings_buuton.pressed.connect(self.settings)
        self.ui.about_button.clicked.connect(self.about)
        self.ui.settings_buuton.installEventFilter(self)

        self.thread_connect()
       

    @QtCore.pyqtSlot()
    def set_image(self):
        if self.pos:
            x, y = self.pos
            rect = (x - self.size, y - self.size, self.size * 2, self.size * 2)
            PIL_image = pyautogui.screenshot(region=rect).resize((150, 150))

            # add cross
            draw = ImageDraw.Draw(PIL_image)
            draw.line((64, 75, 74, 75), fill='black', width=1)
            draw.line((76, 75, 86, 75), fill='black', width=1)
            draw.line((75, 64, 75, 74), fill='black', width=1)
            draw.line((75, 76, 75, 86), fill='black', width=1)

            Qt_image = ImageQt(PIL_image)
            image = QPixmap.fromImage(Qt_image)
            self.ui.image.setPixmap(image)


    @QtCore.pyqtSlot()
    def check_pixel(self):
        if self.run and not self.set:
            is_click = False
            r, g, b = pyautogui.pixel(*self.pos)
            if (r, g, b) == (0, 0, 0):
                is_click = True
            
            if is_click:
                pyautogui.click(x=self.pos[0], y=self.pos[1])
                self.ui.info.append("Стрелка была нажата")
                pyautogui.moveRel(-100, 100, duration=0.25)

        
    def thread_connect(self):
        # создадим поток
        self.thread = QtCore.QThread()
        # создадим объект для выполнения кода в другом потоке
        self.updater = Updater()
        # перенесём объект в другой поток
        self.updater.moveToThread(self.thread)
        # после чего подключим все сигналы и слоты
        self.updater.image_update.connect(self.set_image)
        self.updater.button_check.connect(self.check_pixel)
        # подключим сигнал старта потока к методу run у объекта, который должен выполнять код в другом потоке
        self.thread.started.connect(self.updater.run)
        # запустим поток
        self.thread.start()


    def start_and_stop(self):
        """
        Run button's handler
        """
        if self.pos:
            states = {False: ("Запустить", "Программа была запущена!"), True: ("Остановить", "Программа была остановлена!")}
            self.ui.info.append(states[self.run][1])
            self.run = not self.run
            self.ui.run_button.setText(states[self.run][0])
            self.ui.settings_buuton.setEnabled(not self.run)
            self.ui.about_button.setEnabled(not self.run)
        else:
            self.ui.info.append("Точка не установлена!")


    def settings(self):
        """
        Settings button's handler
        """
        if not self.run:
            states = {False: "Калибровать", True: "Калибровка..."}
            self.set = not self.set
            self.ui.run_button.setEnabled(not self.set)
            self.ui.settings_buuton.setText(states[self.set])
            self.ui.about_button.setEnabled(not self.set)


    def about(self):
        """
        About button's handler
        """
        with open("resourses/about.txt", "r", encoding="UTF-8") as f:
            text = f.read()
        self.about_info = QtWidgets.QMessageBox().information(self, "О программе", text.format(date.today().year))


    def eventFilter(self, source, event):
        """
        Set press point
        """
        if self.set and not self.run:
            if event.type() == QtCore.QEvent.Type.MouseMove:
                x, y = pyautogui.position()
                self.pos = (x, y)
            elif event.type() == QtCore.QEvent.Type.MouseButtonRelease:
                self.settings()
                self.ui.info.append(f"Точка установлена {self.pos}")
 
        return QtWidgets.QMainWindow.eventFilter(self, source, event)
