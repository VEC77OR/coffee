import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView
from PyQt5.QtCore import Qt
import sys


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        l = ['Название', 'Степень обжарки', 'Молотый/в зёрнах', 'Вкус',
                  'Цена', 'Объём упаковки']

        self.setGeometry(800, 450, 600, 300)
        self.setFixedSize(600, 300)
        self.setWindowTitle('Types of coffee')

        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        r = (cur.execute("""SELECT * FROM info""")).fetchall()
        con.commit()
        con.close()

        self.table = QTableWidget(self)
        self.table.resize(600, 600)
        self.table.move(0, 0)
        self.table.setColumnCount(6)

        self.table.setHorizontalHeaderLabels([l[0], l[1], l[2], l[3],
                                             l[4], l[5]])

        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)

        self.table.setRowCount(len(r))

        for i in range(len(r)):
            self.table.setItem(i, 0, QTableWidgetItem(str(r[i][1])))
            self.table.setItem(i, 1, QTableWidgetItem(str(r[i][2])))
            self.table.setItem(i, 2, QTableWidgetItem(str(r[i][3])))
            self.table.setItem(i, 3, QTableWidgetItem(str(r[i][4])))
            self.table.setItem(i, 4, QTableWidgetItem(str(r[i][5])))
            self.table.setItem(i, 5, QTableWidgetItem(str(r[i][6])))

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.table.resizeColumnsToContents()

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        self.show()


app = QApplication(sys.argv)
ex = Main()
ex.show()
sys.exit(app.exec_())
