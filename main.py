import sqlite3
import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.updTable()

    def updTable(self):
        cur = self.con.cursor()
        data = cur.execute('SELECT "название сорта", "степень обжарки", "молотый/в зернах",'
                           '"описание вкуса","цена","объем упаковки (в мл)" FROM Coffees').fetchall()
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setHorizontalHeaderLabels([i[0] for i in cur.description])
        for i, row in enumerate(data):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    sys.excepthook = except_hook
    sys.exit(app.exec())
