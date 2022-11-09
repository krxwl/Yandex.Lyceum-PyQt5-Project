import sys
import webbrowser
import sqlite3

from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets


def center(self):  # функция для центрирования окна по центру
    fg = self.frameGeometry()
    display = QApplication.desktop().screenNumber(
        QApplication.desktop().cursor().pos())
    center = QApplication.desktop().screenGeometry(display).center()
    fg.moveCenter(center)
    self.move(fg.topLeft())


class PopUp(QMainWindow):  # класс всплывающего окна, которое высвечивает информацию о книге
    def __init__(self, ID, title, author, year, link):
        super().__init__()
        self.ID = ID
        self.title = title
        self.author = author
        self.year = year
        self.link = link
        self.setupUi(self)

    def setupUi(self, MainWindow):  # метод который устанавливает графический интерфейс
        MainWindow.setObjectName("MainWindow")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setScaledContents(True)
        self.label.setMinimumSize(250, 400)
        self.label.setMaximumSize(250, 400)
        self.label.setPixmap(QPixmap(f"pic/{self.title}.jpg"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft |
                                  QtCore.Qt.AlignVCenter)
        self.label_3.setText("id")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.button_clicked)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):    # метод который задает текст виджетам в окне
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", f"ID: {self.ID}"))
        self.label_2.setText(_translate("MainWindow", f"Название: {self.title}"))
        self.label_4.setText(_translate("MainWindow", f"Автор: {self.author}"))
        self.label_5.setText(_translate("MainWindow", f"Год издания: {self.year}"))
        self.pushButton.setText(_translate("MainWindow", "Открыть ссылку на книгу"))

    def button_clicked(self):   # метод, который срабатывает при нажатии на кнопку, открывает
        webbrowser.open(self.link)  # ссылку на книгу


