import sys

from PyQt5.QtWidgets import QTableWidgetItem

from Data_Layer.user import User

#The UserOpLogic class inherits from the User class and handles adding, deleting, and updating users.
class UserOpLogic(User):


    def __init__(self, name, phone, table, id, search):
        self._sName = search
        self._uID = id
        self._uName = name
        self._uPhone = phone
        self._uTable = table

    #Add user to list operation
    def addUser(self):
        # We check whether there is an element in the ID List and add accordingly.
        try:
            #if user list is empty
            if len(User._userID) == 0:
                # It is checked whether the telephone number entered is a number.
                try:
                    numberConvert = int(self._uPhone)
                    print(numberConvert)
                except:
                    print("Lütfen sadece sayı giriniz!")
                    return None
                #checking whether the entered number is 10 digits or not
                if len(self._uPhone) < 10 or len(self._uPhone) > 10:
                    print("Telefon numarasını yanlış girdiniz!")
                else:
                    self._userID.append(1)
                    print(self._userID)
                    self._userName.append(self._uName)
                    self._userPhone.append(self._uPhone)
                    self.getListItemsToRow(self._uTable)
                    self.updateAllList(self._uTable)
                    print(self._userName, self._userPhone)
                    print(self._userList)
            else:
                # It is checked whether the telephone number entered is a number.
                try:
                    numberConvert = int(self._uPhone)
                    print(numberConvert)
                except:
                    print("Lütfen sadece sayı giriniz!")
                    return None

                #if the entered number or name already exists in the list
                if self._uName in self._userName or self._uPhone in self._userPhone:
                    print("listeye eklecenek elemanda çakışma var.")
                # checking whether the entered number is 10 digits or not
                elif len(self._uPhone) < 10 or len(self._uPhone) > 10:
                    print("Telefon numaranızı yanlış girdiniz!")
                else:
                    for i in range(len(self._userID)):
                        if self._userID[i] == self._userID[-1]:
                            self._userID.append(i + 2)
                    # We add other parameters to the relevant lists.
                    self._userName.append(self._uName)
                    self._userPhone.append(self._uPhone)
                    self.getListItemsToRow(self._uTable)
                    self.updateAllList(self._uTable)
                    print(self._userName, self._userPhone)
                    print(self._userList)

        except:
            print("ID eklemede hata var!", sys.exc_info())



    #user deletion that conflicts with variables
    def deleteUser(self):
        try:
            #A for loop is created for the length of the userID.
            for i in range(len(self._userID)):
                #The similarity of the entered values with the values in the list is checked
                if self._uName == self._userName[i] and self._uPhone == self._userPhone[i]:
                    if self._userID[i] != self._userID[-1]:
                        for j in range(i+1, len(self._userID)):
                            self._userID[j] -= 1
                    else:
                        pass
                    self.removeRow(self._uTable)
                    self._userID.remove(self._userID[i])
                    self._userName.remove(self._uName)
                    self._userPhone.remove(self._uPhone)
                    self.updateAllList(self._uTable)
                    print(self._userName, self._userPhone)
                    print(self._userList)
                    break
                else:
                    print("Bu isim ve telefon numarasına sahip kullanıcı bulunamadı!")
        except:
            print("Hata:",sys.exc_info())

    #The method that updates the information of the desired user
    def updateUser(self):
        try:
            convertID = int(self._uID)
            for i in range(len(self._userID)):
                #if the entered id is found in the list
                if convertID == self._userID[i]:
                    """
                    if self.uName in User.userName or self.uPhone in User.userPhone:
                        print("listede güncellenecek isim çakışması var.")
                    else:
                    """
                    self._userName[i] = self._uName
                    self._userPhone[i] = self._uPhone
                    rowData = [self._userID[i], self._userName[i], self._userPhone[i]]
                    self.updateNameTableRow(self._uTable, rowData)
                    self.updateAllList(self._uTable)
                    print(self._userList)
                else:
                    print("Koşul sağlanamadı")
                    pass
        except:
            print("Hata:", sys.exc_info())

    #Method that allows the desired user to be searched from the list and added to the table later.
    def searchUser(self):
        if len(self._userID) == 0:
            print("Listede Hiç Eleman yok")
            pass
        else:
            for i in range(len(self._userID)):
                if  self._sName == self._userName[i] or self._sName == self._userPhone[i]:
                    row_List = [self._userID[i], self._userName[i], self._userPhone[i]]
                    self.addSearchUserToTable(self._uTable, row_List)
                    break
                else:
                    print("Listede bu isimde eleman bulunamadı")
                    pass

    #Method for updating the user list and adding it back to the table
    def refreshConnect(self):
        try:
            self.updateAllList(self._uTable)
        except:
            print("updateTable Metodunda hata var!", sys.exc_info())



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

    #Method to add only the searched user to the table
    def addSearchUserToTable(self, table, row_data):
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

    #method that allows users to be eliminated sequentially
    def getListItemsToRow(self, tWidget):
        try:
            if len(self._userID) == 0:
                pass
            else:
                for i in range(len(self._userID)):
                    if self._userID[i] == self._userID[-1]:
                        row_List = [self._userID[i], self._userName[i], self._userPhone[i]]
                        self.addTableRow(tWidget, row_List)
                    else:
                        pass
        except:
            print("Hata:", sys.exc_info())

    #The added user is being added to the table.
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
        if len(self._userID) == 0:
            print("Listede Hiç Eleman yok")
            pass
        else:
            for i in range(len(self._userID)):
                if self._userName[i] == self._uName and self._userPhone[i] == self._uPhone:
                    row_Item = self._userID[i]
                    self.removeRowFromTable(tWidget, row_Item)
                    break
                else:
                    print("Listede bu isimde eleman bulunamadı")
                    pass

    #method to delete only the desired line
    def removeRowFromTable(self, table, row_data):
        try:
            row = row_data
            row -= 1
            table.removeRow(row)
        except:
            print("Hata removeRowFromTable metodundan kaynaklı", sys.exc_info())

    #method to delete all items in table
    def deleteAllItems(self, table):
        while (table.rowCount() > 0):
            table.removeRow(0)

    def updateAllList(self, tWidget):
        try:
            self.deleteAllItems(tWidget)
            for i in range(len(self._userID)):
                rowItem = [self._userID[i], self._userName[i], self._userPhone[i]]
                self.addTableRow(tWidget, rowItem)
        except:
            print("updateTable Metodunda hata var!", sys.exc_info())