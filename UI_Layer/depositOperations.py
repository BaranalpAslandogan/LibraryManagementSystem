# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'depositOperations.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from BL_Layer.depositOpLogic import *
from UI_Layer import depositAddPage


class Ui_depositDialog(object):
    def setupUi(self, depositDialog):
        depositDialog.setObjectName("depositDialog")
        depositDialog.resize(579, 651)
        depositDialog.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.groupBox = QtWidgets.QGroupBox(depositDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 561, 631))
        self.groupBox.setStyleSheet("color: rgb(190, 190, 190);\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 19, 561, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(14, 0, 14, 6)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.depositSearchLayout = QtWidgets.QHBoxLayout()
        self.depositSearchLayout.setObjectName("depositSearchLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.depositSearchLayout.addWidget(self.label)
        self.depositSearchEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.depositSearchEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(42, 42, 42);")
        self.depositSearchEdit.setObjectName("depositSearchEdit")
        self.depositSearchLayout.addWidget(self.depositSearchEdit)
        self.depositSearchButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.depositSearchButton.setStyleSheet("background-color: rgb(152, 152, 152);\n"
                                               "color: rgb(53, 53, 53);")
        self.depositSearchButton.setObjectName("depositSearchButton")
        self.depositSearchLayout.addWidget(self.depositSearchButton)
        self.depositRefreshButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.depositRefreshButton.setStyleSheet("background-color: rgb(152, 152, 152);\n"
                                                "color: rgb(53, 53, 53);")
        self.depositRefreshButton.setObjectName("depositRefreshButton")
        self.depositSearchLayout.addWidget(self.depositRefreshButton)
        self.verticalLayout_2.addLayout(self.depositSearchLayout)

        try:
            self.depositTableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
            self.depositTableWidget.setStyleSheet("background-color: rgb(230, 230, 230);\n"
    "color: rgb(62, 62, 62);")
            self.depositTableWidget.setObjectName("depositTableWidget")
            self.depositTableWidget.setColumnCount(4)
            self.depositTableWidget.rowCount()
            self.depositTableWidget.setShowGrid(True)
            self.depositTableWidget.setHorizontalHeaderLabels(['Emanet Kitap Adı','Emanet Edilen Kullanıcı', 'Emanet Tarihi','Teslim Tarihi'])
            self.depositTableWidget.verticalHeader().sectionClicked.connect(self.getTableLabels)
        except:
            print("Table ekleme hatası:",sys.exc_info())

        self.verticalLayout_2.addWidget(self.depositTableWidget)
        self.depositButtonsLayout = QtWidgets.QHBoxLayout()
        self.depositButtonsLayout.setObjectName("depositButtonsLayout")
        self.expiredDepositShowButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.expiredDepositShowButton.setStyleSheet("background-color: rgb(152, 152, 152);\n"
                                                    "color: rgb(53, 53, 53);")
        self.expiredDepositShowButton.setObjectName("expiredDepositShowButton")
        self.depositButtonsLayout.addWidget(self.expiredDepositShowButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.depositButtonsLayout.addItem(spacerItem)
        self.depositAddButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.depositAddButton.setObjectName("depositAddButton")
        self.depositAddButton.setStyleSheet("background-color: rgb(152, 152, 152);\n"
                                                   "color: rgb(53, 53, 53);")
        self.depositButtonsLayout.addWidget(self.depositAddButton)
        self.depositUpdateTimeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.depositUpdateTimeButton.setObjectName("depositUpdateTimeButton")
        self.depositUpdateTimeButton.setStyleSheet("background-color: rgb(152, 152, 152);\n"
                                                "color: rgb(53, 53, 53);")
        self.depositButtonsLayout.addWidget(self.depositUpdateTimeButton)
        self.depositDeleteButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.depositDeleteButton.setObjectName("depositDeleteButton")
        self.depositDeleteButton.setStyleSheet("background-color: rgb(152, 152, 152);\n"
                                            "color: rgb(53, 53, 53);")
        self.depositButtonsLayout.addWidget(self.depositDeleteButton)
        self.verticalLayout_2.addLayout(self.depositButtonsLayout)

        self.depositAddButton.clicked.connect(self.getDepositAddPage)
        self.expiredDepositShowButton.clicked.connect(self.getExpiredDeposits)
        self.depositRefreshButton.clicked.connect(self.getDeposits)
        self.depositDeleteButton.clicked.connect(self.deleteItemFromDeposit)
        self.depositSearchButton.clicked.connect(self.getSearchDeposit)
        self.depositUpdateTimeButton.clicked.connect(self.addExtraTime)
        self.getDeposits()

        self.userNameText = ""
        self.bookNameText = ""
        self.dateTimeText = ""
        self.expireDateText = ""

        self.retranslateUi(depositDialog)
        QtCore.QMetaObject.connectSlotsByName(depositDialog)

    def addExtraTime(self):
        try:
            connect = DepositOpLogic(self.depositTableWidget,self.bookNameText,
                                     self.userNameText,self.dateTimeText, self.expireDateText,
                                     self.depositSearchEdit.text())
            connect.extraTime()
        except:
            print("deleteItemFromDeposit hatası:", sys.exc_info())


    def getSearchDeposit(self):
        try:
            connect = DepositOpLogic(self.depositTableWidget,self.bookNameText,
                                     self.userNameText,self.dateTimeText, self.expireDateText,
                                     self.depositSearchEdit.text())
            connect.searchDeposit()
        except:
            print("deleteItemFromDeposit hatası:", sys.exc_info())

    def deleteItemFromDeposit(self):
        try:
            connect = DepositOpLogic(self.depositTableWidget,self.bookNameText,
                                     self.userNameText,self.dateTimeText, self.expireDateText,
                                     self.depositSearchEdit.text())
            connect.deleteDeposit()
        except:
            print("deleteItemFromDeposit hatası:", sys.exc_info())

    def getDeposits(self):
        try:
            connect = DepositOpLogic(self.depositTableWidget,self.bookNameText,
                                     self.userNameText,self.dateTimeText, self.expireDateText,
                                     self.depositSearchEdit.text())
            connect.updateAllDepositList()
        except:
            print("getDeposits hatası:", sys.exc_info())

    def getExpiredDeposits(self):
        try:
            connect = DepositOpLogic(self.depositTableWidget,self.bookNameText,
                                     self.userNameText,self.dateTimeText, self.expireDateText,
                                     self.depositSearchEdit.text())
            connect.expiredDepositFilter()
        except:
            print("getDeposits hatası:", sys.exc_info())


    def getTableLabels(self, row):
        try:
            book = self.depositTableWidget.item(row, 0)
            user = self.depositTableWidget.item(row, 1)
            date = self.depositTableWidget.item(row, 2)
            day = self.depositTableWidget.item(row, 3)

            self.bookNameText = book.text()
            self.userNameText = user.text()
            self.dateTimeText = date.text()
            self.expireDateText = day.text()

        except:
            print("Hata:", sys.exc_info())

    def getDepositAddPage(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = depositAddPage.Ui_depositAdd()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def retranslateUi(self, depositDialog):
        _translate = QtCore.QCoreApplication.translate
        depositDialog.setWindowTitle(_translate("depositDialog", "Dialog"))
        self.groupBox.setTitle(_translate("depositDialog", "Emanet İşlemleri"))
        self.label.setText(_translate("depositDialog", "Emanet Kitap İsmi:"))
        self.depositSearchButton.setText(_translate("depositDialog", "Ara"))
        self.depositRefreshButton.setText(_translate("depositDialog", "Yenile"))
        self.depositAddButton.setText(_translate("depositDialog", "Emanet Ekle"))
        self.depositUpdateTimeButton.setText(_translate("depositDialog", "Süre Uzat"))
        self.expiredDepositShowButton.setText(_translate("depositDialog", "Süresi Geçen Emanetler"))
        self.depositDeleteButton.setText(_translate("depositDialog", "Sil"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bookDialog = QtWidgets.QDialog()
    ui = Ui_depositDialog()
    ui.setupUi(bookDialog)
    bookDialog.show()
    sys.exit(app.exec_())
