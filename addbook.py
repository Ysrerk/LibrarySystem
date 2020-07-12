import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import addmember
import sqlite3

lfont=QFont("Aria" ,12)
bfont=QFont("Arial",10)
connect=sqlite3.connect("library.db")
cursor=connect.cursor()

class Addbook(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,100,475,600)
        self.setWindowTitle("ADD BOOK PAGE")
        self.setStyleSheet("background-color:#e61919;")
        self.ui()

    def ui(self):

        ####Title
        booktitle=QLabel("ADD NEW BOOKS",self)
        booktitle.move(175,130)
        booktitle.setFont(lfont)

        ###id
        self.idun = QLineEdit("")


        ###Book name edit
        self.bookname=QLineEdit(self)
        self.bookname.setPlaceholderText("Book Name")
        self.bookname.setStyleSheet("background-color:#ffffff;")
        self.bookname.move(175,175)
        ###Book writer edit
        self.writername = QLineEdit(self)
        self.writername.setPlaceholderText("Writer Name")
        self.writername.setStyleSheet("background-color:#ffffff;")
        self.writername.move(175, 210)
        ###Book QUANTITY
        self.bookquantity = QLineEdit(self)
        self.bookquantity.setPlaceholderText("Quantity")
        self.bookquantity.setStyleSheet("background-color:#ffffff;")
        self.bookquantity.move(175, 245)

        ###Book image
        bookimage = QLabel(self)
        bookimage.setPixmap(QPixmap("images/addbook.png"))
        bookimage.move(165, 350)

        ####save button

        self.savebutton=QPushButton("Save",self)
        self.savebutton.move(175,290)
        self.savebutton.setStyleSheet("background-color:#ffffff;")
        self.savebutton.clicked.connect(self.booksave)

        ######updatebutton
        self.updatebutton = QPushButton("Update", self)
        self.updatebutton.move(255, 290)
        self.updatebutton.setStyleSheet("background-color:#ffffff;")
        self.updatebutton.clicked.connect(self.bookupdate)
        self.updatebutton.setEnabled(False)


        self.show()

    def booksave(self):
        bname=self.bookname.text()
        wrtname=self.writername.text()
        quantity=self.bookquantity.text()
        cursor.execute("INSERT INTO books VALUES(?,?,?,?,?)",(None,bname,wrtname,quantity,"Active"))

        connect.commit()
        QMessageBox.information(self, "QMessageBox.Information()", "Nem Book saved")
        self.bookname.setText("")
        self.writername.setText("")
        self.bookquantity.setText("")

    def bookupdate(self):
        bnameu=self.bookname.text()
        wrtnameu=self.writername.text()
        quantityu=self.bookquantity.text()
        idu=self.idun.text()

        cursor.execute("UPDATE books set name=?, writer=?,quantity=? where id=?",(bnameu,wrtnameu,quantityu,idu))
        connect.commit()
        QMessageBox.information(self, "QMessageBox.Information()", "books  info updated")
        self.bookname.setText("")
        self.writername.setText("")
        self.bookquantity.setText("")






def main():
    application=QApplication(sys.argv)
    addbook=Addbook()
    sys.exit(application.exec_())
if __name__ == '__main__':
    main()