# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookOperations.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from BL_Layer.bookOpLogic import BookOpLogic


class Ui_bookDialog(object):
    def setupUi(self, bookDialog):
        bookDialog.setObjectName("bookDialog")
        bookDialog.resize(1137, 389)
        bookDialog.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.groupBox = QtWidgets.QGroupBox(bookDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1121, 371))
        self.groupBox.setStyleSheet("\n"
"color: rgb(200, 200, 200);")
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 471, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.bookNameEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.bookNameEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(42, 42, 42);")
        self.bookNameEdit.setText("")
        self.bookNameEdit.setObjectName("bookNameEdit")
        self.gridLayout.addWidget(self.bookNameEdit, 1, 1, 1, 2)
        self.bookTypeBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.bookTypeBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(50, 50, 50);")
        self.bookTypeBox.setObjectName("bookTypeBox")
        self.bookTypeBox.addItem("")
        self.bookTypeBox.addItem("")
        self.bookTypeBox.addItem("")
        self.bookTypeBox.addItem("")
        self.bookTypeBox.addItem("")
        self.bookTypeBox.addItem("")
        self.bookTypeBox.addItem("")
        self.bookTypeBox.addItem("")
        self.gridLayout.addWidget(self.bookTypeBox, 2, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.bookAuthorNameEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.bookAuthorNameEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(42, 42, 42);")
        self.bookAuthorNameEdit.setText("")
        self.bookAuthorNameEdit.setObjectName("bookAuthorNameEdit")
        self.gridLayout.addWidget(self.bookAuthorNameEdit, 4, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.bookArrivalDateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.bookArrivalDateEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(50, 50, 50);")
        self.bookArrivalDateEdit.setObjectName("bookArrivalDateEdit")
        self.gridLayout.addWidget(self.bookArrivalDateEdit, 6, 1, 1, 2)
        self.bookPublisherEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.bookPublisherEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(42, 42, 42);")
        self.bookPublisherEdit.setText("")
        self.bookPublisherEdit.setObjectName("bookPublisherEdit")
        self.gridLayout.addWidget(self.bookPublisherEdit, 5, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.bookIDLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.bookIDLine.setStyleSheet("background-color: rgb(215, 215, 215);\n"
"color: rgb(92, 92, 92);")
        self.bookIDLine.setObjectName("bookIDLine")
        self.bookIDLine.setReadOnly(True)
        self.gridLayout.addWidget(self.bookIDLine, 0, 1, 1, 1)

        # add table widget
        self.bookTableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.bookTableWidget.setColumnCount(6)
        self.bookTableWidget.setGeometry(QtCore.QRect(490, 50, 621, 311))
        self.bookTableWidget.setStyleSheet("\n""background-color: rgb(215, 215, 215);\n""color: rgb(103, 103, 103);")
        self.bookTableWidget.setShowGrid(True)
        # userTableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.bookTableWidget.setObjectName("userTableWidget")

        self.bookTableWidget.rowCount()
        # set table header
        self.bookTableWidget.setHorizontalHeaderLabels(['Kitap ID', 'Kitap Adı', 'Kitap Türü', 'Yazar', 'Yayın Evi', 'Geliş Tarihi'])
        try:
            self.bookTableWidget.verticalHeader().sectionClicked.connect(self.getTableLabels)
        except:
            print("Hata:", sys.exc_info())

        self.bookAddButton = QtWidgets.QPushButton(self.groupBox)
        self.bookAddButton.setGeometry(QtCore.QRect(10, 310, 151, 23))
        self.bookAddButton.setStyleSheet("background-color: rgb(152, 152, 152);\n"
"color: rgb(53, 53, 53);")
        self.bookAddButton.setObjectName("bookAddButton")
        self.bookUpdateButton = QtWidgets.QPushButton(self.groupBox)
        self.bookUpdateButton.setGeometry(QtCore.QRect(170, 310, 151, 23))
        self.bookUpdateButton.setStyleSheet("background-color: rgb(152, 152, 152);\n"
"color: rgb(53, 53, 53);")
        self.bookUpdateButton.setObjectName("bookUpdateButton")
        self.bookDeleteButton = QtWidgets.QPushButton(self.groupBox)
        self.bookDeleteButton.setGeometry(QtCore.QRect(330, 310, 151, 23))
        self.bookDeleteButton.setStyleSheet("background-color: rgb(152, 152, 152);\n"
"color: rgb(53, 53, 53);")
        self.bookDeleteButton.setObjectName("bookDeleteButton")
        self.bookSearchButton = QtWidgets.QPushButton(self.groupBox)
        self.bookSearchButton.setGeometry(QtCore.QRect(910, 20, 81, 21))
        self.bookSearchButton.setStyleSheet("background-color: rgb(152, 152, 152);\n"
"color: rgb(53, 53, 53);")
        self.bookSearchButton.setObjectName("bookSearchButton")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(500, 20, 101, 21))
        self.label_7.setObjectName("label_7")
        self.bookSearchEdit = QtWidgets.QLineEdit(self.groupBox)
        self.bookSearchEdit.setGeometry(QtCore.QRect(610, 20, 291, 20))
        self.bookSearchEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(42, 42, 42);")
        self.bookSearchEdit.setObjectName("bookSearchEdit")
        self.bookListUpdateButton = QtWidgets.QPushButton(self.groupBox)
        self.bookListUpdateButton.setGeometry(QtCore.QRect(1000, 20, 81, 21))
        self.bookListUpdateButton.setStyleSheet("background-color: rgb(152, 152, 152);\n"
"color: rgb(53, 53, 53);")
        self.bookListUpdateButton.setObjectName("bookListUpdateButton")

        try:
            self.bookAddButton.clicked.connect(self.connectUserOp)
            self.bookUpdateButton.clicked.connect(self.getUserUpdatePage)
            self.bookDeleteButton.clicked.connect(self.connectDeleteUser)
            self.bookSearchButton.clicked.connect(self.connectSearchUser)
            self.bookUpdateButton.clicked.connect(self.getUserUpdatePage)
            self.bookListUpdateButton.clicked.connect(self.refreshTable)
        except:
            print("Hata:", sys.exc_info())

        self.retranslateUi(bookDialog)
        QtCore.QMetaObject.connectSlotsByName(bookDialog)

    def refreshTable(self):
        try:
            connection = BookOpLogic(self.bookIDLine.text(), self.bookNameEdit.text(),
                                     self.bookTypeBox.currentText(), self.bookAuthorNameEdit.text(),
                                     self.bookPublisherEdit.text(), self.bookArrivalDateEdit.text(),
                                     self.bookTableWidget, self.bookSearchEdit.text())
            connection.refreshConnect()
        except:
            print("refresh table metodunda hata:", sys.exc_info())

    def connectUserOp(self):
        try:
            connectBook = BookOpLogic(self.bookIDLine.text(), self.bookNameEdit.text(),
                                     self.bookTypeBox.currentText(), self.bookAuthorNameEdit.text(),
                                     self.bookPublisherEdit.text(), self.bookArrivalDateEdit.text(),
                                     self.bookTableWidget, self.bookSearchEdit.text())
            connectBook.addBook()

        except:
            print("Hata:", sys.exc_info())

    def connectSearchUser(self):
        try:
            connectBook = BookOpLogic(self.bookIDLine.text(), self.bookNameEdit.text(),
                                      self.bookTypeBox.currentText(), self.bookAuthorNameEdit.text(),
                                      self.bookPublisherEdit.text(), self.bookArrivalDateEdit.text(),
                                      self.bookTableWidget, self.bookSearchEdit.text())
            connectBook.searchBook()

        except:
            print("Hata:", sys.exc_info())

    def connectDeleteUser(self):
        try:
            connectBook = BookOpLogic(self.bookIDLine.text(), self.bookNameEdit.text(),
                                      self.bookTypeBox.currentText(), self.bookAuthorNameEdit.text(),
                                      self.bookPublisherEdit.text(), self.bookArrivalDateEdit.text(),
                                      self.bookTableWidget, self.bookSearchEdit.text())
            connectBook.deleteBook()
        except:
            print("Hata:", sys.exc_info())

    def getUserUpdatePage(self):
        try:
            connectBook = BookOpLogic(self.bookIDLine.text(), self.bookNameEdit.text(),
                                      self.bookTypeBox.currentText(), self.bookAuthorNameEdit.text(),
                                      self.bookPublisherEdit.text(), self.bookArrivalDateEdit.text(),
                                      self.bookTableWidget, self.bookSearchEdit.text())
            connectBook.updateBook()
        except:
            print("Hata:", sys.exc_info())


    def getTableLabels(self,row):
        try:
            idItem = self.bookTableWidget.item(row, 0)
            self.bookIDLine.setText(idItem.text())
            nameItem = self.bookTableWidget.item(row, 1)
            self.bookNameEdit.setText(nameItem.text())
            typeItem = self.bookTableWidget.item(row, 2)
            self.bookTypeBox.setCurrentText(typeItem.text())
            authorItem = self.bookTableWidget.item(row, 3)
            self.bookAuthorNameEdit.setText(authorItem.text())
            publisherItem = self.bookTableWidget.item(row, 4)
            self.bookPublisherEdit.setText(publisherItem.text())
            arrivalItem = self.bookTableWidget.item(row, 5).text()
            arrivalDateConvert =  datetime.strptime(arrivalItem, '%m/%d/%Y')
            self.bookArrivalDateEdit.setDateTime(arrivalDateConvert)
            allItems = [idItem.text(), nameItem.text(), typeItem.text(),
                        authorItem.text(), publisherItem.text(), arrivalDateConvert]
            print(allItems)
        except:
            print("Hata:", sys.exc_info())

    def retranslateUi(self, bookDialog):
        _translate = QtCore.QCoreApplication.translate
        bookDialog.setWindowTitle(_translate("bookDialog", "Dialog"))
        self.groupBox.setTitle(_translate("bookDialog", "Kitap İşlemleri"))
        self.bookTypeBox.setItemText(0, _translate("bookDialog", "Korku"))
        self.bookTypeBox.setItemText(1, _translate("bookDialog", "Aksiyon"))
        self.bookTypeBox.setItemText(2, _translate("bookDialog", "Bilim Kurgu"))
        self.bookTypeBox.setItemText(3, _translate("bookDialog", "Eğitim"))
        self.bookTypeBox.setItemText(4, _translate("bookDialog", "Çocuk Klasikleri"))
        self.bookTypeBox.setItemText(5, _translate("bookDialog", "Fantastik"))
        self.bookTypeBox.setItemText(6, _translate("bookDialog", "Kişisel Gelişim"))
        self.bookTypeBox.setItemText(7, _translate("bookDialog", "Din Kültürü"))
        self.label_3.setText(_translate("bookDialog", "Kitap Türü:"))
        self.label_4.setText(_translate("bookDialog", "Geliş Tarihi:"))
        self.label.setText(_translate("bookDialog", "Yazar:"))
        self.label_2.setText(_translate("bookDialog", "Kitap Adı:"))
        self.label_5.setText(_translate("bookDialog", "Yayın Evi:"))
        self.label_6.setText(_translate("bookDialog", "Kitap ID:"))
        self.bookAddButton.setText(_translate("bookDialog", "Ekle"))
        self.bookUpdateButton.setText(_translate("bookDialog", "Güncelle"))
        self.bookDeleteButton.setText(_translate("bookDialog", "Sil"))
        self.bookSearchButton.setText(_translate("bookDialog", "Ara"))
        self.label_7.setText(_translate("bookDialog", "Aranacak Kitap İsmi:"))
        self.bookListUpdateButton.setText(_translate("bookDialog", "Liste Yenile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bookDialog = QtWidgets.QDialog()
    ui = Ui_bookDialog()
    ui.setupUi(bookDialog)
    bookDialog.show()
    sys.exit(app.exec_())
