from app import App
from PyQt6 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = App()
    application.show()

    result = app.exec()
    if result:
        print("ERROR: program was crushed!")
