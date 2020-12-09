

#
import sys

from PyQt5.QtWidgets import QTableWidgetItem

from Data_Layer.book import self

#The BookOpLogic class inherits from the Book class and handles adding, deleting, and updating books.
class BookOpLogic(self):

    #The __init__ method will work first and create objects for all variables.
    def __init__(self, id, name, type, author, publisher, arrivalDate, table, search):
        self._bID = id
        self._bName = name
        self._bType = type
        self._bPub = publisher
        self._bAuth = author
        self._bArrival = arrivalDate
        self._bTable = table
        self._bSearch = search

    # Add book to list operation
    def addBook(self):
        #We check whether there is an element in the ID List and add accordingly.
        try:
            if len(self._bookID) == 0:
                self._bookID.append(1)
                print(self._bookID)
            else:
                for i in range(len(self._bookID)):
                    if self._bookID[i] == self._bookID[-1]:
                        self._bookID.append(i + 2)
        except:
            print("ID eklemede hata var!", sys.exc_info())

        #We add other parameters to the relevant lists.
        if self._bName in self._bookName:
            print("Kitap isimleri çakışıyor!")
        else:
            self._bookName.append(self._bName)
            self._bookType.append(self._bType)
            self._bookAuthor.append(self._bAuth)
            self._bookPublisher.append(self._bPub)
            self._bookArrivalDate.append(self._bArrival)
            self.getListItemsToRow(self._bTable)
            self.updateAllList(self._bTable)
            print(self._bookList)

    # book deletion that conflicts with variables
    def deleteBook(self):
        for i in range(len(self._bookID)):
            #method that deletes the book and deletes the ID order of the book to be deleted
            if self._bName == self._bookName[i] and self._bType == self._bookType[i] and \
                    self._bAuth == self._bookAuthor[i] and self._bPub == self._bookPublisher[i] \
                    and self._bArrival == self._bookArrivalDate[i]:
                if self._bookID[i] != self._bookID[-1]:
                    for j in range(i + 1, len(self._bookID)):
                        self._bookID[j] -= 1
                else:
                    pass
                self.removeRow(self._bTable)
                self._bookID.remove(self._bookID[i])
                self._bookName.remove(self._bName)
                self._bookType.remove(self._bType)
                self._bookAuthor.remove(self._bAuth)
                self._bookPublisher.remove(self._bPub)
                self._bookArrivalDate.remove(self._bArrival)
                self.updateAllList(self._bTable)
                print(self._bookList)
                break
            else:
                print("Bu özelliklere sahip bir kitap bulunamadı!")

    #The method that updates the data of the desired book
    def updateBook(self):
        try:
            convertID = int(self._bID)
            for i in range(len(self._bookID)):
                #if the entered id is in the book list
                if convertID == self._bookID[i]:
                    self._bookName[i] = self._bName
                    self._bookType[i] = self._bType
                    self._bookAuthor[i] = self._bAuth
                    self._bookPublisher[i] = self._bPub
                    self._bookArrivalDate[i] = self._bArrival
                    rowData = [self._bookID[i], self._bookName[i], self._bookType[i],
                               self._bookAuthor[i], self._bookPublisher[i], self._bookArrivalDate[i]]
                    self.updateNameTableRow(self._bTable, rowData)
                    self.updateAllList(self._bTable)
                    print(self._bookList)
                else:
                    print("Koşul sağlanamadı")
                    pass
        except:
            print("Hata:", sys.exc_info())

    #method to search the desired book in the list
    def searchBook(self):
        if len(self._bookID) == 0:
            print("Listede Hiç Eleman yok")
            pass
        else:
            for i in range(len(self._bookID)):
                if self._bSearch == self._bookName[i]:
                    row_List = [self._bookID[i], self._bookName[i], self._bookType[i],
                                self._bookAuthor[i], self._bookPublisher[i], self._bookArrivalDate[i]]
                    self.addSearchBookToTable(self._bTable, row_List)
                    break
                else:
                    print("Listede bu isimde eleman bulunamadı")
                    pass


    # The added user is being added to the table.
    def updateNameTableRow(self, table, row_data):
        row = row_data[0]
        row -= 1
        col = 0
        for item in row_data:
            cell = QTableWidgetItem(str(item))
            table.setItem(row, col, cell)
            col += 1
        print("Fonksiyon Çalışıyor!")

    #method that only adds the searched book to the table
    def addSearchBookToTable(self, table, row_data):
        try:
            col = 0
            self.deleteAllItems(table)
            table.setRowCount(1)
            for item in row_data:
                cell = QTableWidgetItem(str(item))
                table.setItem(0, col, cell)
                col += 1

        except:
            print("Hata:",sys.exc_info())


    #It allows the elements to be added to the list sequentially in book insertion one by one.
    def getListItemsToRow(self, tWidget):
        try:
            if len(self._bookID) == 0:
                pass
            else:
                for i in range(len(self._bookID)):
                    if self._bookID[i] == self._bookID[-1]:
                        row_List = [self._bookID[i], self._bookName[i], self._bookType[i],
                                    self._bookAuthor[i], self._bookPublisher[i], self._bookArrivalDate[i]]
                        self.addTableRow(tWidget, row_List)
                    else:
                        pass
        except:
            print("Hata:", sys.exc_info())


    #The added book is being added to the table.
    def addTableRow(self, table, row_data):
        row = table.rowCount()
        table.setRowCount(row + 1)
        col = 0
        for item in row_data:
            cell = QTableWidgetItem(str(item))
            table.setItem(row, col, cell)
            col += 1

    #The added user is being added to the table.
    def removeRow(self, tWidget):
        #if book list is empty
        if len(self._bookID) == 0:
            print("Listede Hiç Eleman yok")
            pass
        else:
            for i in range(len(self._bookID)):
                #If the entered data and the data to be deleted match
                if self._bName == self._bookName[i] and self._bType == self._bookType[i] and \
                    self._bAuth == self._bookAuthor[i] and self._bPub == self._bookPublisher[i] \
                        and self._bArrival == self._bookArrivalDate[i]:

                    row_Item = self._bookID[i]
                    self.removeRowFromTable(tWidget, row_Item)
                    break

                else:
                    print("Listede bu isimde eleman bulunamadı")
                    pass

    #deletes only the desired row from the table.
    def removeRowFromTable(self, table, row_data):
        try:
            row = row_data
            row -= 1
            table.removeRow(row)
        except:
            print("Hata removeRowFromTable metodundan kaynaklı", sys.exc_info())

    #deletes all data in the table.
    def deleteAllItems(self, table):
        while (table.rowCount() > 0):
            table.removeRow(0)

    #Required method for table refresh
    def refreshConnect(self):
        try:
            self.updateAllList(self._bTable)
        except:
            print("updateTable Metodunda hata var!")

    #A request is sent to update all the books in the list and add them to the table.
    def updateAllList(self, tWidget):
        try:
            self.deleteAllItems(tWidget)
            for i in range(len(self._bookID)):
                rowItem = [self._bookID[i], self._bookName[i], self._bookType[i],
                           self._bookAuthor[i], self._bookPublisher[i], self._bookArrivalDate[i]]
                self.updateAllTable(tWidget, rowItem)
        except:
            print("updateTable Metodunda hata var!", sys.exc_info())

    #All books in the list are added to the relevant table.
    def updateAllTable(self, table, rowData):
        try:
            row = table.rowCount()
            col = 0
            table.setRowCount(row+1)
            for item in rowData:
                cell = QTableWidgetItem(str(item))
                table.setItem(row, col, cell)
                col += 1
            print("Fonksiyon Çalışıyor!")
        except:
            print("updateTable Metodunda hata var!")