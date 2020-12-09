import sys
import datetime
from datetime import *

from PyQt5.QtWidgets import QTableWidgetItem

from Data_Layer.book import self
from Data_Layer.deposit import Deposit
from Data_Layer.user import User


class DepositOpLogic(Deposit, User, self):



    def __init__(self, table, book, user, date, day, search):
        #Objects required for the insertion are defined.
        self._aTable = table
        self._dBook = book
        self._dUser = user
        self._dDate = date
        self._dDay = day
        self._dSearch = search

        self._books = Deposit._depositBookName
        self._users = Deposit._depositUserName
        self._dates = Deposit._depositTakeDate
        self._days = Deposit._depositAddDay
        self._list = Deposit._depositList
        print("deneme")


    #is the method of adding deposit books. The book name, user name, consignment date and delivery date are entered for the requested deposit.
    def addDeposit(self):
        try:
            #if book is already in deposit books
            if self._dBook in self._books:
                print("Bu kitap zaten emanette olduğu için eklenemez!")
                pass
            else:
                #If the desired book and user are available, deposit is added.
                if self._dBook in self._bookName and self._dUser in User._userName:
                    self._users.append(self._dUser)
                    self._books.append(self._dBook)
                    self._dates.append(self._dDate)

                    if self._dDay == "15 Gün":
                        startDate = datetime.strptime(self._dDate, '%m/%d/%Y')
                        endDate = (startDate + timedelta(days=15)).strftime('%m/%d/%Y')
                        lastDate = str(endDate)
                        self._days.append(lastDate)
                    elif self._dDay == "30 Gün":
                        startDate = datetime.strptime(self._dDate, '%m/%d/%Y')
                        endDate = (startDate + timedelta(days=30)).strftime('%m/%d/%Y')
                        lastDate = str(endDate)
                        self._days.append(lastDate)
                    elif self._dDay == "60 Gün":
                        startDate = datetime.strptime(self._dDate, '%m/%d/%Y')
                        endDate = (startDate + timedelta(days=60)).strftime('%m/%d/%Y')
                        lastDate = str(endDate)
                        self._days.append(lastDate)

                    self.getUsers()
                    self.getBooks()
                    print(self._list)
                else:
                    print("Kullanıcı veya İsim hatalı")
        except:
            print("addDeposit hata:", sys.exc_info())

    #Delete selected user from deposit list and update deposit table
    def deleteDeposit(self):
        for i in range(len(self._books)):
            #If the entered information matches, the deletion process is initiated.
            if self._dBook == self._books[i] and self._dUser == self._users[i] \
                and self._dDate == self._dates[i] and self._dDay == self._days[i]:
                self.deleteAllItems(self._aTable)
                self._books.remove(self._books[i])
                self._users.remove(self._users[i])
                self._dates.remove(self._dates[i])
                self._days.remove(self._days[i])
                self.updateDepositList(self._aTable)
                print(Deposit._depositList)

    #Call User and Book List Update Method
    def getUsers(self):
        self.updateAllUserList(self._aTable)
    def getBooks(self):
        self.updateAllBookList(self._aTable)

    #It is checked whether the called user is in the User list. If the user is registered in the User list, it is called to the table.
    def searchUser(self):
        print(self._dUser)
        if len(User._userID) == 0:
            print("Listede Hiç Eleman yok")
        else:
            #if the search box is empty
            if len(self._dUser) == 0:
                self.deleteAllItems(self._aTable)
                for i in range(len(User._userID)):
                    row_List = [User._userID[i], User._userName[i], User._userPhone[i]]
                    self.updateAllTable(self._aTable, row_List)
            else:
                for i in range(len(User._userID)):
                    self.deleteAllItems(self._aTable)
                    if self._dUser == User._userName[i]:
                        row_List = [User._userID[i], User._userName[i], User._userPhone[i]]
                        self.updateAllTable(self._aTable, row_List)
                        break
                    else:
                        print("Listede bu isimde eleman bulunamadı")
                        pass

    # The desired book is searched from the list and only itself is added to the table.
    def searchBook(self):
        try:
            if len(self._bookID) == 0:
                print("Listede Hiç Eleman yok")
                pass
            else:
                if len(self._dBook) == 0:
                    self.deleteAllItems(self._aTable)
                    self.updateAllBookList(self._aTable)
                else:
                    for i in range(len(self._bookID)):
                        #if the wanted book is on the deposit list
                        if self._dBook in self._books:
                            pass
                        #if the searched variable exists in the book list
                        elif self._dBook == self._bookName[i]:
                            row_List = [self._bookID[i], self._bookName[i], self._bookType[i],
                                        self._bookAuthor[i], self._bookPublisher[i], self._bookArrivalDate[i]]
                            self.deleteAllItems(self._aTable)
                            self.updateAllTable(self._aTable, row_List)
                            break
                        else:
                            print("Listede bu isimde eleman bulunamadı")
                            pass
        except:
            print("searchBook metodunda hata:", sys.exc_info())

    #The desired deposit is searched from the list and only itself is added to the table.
    def searchDeposit(self):
        if len(self._bookID) == 0:
            print("Listede Hiç Eleman yok")
            pass
        else:
            self.deleteAllItems(self._aTable)
            for i in range(len(self._bookID)):
                if self._dSearch == self._books[i] or self._dSearch == self._users[i]:
                    row_List = [self._books[i], self._users[i], self._dates[i],
                                self._days[i]]
                    self.updateAllTable(self._aTable, row_List)
                else:
                    print("Listede bu isimde eleman bulunamadı")
                    pass

    #It is a method that adds time for books in deposit.
    def extraTime(self):
        try:
            for i in range(len(self._books)):
                #It is searched which element in the list matches with the entered information.
                if self._dBook == self._books[i] and self._dUser == self._users[i] \
                    and self._dDate == self._dates[i] and self._dDay == self._days[i]:

                    #An extra 15 days is added to the selected consignment and the delivery date is updated.
                    dayItemConvert = datetime.strptime(self._days[i], '%m/%d/%Y')
                    addDay = (dayItemConvert + timedelta(days=15)).strftime('%m/%d/%Y')
                    finalDay = str(addDay)
                    self._days[i] = finalDay

                    self.updateDepositList(self._aTable)

                    print(Deposit._depositList)
        except:
            print("extraTime Hata:", sys.exc_info())

    #Method of filtering out-of-date deposits
    def expiredDepositFilter(self):
        #if deposit list is empty
        if Deposit._depositBookName is None:
            print("Emanet Kitap Yok!")
        else:
            self.deleteAllItems(self._aTable)
            for i in range(len(Deposit._depositBookName)):
                #converting the time and checking whether the day has passed
                time = Deposit._depositAddDay[i]
                convertDate = datetime.strptime(time, '%m/%d/%Y')
                today = datetime.now()

                if today > convertDate:
                    rowItem = [self._books[i], self._users[i], self._dates[i], self._days[i]]
                    # expired deposits will be added to the table
                    self.updateAllTable(self._aTable, rowItem)
                else:
                    pass
    #It is the method that allows the escrow list to be updated and reloaded
    def updateAllDepositList(self):
        try:
            #if deposit list is empty
            if len(Deposit._depositBookName) == 0:
                print("liste boş")
            else:
                self.deleteAllItems(self._aTable)
                for i in range(len(Deposit._depositBookName)):
                    rowItem = [self._books[i], self._users[i], self._dates[i], self._days[i]]
                    self.updateAllTable(self._aTable, rowItem)
        except:
            print("updateDepositList Metodunda hata var! : ", sys.exc_info())

    #Delete All List İtems in Table
    def deleteAllItems(self, table):
        while (table.rowCount() > 0):
            table.removeRow(0)

    #Method that calls all deposits from the list
    def updateDepositList(self, tWidget):
        try:
            #All elements in the table are deleted. then all books on the deposit list are reassigned into a list.
            self.deleteAllItems(tWidget)
            for i in range(len(self._books)):
                rowItem = [self._books[i], self._users[i], self._dates[i], self._days[i]]
                # deposits will be added to the table
                self.updateAllTable(tWidget, rowItem)
        except:
            print("updateDepositList hatası:",sys.exc_info())

    #Method that calls all users from the list
    def updateAllUserList(self, tWidget):
        try:
            # All elements in the table are deleted. then all books on the user list are reassigned into a list.
            self.deleteAllItems(tWidget)
            for i in range(len(User._userID)):
                rowItem = [User._userID[i], User._userName[i], User._userPhone[i]]
                # users will be added to the table
                self.updateAllTable(tWidget, rowItem)
        except:
            print("updateUserTable Metodunda hata var!")

    #Method that calls all books from the list
    def updateAllBookList(self, tWidget):
        try:
            # All elements in the table are deleted. then all books on the book list are reassigned into a list.
            self.deleteAllItems(tWidget)
            for i in range(len(self._bookID)):
                if self._bookName[i] in self._books:
                    pass
                else:
                    rowItem = [self._bookID[i], self._bookName[i], self._bookType[i],
                               self._bookAuthor[i], self._bookPublisher[i], self._bookArrivalDate[i]]
                    #books will be added to the table
                    self.updateAllTable(tWidget, rowItem)
        except:
            print("updateBookTable Metodunda hata var!:",sys.exc_info())

    #Transfers all variables in the lists to the table.
    def updateAllTable(self, table, rowData):
        try:
            row = table.rowCount()
            col = 0
            table.setRowCount(row + 1)
            for item in rowData:
                cell = QTableWidgetItem(str(item))
                table.setItem(row, col, cell)
                col += 1
            print("Fonksiyon Çalışıyor!")
        except:
            print("updateAllTable Metodunda hata var! : ", sys.exc_info())

