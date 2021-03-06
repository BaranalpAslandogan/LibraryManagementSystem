# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userOperations.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from BL_Layer.userOpLogic import UserOpLogic
from Data_Layer.user import User
from UI_Layer import userUpdatePage


class Ui_userDialog(object):
    def setupUi(self, userDialog):
        userDialog.setObjectName("userDialog")
        userDialog.resize(890, 387)
        userDialog.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.groupBox = QtWidgets.QGroupBox(userDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 871, 371))
        self.groupBox.setStyleSheet("\n"
                                    "color: rgb(200, 200, 200);")
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 471, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.userNameEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.userNameEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(42, 42, 42);")
        self.userNameEdit.setText("")
        self.userNameEdit.setObjectName("userNameEdit")
        self.gridLayout.addWidget(self.userNameEdit, 1, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.userPhoneEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.userPhoneEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "color: rgb(42, 42, 42);")
        self.userPhoneEdit.setText("")
        self.userPhoneEdit.setObjectName("userPhoneEdit")
        self.gridLayout.addWidget(self.userPhoneEdit, 2, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.idBox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.idBox.setEnabled(True)
        self.idBox.setStyleSheet("background-color: rgb(200, 200, 200);\n"
                                 "color: rgb(90, 90, 90);")
        self.idBox.setReadOnly(True)
        self.idBox.setObjectName("idBox")
        self.gridLayout.addWidget(self.idBox, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        # add table widget
        self.userTableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.userTableWidget.setColumnCount(3)
        self.userTableWidget.setGeometry(QtCore.QRect(490, 50, 371, 311))
        self.userTableWidget.setStyleSheet("\n""background-color: rgb(215, 215, 215);\n""color: rgb(103, 103, 103);")
        self.userTableWidget.setShowGrid(True)
        # userTableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.userTableWidget.setObjectName("userTableWidget")

        self.userTableWidget.rowCount()
        # set table header
        self.userTableWidget.setHorizontalHeaderLabels(['Kullanıcı ID', 'İsim-Soyisim', 'Telefon Numarası'])
        try:
            self.userTableWidget.verticalHeader().sectionClicked.connect(self.getTableLabels)
        except:
            print("Hata:", sys.exc_info())

        self.userAddButton = QtWidgets.QPushButton(self.groupBox)
        self.userAddButton.setGeometry(QtCore.QRect(10, 310, 151, 23))
        self.userAddButton.setStyleSheet("background-color: rgb(152, 152, 152);\n"
                                         "color: rgb(53, 53, 53);")
        self.userAddButton.setObjectName("userAddButton")
        self.userUpdateButton = QtWidgets.QPushButton(self.groupBox)
        self.userUpdateButton.setGeometry(QtCore.QRect(170, 310, 151, 23))
        self.userUpdateButton.setStyleSheet("background-color: rgb(152, 152, 152);\n"
                                            "color: rgb(53, 53, 53);")
        self.userUpdateButton.setObjectName("userUpdateButton")

        self.userDeleteButton = QtWidgets.QPushButton(self.groupBox)
        self.userDeleteButton.setGeometry(QtCore.QRect(330, 310, 151, 23))
        self.userDeleteButton.setStyleSheet("background-color: rgb(152, 152, 152);\n"
                                            "color: rgb(53, 53, 53);")
        self.userDeleteButton.setObjectName("userDeleteButton")

        self.userSearchButton = QtWidgets.QPushButton(self.groupBox)
        self.userSearchButton.setGeometry(QtCore.QRect(708, 20, 71, 21))
        self.userSearchButton.setStyleSheet("background-color: rgb(152, 152, 152);\n"
                                            "color: rgb(53, 53, 53);")
        self.userSearchButton.setObjectName("userSearchButton")

        self.listUpdateButton = QtWidgets.QPushButton(self.groupBox)
        self.listUpdateButton.setGeometry(QtCore.QRect(782, 20, 79, 21))
        self.listUpdateButton.setStyleSheet("background-color: rgb(152, 152, 152);\n"
                                            "color: rgb(53, 53, 53);")
        self.listUpdateButton.setObjectName("listUpdateButton")

        self.userSearchEdit = QtWidgets.QLineEdit(self.groupBox)
        self.userSearchEdit.setGeometry(QtCore.QRect(540, 20, 160, 21))
        self.userSearchEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "color: rgb(42, 42, 42);")
        self.userSearchEdit.setObjectName("userSearchEdit")

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(490, 20, 41, 21))
        self.label_4.setObjectName("label_4")

        try:
            self.userAddButton.clicked.connect(self.connectUserOp)
            self.userUpdateButton.clicked.connect(self.getUserUpdatePage)
            self.userDeleteButton.clicked.connect(self.connectDeleteUser)
            self.userSearchButton.clicked.connect(self.connectSearchUser)
            self.userUpdateButton.clicked.connect(self.getUserUpdatePage)
            self.listUpdateButton.clicked.connect(self.refreshTable)
        except:
            print("Hata:", sys.exc_info())

        self.retranslateUi(userDialog)
        QtCore.QMetaObject.connectSlotsByName(userDialog)


    def getTableLabels(self,row):
        try:
            idItem = self.userTableWidget.item(row, 0)
            self.idBox.setText(idItem.text())
            nameItem = self.userTableWidget.item(row, 1)
            self.userNameEdit.setText(nameItem.text())
            phoneItem = self.userTableWidget.item(row, 2)
            self.userPhoneEdit.setText(phoneItem.text())
            allItems = [idItem.text(), nameItem.text(), phoneItem.text()]
            print(allItems)
        except:
            print("Hata:", sys.exc_info())

    def refreshTable(self):
        try:
            connection = UserOpLogic(self.userNameEdit.text(), self.userPhoneEdit.text(), self.userTableWidget,
                                      self.idBox.text(), self.userSearchEdit.text())
            connection.refreshConnect()
        except:
            print("refresh table metodunda hata:", sys.exc_info())

    def connectUserOp(self):
        try:
            connectUser = UserOpLogic(self.userNameEdit.text(), self.userPhoneEdit.text(), self.userTableWidget,
                                      self.idBox.text(), self.userSearchEdit.text())
            connectUser.addUser()

        except:
            print("Hata:", sys.exc_info())

    def connectSearchUser(self):
        try:
            connectUser = UserOpLogic(self.userNameEdit.text(), self.userPhoneEdit.text(), self.userTableWidget,
                                      self.idBox.text(),self.userSearchEdit.text())
            connectUser.searchUser()

        except:
            print("Hata:", sys.exc_info())

    def connectDeleteUser(self):
        try:
            connectUser = UserOpLogic(self.userNameEdit.text(), self.userPhoneEdit.text(), self.userTableWidget,
                                      self.idBox.text(),self.userSearchEdit.text())
            connectUser.deleteUser()
        except:
            print("Hata:", sys.exc_info())

    def getUserUpdatePage(self):
        try:
            connectUser = UserOpLogic(self.userNameEdit.text(), self.userPhoneEdit.text(), self.userTableWidget,
                                      self.idBox.text(),self.userSearchEdit.text())
            connectUser.updateUser()
        except:
            print("Hata:", sys.exc_info())

    def retranslateUi(self, userDialog):
        _translate = QtCore.QCoreApplication.translate
        userDialog.setWindowTitle(_translate("userDialog", "Dialog"))
        self.groupBox.setTitle(_translate("userDialog", "Kullanıcı İşlemleri"))
        self.label.setText(_translate("userDialog", "Telefon Numarası:"))
        self.label_2.setText(_translate("userDialog", "Adı-Soyadı:"))
        self.label_3.setText(_translate("userDialog", "Kullanıcı ID:"))
        self.label_4.setText(_translate("userDialog", "İsim Ara:"))
        self.userAddButton.setText(_translate("userDialog", "Ekle"))
        self.userUpdateButton.setText(_translate("userDialog", "Güncelle"))
        self.userDeleteButton.setText(_translate("userDialog", "Sil"))
        self.userSearchButton.setText(_translate("userDialog", "Ara"))
        self.listUpdateButton.setText(_translate("userDialog", "Liste Yenile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    userDialog = QtWidgets.QDialog()
    ui = Ui_userDialog()
    ui.setupUi(userDialog)
    userDialog.show()
    sys.exit(app.exec_())