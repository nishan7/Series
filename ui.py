# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
# from PySide2.QtCore import Slot
from PyQt5.QtCore import pyqtSlot

import data
import os
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, data_obj):
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
        self.horizontalLayout.addWidget(self.series_text_field)

        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setObjectName("search_button")
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

#####Adding the buttons
        files_names = data_obj.display_dict.keys()
        self.addButtons(files_names)

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
        #
        # for b in self.buttons:
        #     # b.clicked.connect(lambda : self.action(b.text()))
        #     print(b)
        i=0
        for b in self.buttons:
            self.buttons[i].clicked.connect(lambda: self.action(i))
            i+=1



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Series Tracker"))
        self.label.setText(_translate("MainWindow", "Enter Series Name:"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        # self.pushButton.setText(_translate("MainWindow", "PushButton1"))
        # self.pushButton2.setText(_translate("MainWindow", "PushButton2"))
        # self.pushButton3.setText(_translate("MainWindow", "PushButton3"))

    def addButtons(self, lst):
        # lst = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10', 'b11', 'b12', 'b13', 'b14', 'b15', 'b16',
        #        'b17', 'b18']
        print(lst);
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
            # self.pushButton.clicked.connect(lambda: self.action(i+j))


    # @pyqtSlot()
    def action(self,var):
        print(var)
        print()

    def action2(self, var):
        print(var+" 2")


if __name__ == "__main__":
    import sys
    with open('search.txt') as fp:
        query = fp.read()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    data_obj=data.Read(query)


    ui.setupUi(MainWindow,data_obj)
    MainWindow.show()
    sys.exit(app.exec_())