class InputDialog(QMainWindow):    # класс диалогового окно для добавления/редактирования элементов
    def __init__(self, action):     # в базе данных
        super().__init__()
        self.setupUi()
        self.action = action
        self.show()
        if self.action == "edit" and int(ex.tableWidget_2.currentColumn()) == 0:
            con = sqlite3.connect("books_db.db")
            cur = con.cursor()
            self.ID, self.title, self.author, self.genre, self.year, self.link = cur.execute(f"""
            select * from books where id = {ex.tableWidget_2.currentItem().text()}""").fetchone()
            self.lineEdit.setText(str(self.ID))
            self.lineEdit.setEnabled(False)
            self.lineEdit_2.setText(str(self.title))
            self.lineEdit_3.setText(str(self.author))
            self.lineEdit_4.setCurrentText([i[0] for i in cur.execute(f"""select title from 
            genres where id = {self.genre}""")][0])
            self.lineEdit_5.setText(str(self.link))
            self.lineEdit_6.setText(str(self.year))
            con.close()
        elif int(ex.tableWidget_2.currentColumn()) != 0 and self.action == "edit":
            self.close()
            ex.error()

    def setupUi(self):  # метод который устанавливает графический интерфейс
        self.setObjectName("MainWindow")
        self.resize(500, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setMinimumSize(QtCore.QSize(500, 500))
        self.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        con = sqlite3.connect("books_db.db")  # введенных данных и добавляет/редактирует элемент
        cur = con.cursor()
        self.lineEdit_4 = QtWidgets.QComboBox()
        self.lineEdit_4.addItems([i[0] for i in cur.execute(f"""select title from genres""")])
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_3.addWidget(self.lineEdit_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.label_6.setText("Год")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_6.addWidget(self.lineEdit_6)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.pushButton.clicked.connect(self.pressedd)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def pressedd(self):  # метод который срабатывает при нажатии на кнопку, проверяет корректность
        con = sqlite3.connect("books_db.db")  # введенных данных и добавляет/редактирует элемент
        cur = con.cursor()
        if self.action == "new":
                    if len(self.lineEdit.text()) >= 1 and int(self.lineEdit.text()) not in [i[0] for i in
                                                     cur.execute(f"""select id from books""")]:
                        print([i[0] for i in cur.execute(f"select id from genres where title = "
                                                            f"'{self.lineEdit_4.currentText()}'")][0])
                        cur.execute(f"""INSERT INTO books
                                VALUES ({int(self.lineEdit.text())}, 
                                '{self.lineEdit_2.text()}', '{self.lineEdit_3.text()}', 
                                {[i[0] for i in cur.execute(f"select id from genres where title = "
                                                            f"'{self.lineEdit_4.currentText()}'")][0]},
                                {int(self.lineEdit_6.text())}, '{self.lineEdit_5.text()}')""")
                    elif len(self.lineEdit.text()) >= 1 and int(self.lineEdit.text()) in [i[0] for i in
                                                     cur.execute(f"""select id from books""")]:
                        QMessageBox.critical(self, "Ошибка",
                                                 "ID должен быть уникальным у каждой книги",
                                                 buttons=QMessageBox.Ignore)
                    else:
                        cur.execute(f"""INSERT INTO books
                                                        VALUES ({max([i[0] for i in
                                                     cur.execute("select id from books")]) + 1}, 
                                            '{self.lineEdit_2.text()}', '{self.lineEdit_3.text()}', 
                                            {[i[0] for i in cur.execute(f"select id from genres where title = "
                                                            f"'{self.lineEdit_4.currentText()}'")][0]},
                                            {int(self.lineEdit_6.text())}, 
                                            '{self.lineEdit_5.text()}')""")
                    con.commit()
                    self.close()
        else:

            con.execute(f"""UPDATE books
                        SET title = '{self.lineEdit_2.text()}', author = '{self.lineEdit_3.text()}',
                        genre = {[i[0] for i in cur.execute(f"select id from genres where title = "
                                                        f"'{self.lineEdit_4.currentText()}'")][0]}, 
                                                        year = {int(self.lineEdit_6.text())},
                        link = '{self.lineEdit_5.text()}'
                        WHERE id = {self.ID}""")
            con.commit()
        ex.rerun_database()
        con.close()
        self.close()

    def retranslateUi(self):    # метод который устанавливает текст для виджетов
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Заполните Информацию о книге"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "Название"))
        self.label_3.setText(_translate("MainWindow", "Автор"))
        self.label_4.setText(_translate("MainWindow", "ID уже существующего жанра"))
        self.label_5.setText(_translate("MainWindow", "Ссылка (если есть)"))
        self.pushButton.setText(_translate("MainWindow", "OK"))


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):  # метод для установки графического интерфейса
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 1000))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setMinimumSize(QtCore.QSize(40, 40))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel { color :#3FC1C9; }")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pythonbook_1 = QtWidgets.QLabel(self.tab)
        self.pythonbook_1.setMinimumSize(QtCore.QSize(140, 210))
        self.pythonbook_1.setMaximumSize(QtCore.QSize(140, 210))
        self.pythonbook_1.setText("")
        self.pythonbook_1.setPixmap(QtGui.QPixmap("pic/Python. Полное руководство.jpg"))
        self.pythonbook_1.setScaledContents(True)
        self.pythonbook_1.setObjectName("pythonbook_1")
        self.horizontalLayout_8.addWidget(self.pythonbook_1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.d2 = list()
        self.horizontalLayout_8.addItem(spacerItem)
        self.pythonbook_2 = QtWidgets.QLabel(self.tab)
        self.pythonbook_2.setMinimumSize(QtCore.QSize(140, 210))
        self.pythonbook_2.setMaximumSize(QtCore.QSize(140, 210))
        self.pythonbook_2.setText("")
        self.pythonbook_2.setPixmap(
            QtGui.QPixmap("pic/Python создаем программы и игры, 3-е издание.jpg"))
        self.pythonbook_2.setScaledContents(True)
        self.pythonbook_2.setObjectName("pythonbook_2")
        self.horizontalLayout_8.addWidget(self.pythonbook_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.pythonbook_3 = QtWidgets.QLabel(self.tab)
        self.pythonbook_3.setMinimumSize(QtCore.QSize(140, 210))
        self.pythonbook_3.setMaximumSize(QtCore.QSize(140, 210))
        self.pythonbook_3.setText("")
        self.pythonbook_3.setPixmap(
            QtGui.QPixmap("pic/Алгоритмы Data Science и их практическая реализация на Python.jpg"))
        self.pythonbook_3.setScaledContents(True)
        self.pythonbook_3.setObjectName("pythonbook_3")
        self.horizontalLayout_8.addWidget(self.pythonbook_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.pythonbook_4 = QtWidgets.QLabel(self.tab)
        self.pythonbook_4.setMinimumSize(QtCore.QSize(140, 210))
        self.pythonbook_4.setMaximumSize(QtCore.QSize(140, 210))
        self.pythonbook_4.setText("")
        self.pythonbook_4.setPixmap(QtGui.QPixmap("pic/Python. К вершинам мастерства.jpg"))
        self.pythonbook_4.setScaledContents(True)
        self.pythonbook_4.setObjectName("label_16")
        self.horizontalLayout_8.addWidget(self.pythonbook_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.pythonbook_5 = QtWidgets.QLabel(self.tab)
        self.pythonbook_5.setMinimumSize(QtCore.QSize(140, 210))
        self.pythonbook_5.setMaximumSize(QtCore.QSize(140, 210))
        self.pythonbook_5.setText("")
        self.pythonbook_5.setPixmap(
            QtGui.QPixmap("pic/Стандартная библиотека Python 3. Справочник с примерами.jpg"))
        self.pythonbook_5.setScaledContents(True)
        self.pythonbook_5.setObjectName("pythonbook_5")
        self.horizontalLayout_8.addWidget(self.pythonbook_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.pythonbook_6 = QtWidgets.QLabel(self.tab)
        self.pythonbook_6.setMinimumSize(QtCore.QSize(140, 210))
        self.pythonbook_6.setMaximumSize(QtCore.QSize(140, 210))
        self.pythonbook_6.setText("")
        self.pythonbook_6.setPixmap(
            QtGui.QPixmap("pic/Классические задачи Computer Science на языке Python.jpg"))
        self.pythonbook_6.setScaledContents(True)
        self.pythonbook_6.setObjectName("pythonbook_6")
        self.horizontalLayout_8.addWidget(self.pythonbook_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel { color :#3FC1C9; }")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.javabook_1 = QtWidgets.QLabel(self.tab)
        self.javabook_1.setMinimumSize(QtCore.QSize(140, 210))
        self.javabook_1.setMaximumSize(QtCore.QSize(140, 210))
        self.javabook_1.setText("Предметно-ориентированное проектирование в Enterprise Java")
        self.javabook_1.setPixmap(
            QtGui.QPixmap("pic/Предметно-ориентированное проектирование в Enterprise Java.jpg"))
        self.javabook_1.setScaledContents(True)
        self.javabook_1.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.javabook_1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.javabook_2 = QtWidgets.QLabel(self.tab)
        self.javabook_2.setMinimumSize(QtCore.QSize(140, 210))
        self.javabook_2.setMaximumSize(QtCore.QSize(140, 210))
        self.javabook_2.setText("")
        self.javabook_2.setPixmap(QtGui.QPixmap("pic/Grokking The Java Developer Interview.jpg"))
        self.javabook_2.setScaledContents(True)
        self.javabook_2.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.javabook_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.javabook_3 = QtWidgets.QLabel(self.tab)
        self.javabook_3.setMinimumSize(QtCore.QSize(140, 210))
        self.javabook_3.setMaximumSize(QtCore.QSize(140, 210))
        self.javabook_3.setText("")
        self.javabook_3.setPixmap(
            QtGui.QPixmap("pic/Java Cookbook - Problems and Solutions for Java Developers.jpg"))
        self.javabook_3.setScaledContents(True)
        self.javabook_3.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.javabook_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.javabook_4 = QtWidgets.QLabel(self.tab)
        self.javabook_4.setMinimumSize(QtCore.QSize(140, 210))
        self.javabook_4.setMaximumSize(QtCore.QSize(140, 210))
        self.javabook_4.setText("")
        self.javabook_4.setPixmap(
            QtGui.QPixmap("pic/Data Visualization with Python and JavaScript.jpg"))
        self.javabook_4.setScaledContents(True)
        self.javabook_4.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.javabook_4)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.javabook_5 = QtWidgets.QLabel(self.tab)
        self.javabook_5.setMinimumSize(QtCore.QSize(140, 210))
        self.javabook_5.setMaximumSize(QtCore.QSize(140, 210))
        self.javabook_5.setText("")
        self.javabook_5.setPixmap(
            QtGui.QPixmap("pic/Learn Kubernetes Docker .NET Core Java Node.JS PHP or Python.jpg"))
        self.javabook_5.setScaledContents(True)
        self.javabook_5.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.javabook_5)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.javabook_6 = QtWidgets.QLabel(self.tab)
        self.javabook_6.setMinimumSize(QtCore.QSize(140, 210))
        self.javabook_6.setMaximumSize(QtCore.QSize(140, 210))
        self.javabook_6.setText("")
        self.javabook_6.setPixmap(QtGui.QPixmap("pic/Java 17 Recipes.jpg"))
        self.javabook_6.setScaledContents(True)
        self.javabook_6.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.javabook_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel { color :#3FC1C9; }")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.devopsbook_1 = QtWidgets.QLabel(self.tab)
        self.devopsbook_1.setMinimumSize(QtCore.QSize(140, 210))
        self.devopsbook_1.setMaximumSize(QtCore.QSize(140, 210))
        self.devopsbook_1.setBaseSize(QtCore.QSize(100, 140))
        self.devopsbook_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.devopsbook_1.setStyleSheet("QLabel {float: left;}")
        self.devopsbook_1.setText("")
        self.devopsbook_1.setPixmap(QtGui.QPixmap("pic/Руководство по DevOps.jpg"))
        self.devopsbook_1.setScaledContents(True)
        self.devopsbook_1.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.devopsbook_1.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.devopsbook_1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.devopsbook_2 = QtWidgets.QLabel(self.tab)
        self.devopsbook_2.setMinimumSize(QtCore.QSize(140, 210))
        self.devopsbook_2.setMaximumSize(QtCore.QSize(140, 210))
        self.devopsbook_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.devopsbook_2.setStyleSheet("QLabel {float: left;}")
        self.devopsbook_2.setText("500")
        self.devopsbook_2.setPixmap(QtGui.QPixmap("pic/Lean DevOps.jpg"))
        self.devopsbook_2.setScaledContents(True)
        self.devopsbook_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.devopsbook_2.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.devopsbook_2)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.devopsbook_3 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.devopsbook_3.sizePolicy().hasHeightForWidth())
        self.devopsbook_3.setSizePolicy(sizePolicy)
        self.devopsbook_3.setMinimumSize(QtCore.QSize(140, 210))
        self.devopsbook_3.setMaximumSize(QtCore.QSize(140, 210))
        self.devopsbook_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.devopsbook_3.setStyleSheet("QLabel{float: left;}")
        self.devopsbook_3.setText("")
        self.devopsbook_3.setPixmap(QtGui.QPixmap("pic/Practical Security for Agile and DevOps.jpg"))
        self.devopsbook_3.setScaledContents(True)
        self.devopsbook_3.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.devopsbook_3.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.devopsbook_3)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.pass1 = QtWidgets.QLabel(self.tab)
        self.pass1.setMinimumSize(QtCore.QSize(140, 210))
        self.pass1.setMaximumSize(QtCore.QSize(140, 210))
        self.pass1.setText("")
        self.pass1.setObjectName("pass1")
        self.horizontalLayout_6.addWidget(self.pass1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.pass2 = QtWidgets.QLabel(self.tab)
        self.pass2.setMinimumSize(QtCore.QSize(140, 210))
        self.pass2.setMaximumSize(QtCore.QSize(140, 210))
        self.pass2.setText("")
        self.pass2.setObjectName("pass2")
        self.horizontalLayout_6.addWidget(self.pass2)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem14)
        self.pass3 = QtWidgets.QLabel(self.tab)
        self.pass3.setMinimumSize(QtCore.QSize(140, 210))
        self.pass3.setMaximumSize(QtCore.QSize(140, 210))
        self.pass3.setText("")
        self.pass3.setObjectName("pass3")
        self.horizontalLayout_6.addWidget(self.pass3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_2.addWidget(self.label_20)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setObjectName("comboBox_2")
        con = sqlite3.connect('books_db.db')
        cur = con.cursor()
        self.tablewithgenres = dict(zip([i[0] for i in cur.execute("""SELECT id from genres""")
                                        .fetchall()], [i[0] for i in cur.execute("""SELECT 
                                                title from genres""").fetchall()]))

        self.elements = cur.execute("""SELECT * FROM books ORDER BY id""").fetchall()
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        spacerItem16 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed,
                                             QtWidgets.QSizePolicy.Minimum)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setText("Узнать информацию")
        self.horizontalLayout_9.addWidget(self.pushButton_5)
        self.horizontalLayout_9.addItem(spacerItem16)
        self.horizontalLayout_9.addWidget(self.pushButton_4)
        spacerItem15 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed,
                                             QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem15)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_9.addWidget(self.pushButton_3)
        spacerItem16 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed,
                                             QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem16)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_9.addWidget(self.pushButton_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.comboBox_2.addItems(['Выберите сортировку', "По ID", "По названию", "По автору",
                                  "По году"])
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setHorizontalHeaderItem(0, QTableWidgetItem('ID'))
        self.tableWidget_2.setHorizontalHeaderItem(1, QTableWidgetItem('Название'))
        self.tableWidget_2.setHorizontalHeaderItem(2, QTableWidgetItem('Автор'))
        self.tableWidget_2.setHorizontalHeaderItem(3, QTableWidgetItem('Жанр'))
        self.tableWidget_2.setHorizontalHeaderItem(4, QTableWidgetItem('Год'))
        self.tableWidget_2.setHorizontalHeaderItem(5, QTableWidgetItem('Ссылка'))
        for i, row in enumerate(self.elements):
            self.tableWidget_2.setRowCount(
                self.tableWidget_2.rowCount() + 1)
            self.tableWidget_2.setItem(
                i, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget_2.setItem(i, 1, QTableWidgetItem(row[1]))
            self.tableWidget_2.setItem(i, 2, QTableWidgetItem(row[2]))
            self.tableWidget_2.setItem(i, 3, QTableWidgetItem(self.tablewithgenres[row[3]]))
            self.tableWidget_2.setItem(i, 4, QTableWidgetItem(str(row[4])))
            self.tableWidget_2.setItem(i, 5, QTableWidgetItem(row[5]))

        self.verticalLayout_7.addWidget(self.tableWidget_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        self.gridLayout_3.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_19.setObjectName("label_19")
        self.horizontalLayout.addWidget(self.label_19)
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(['Выберите сортировку', "По алфавиту", "По ID"])
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed,
                                             QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem17)
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem18 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Fixed,
                                             QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem18)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('ID'))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Жанр'))
        self.tableWidget.setRowCount(0)

        for i, row in enumerate(self.tablewithgenres):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            self.tableWidget.setItem(
                i, 0, QTableWidgetItem(str(row)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(self.tablewithgenres[row]))

        self.tableWidget.resizeColumnsToContents()
        self.gridLayout_4.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        center(self)  # вызов метода для центрирования окна по центру
        self.dialogs = list()
        self.buttons = {self.pythonbook_1: "Python. Полное руководство",
                        self.pythonbook_2: "Python создаем программы и игры, 3-е издание",
                        self.pythonbook_3: "Алгоритмы Data Science и их практическая реализация "
                                           "на Python",
                        self.pythonbook_4: "Python. К вершинам мастерства",
                        self.pythonbook_5: "Стандартная библиотека Python 3. Справочник с примерами",
                        self.pythonbook_6: "Классические задачи Computer Science на языке Python",
                        self.javabook_1: "Предметно-ориентированное проектирование в "
                                         "Enterprise Java",
                        self.javabook_2: "Grokking The Java Developer Interview",
                        self.javabook_3: "Java Cookbook - Problems and Solutions for Java "
                                         "Developers",
                        self.javabook_4: "Data Visualization with Python and JavaScript",
                        self.javabook_5: "Learn Kubernetes Docker .NET Core Java Node.JS PHP or "
                                         "Python",
                        self.javabook_6: "Java 17 Recipes",
                        self.devopsbook_1: "Руководство по DevOps",
                        self.devopsbook_2: "Lean DevOps",
                        self.devopsbook_3: "Practical Security for Agile and DevOps"}

        for i in self.buttons.keys():  # делаем QLabel кликабельными
            i.mouseReleaseEvent = lambda e, btn=i: self.pic_clicked(e, sender=btn)
            i.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        self.comboBox.currentTextChanged.connect(self.sortirovka)
        self.comboBox_2.currentTextChanged.connect(self.sortirovka2)
        self.pushButton.clicked.connect(self.opentxt)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_5.clicked.connect(self.get_info)
        self.pushButton_2.clicked.connect(self.delete)
        self.pushButton_4.clicked.connect(self.edit_element)
        self.pushButton_3.clicked.connect(self.new_element)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):    # метод для установки текста виджетов в окне
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Библиотека программиста"))
        self.label_3.setText(_translate("MainWindow", "> Книги по Python"))
        self.label_2.setText(_translate("MainWindow", "> Книги по Java"))
        self.label.setText(_translate("MainWindow", "> Руководства DevOps"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  _translate("MainWindow", "Главная"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  _translate("MainWindow", "Библиотека"))
        self.label_20.setText(_translate("MainWindow", "Сортировка"))
        self.pushButton_4.setText(_translate("MainWindow", "Редактировать элемент"))
        self.pushButton_3.setText(_translate("MainWindow", "Добавить элемент"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить элемент"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  _translate("MainWindow", "Библиотека"))
        self.label_19.setText(_translate("MainWindow", "Сортировка"))
        self.pushButton.setText(_translate("MainWindow", "Получить список жанров в txt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),
                                  _translate("MainWindow", "Жанры"))

    def open_book(self, ID, title, author, year, link):     # метод, который открывает новое окно с
        dialog = PopUp(ID, title, author, year, link)   # информацией о книге
        self.dialogs.append(dialog)
        dialog.resize(700, 700)
        center(dialog)
        dialog.setWindowTitle("Информация о книге")
        dialog.show()

    def rerun_database(self):   # метод который обновляет данные в таблице с книгами
        con = sqlite3.connect("books_db.db")
        cur = con.cursor()
        self.tableWidget_2.setRowCount(0)
        self.elements = cur.execute("""SELECT * FROM books ORDER BY id""").fetchall()
        for i, row in enumerate(self.elements):
            self.tableWidget_2.setRowCount(
                self.tableWidget_2.rowCount() + 1)
            self.tableWidget_2.setItem(
                i, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget_2.setItem(i, 1, QTableWidgetItem(row[1]))
            self.tableWidget_2.setItem(i, 2, QTableWidgetItem(row[2]))
            self.tableWidget_2.setItem(i, 3, QTableWidgetItem(self.tablewithgenres[row[3]]))
            self.tableWidget_2.setItem(i, 4, QTableWidgetItem(str(row[4])))
            self.tableWidget_2.setItem(i, 5, QTableWidgetItem(row[5]))

    def pic_clicked(self, event, sender=None):  # метод который открывает окно с информацией о книге
        name = self.buttons[sender]     # при нажатии на картинку
        con = sqlite3.connect("books_db.db")
        cur = con.cursor()
        result = cur.execute(f"""SELECT * FROM books WHERE title = '{name}'""").fetchall()
        self.open_book(result[0][0], self.buttons[sender], result[0][2], result[0][4], result[0][5])
        con.close()

    def sortirovka(self):   # сортировка для таблицы жанров
        if self.comboBox.currentText() == "Выберите сортировку" or self.comboBox.currentText() == \
                "По ID":
            newtable = self.tablewithgenres
        elif self.comboBox.currentText() == "По алфавиту":
            newtable = dict(sorted(self.tablewithgenres.items(), key=lambda x: x[1]))
        for i, row in enumerate(newtable.keys()):
            self.tableWidget.setItem(
                i, 0, QTableWidgetItem(str(row)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(newtable[row]))

    def sortirovka2(self):      # сортировка для таблицы книг
        if self.comboBox_2.currentText() == "Выберите сортировку" or self.comboBox_2.currentText() \
                == "По ID":
            self.elements.sort(key=lambda x: x[0])
        elif self.comboBox_2.currentText() == "По названию":
            self.elements.sort(key=lambda x: x[1])
        elif self.comboBox_2.currentText() == "По автору":
            self.elements.sort(key=lambda x: x[2])
        elif self.comboBox_2.currentText() == "По году":
            self.elements.sort(key=lambda x: x[4])
        elif self.comboBox_2.currentText() == "По жанру":
            self.elements.sort(key=lambda x: x[4])
        for i, row in enumerate(self.elements):
            self.tableWidget_2.setItem(
                i, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget_2.setItem(i, 1, QTableWidgetItem(row[1]))
            self.tableWidget_2.setItem(i, 2, QTableWidgetItem(row[2]))
            self.tableWidget_2.setItem(i, 3, QTableWidgetItem(self.tablewithgenres[row[3]]))
            self.tableWidget_2.setItem(i, 4, QTableWidgetItem(str(row[4])))
            self.tableWidget_2.setItem(i, 5, QTableWidgetItem(row[5]))

    def opentxt(self):      # метод для открытия txt файла с жанрами
        webbrowser.open("genres.txt")

    def error(self):    # метод для получения диалогового окна с ошибкой
        button = QMessageBox.critical(self, "Ошибка", "Упс, Вы выбрали другую колонку, выберите"
                                                      " элемент из колонки ID, а "
                                                      " затем нажмите кнопку",
                                      buttons=QMessageBox.Ignore)

    def get_info(self):     # метод для получия информации о книге из базы данных
        con = sqlite3.connect("books_db.db")
        cur = con.cursor()
        if int(self.tableWidget_2.currentColumn()) == 0:
            result = cur.execute(f"""SELECT id, title, author, year, link FROM books WHERE id = 
            {self.tableWidget_2.currentItem().text()}""").fetchone()
            self.open_book(*result)
        else:
            self.error()

    def delete(self):   # метод для удаления элемента из базы данных
        con = sqlite3.connect("books_db.db")
        cur = con.cursor()
        if int(self.tableWidget_2.currentColumn()) == 0:
            result = cur.execute(f"""DELETE FROM books WHERE id = {self.tableWidget_2.currentItem()
                                 .text()}""")
            con.commit()
            con.close()
            self.rerun_database()
        else:
            self.error()

    def new_element(self):  # метод для создания нового элемента
        okno = InputDialog('new')
        okno.show()
        self.d2.append(okno)

    def edit_element(self):   # метод для редактирования существующего элемента
        okno = InputDialog('edit')
        self.d2.append(okno)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.exit(app.exec())
