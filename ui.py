
import os
import subprocess
from PyQt5 import QtCore, QtWidgets
import data
from uiTest import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, data_obj, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.data_obj = data_obj
        # print(self.data_obj.display_dict)

    def setupUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.series_text_field = QtWidgets.QLineEdit(self.centralwidget)
        self.series_text_field.setObjectName("series_text_field")
        self.series_text_field.setText(data_obj.path)
        self.horizontalLayout.addWidget(self.series_text_field)

        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setObjectName("search_button")
        self.search_button.clicked.connect(lambda: self.query_text(self.series_text_field.text()))
        self.horizontalLayout.addWidget(self.search_button)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 985, 706))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")


        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setSpacing(5)

        # Adding the buttons in gridLayout_2

        self.addButtons()

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 2, 0, 1, 1)

        # self.change()

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        for b in self.buttons:
            b.installEventFilter(self)
            # print(b)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Series Tracker"))
        self.label.setText(_translate("MainWindow", "Enter Series Name:"))
        self.search_button.setText(_translate("MainWindow", "Search"))

    def addButtons(self):
        lst = self.data_obj.display_dict.keys()
        self.buttons = list()
        i = 1
        j = 0
        for item in lst:
            self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
            self.pushButton.setSizePolicy(sizePolicy)
            self.pushButton.setText(item)
            self.pushButton.setMinimumWidth(200)
            self.pushButton.setMinimumHeight(150)

            self.pushButton.setObjectName(item)
            self.gridLayout_2.addWidget(self.pushButton, i, j, 1, 1)
            j = (j + 1) % 3
            if j == 0: i += 1
            self.buttons.append(self.pushButton)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                print(obj.objectName(), "Left click")
                self.actionLeft(obj)

            elif event.button() == QtCore.Qt.RightButton:
                print(obj.objectName(), "Right click")
                self.actionRight(obj)

            elif event.button() == QtCore.Qt.MiddleButton:
                print(obj.objectName(), "Middle click")
        return QtCore.QObject.event(obj, event)

    # @pyqtSlot()
    def actionLeft(self, obj):
        # print(self.sender().text())
        print(self.data_obj.display_dict[obj.text()][0])
        os.startfile(self.data_obj.display_dict[obj.text()][0])

    def actionRight(self, obj):
        subprocess.Popen(r'explorer /select, ' + self.data_obj.display_dict[obj.text()][0])

    def query_text(self, var):
        if not os.path.exists(var): self.invalid_path_alert()

        with open('search.txt', 'w') as fp:
            fp.write(var)

        # Clear the gridlayout_2 (all the buttons)
        for i in reversed(range(self.gridLayout_2.count())):
            self.gridLayout_2.itemAt(i).widget().setParent(None)

        # Again read the values from data.py
        data_obj.path = var
        data_obj.read()

        # Update new Buttons
        self.addButtons()
        self.scrollArea.update()
        self.scrollArea.repaint()

    def invalid_path_alert(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Path No Found")
        msg.setText("Your entered path doesn't exists!")
        x = msg.exec()

    def remove_buttons(self):
        for b in self.buttons:
            self.gridLayout_2.removeItem(b)


import sys

if __name__ == "__main__":
    with open('search.txt') as fp:
        query = fp.read()
    data_obj = data.Read(query)

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow(data_obj)
    w.show()
    sys.exit(app.exec_())
