import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sqlite3
import addbook
connect=sqlite3.connect("library.db")
cursor=connect.cursor()
lfont=QFont("Aria" ,12)
bfont=QFont("Arial",10)
class Booklist(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 100, 475, 600)
        self.setWindowTitle("Book List")
        self.setStyleSheet("background-color:#e61919;")
        self.ui()




    def ui(self):

        #booklist widget
        self.booklst=QListWidget(self)
        self.booklst.move(125,50)
        self.booklst.setStyleSheet("background-color:#ffffff;")
        booksll=cursor.execute("select * from books")

        for i in booksll.fetchall():
            self.booklst.addItem(str(i[0])+"-"+i[1]+"/"+i[2]+"/"+i[3])
        ####

        self.membercmb=QComboBox(self)
        self.membercmb.move(170,260)
        self.membercmb.resize(150,25)
        self.membercmb.setStyleSheet("background-color:#ffffff;")
        self.membercmb.setVisible(True)


        cursor.execute("select * from members")
        for i in cursor.fetchall():
            self.membercmb.addItem(str(i[0])+"-"+i[1])


        ####update books

        self.updatebookbtn = QPushButton("Update Book", self)
        self.updatebookbtn.move(170,325)
        self.updatebookbtn.setStyleSheet("background-color:#ffffff;")
        self.updatebookbtn.resize(150, 25)
        self.updatebookbtn.setFont(bfont)
        self.updatebookbtn.setIcon(QIcon("images/update.png"))
        self.updatebookbtn.clicked.connect(self.updatebookf)

        ###give book

        self.givebookbtn = QPushButton("Give Book", self)
        self.givebookbtn.move(170, 360)
        self.givebookbtn.setStyleSheet("background-color:#ffffff;")
        self.givebookbtn.resize(150, 25)
        self.givebookbtn.setFont(bfont)
        self.givebookbtn.setIcon(QIcon("images/book.png"))
        self.givebookbtn.clicked.connect(self.givebookf)

        ###### ###get book

        self.getbookbtn = QPushButton("Get Book", self)
        self.getbookbtn.move(170, 395)
        self.getbookbtn.setStyleSheet("background-color:#ffffff;")
        self.getbookbtn.resize(150, 25)
        self.getbookbtn.setFont(bfont)
        self.getbookbtn.setIcon(QIcon("images/book2.png"))
        self.getbookbtn.clicked.connect(self.getbookf)







        self.show()

    def updatebookf(self):


        self.book=addbook.Addbook()
        self.book.show()

        a=self.booklst.currentItem().text()
        bookid=a.split("-")[0]
        print(bookid)

        cursor.execute("select * from books where id=?",(bookid))

        for i in cursor.fetchall():
            self.book.bookname.setText(i[1])
            self.book.writername.setText(i[2])
            self.book.bookquantity.setText(i[3])
            self.book.idun.setText(bookid)
        self.book.updatebutton.setEnabled(True)
        self.book.savebutton.setEnabled(False)

    def givebookf(self):
        a = self.booklst.currentItem().text()
        bookid = a.split("-")[0]
        print(bookid)

        memberinf=self.membercmb.currentText()
        memberid=memberinf.split("-")[0]
        print(memberid)



        cursor.execute("select * from books where id=?",(bookid))
        for i in cursor.fetchall():
            bookquantity=int(i[3])

            if bookquantity>0:
                cursor.execute("INSERT  INTO bookmember VALUES(?,?,?,?)", (None, bookid, memberid, "Active"))
                cursor.execute("UPDATE  books SET quantity=? where id=?",(str(bookquantity-1),bookid))
                if bookquantity==1:
                    cursor.execute("UPDATE  books SET status=? where id=?", ("Passive", bookid))

                connect.commit()
                QMessageBox.information(self, "QMessageBox.Information()", "process completed")
            else:
                QMessageBox.information(self, "QMessageBox.Information()", "You can nat give this book")

        #self.close()

    def getbookf(self):
        a = self.booklst.currentItem().text()
        bookid = a.split("-")[0]
        print(bookid)

        memberinf = self.membercmb.currentText()
        memberid = memberinf.split("-")[0]
        print(memberid)

        cursor.execute("select * from books where id=?", (bookid))
        for i in cursor.fetchall():
            bookquantity = int(i[3])
        cursor.execute("select * from bookmember where bookid=? and memberid=?",(bookid,memberid))
        for i in cursor.fetchall():
            relationid=int(i[0])
            print(relationid)

            if bookquantity == 0:
                cursor.execute("UPDATE bookmember SET status=? where id=?", ("Passive",relationid))
                cursor.execute("UPDATE  books SET quantity=? where id=?", (str(bookquantity + 1), bookid))
                if bookquantity == 0:
                    cursor.execute("UPDATE  books SET status=? where id=?", ("Active", bookid))

                connect.commit()
                QMessageBox.information(self, "QMessageBox.Information()", "process succefully completed")
            else:
                #cursor.execute("UPDATE bookmember SET status=? where id=?", ("Passive", relationid))
                cursor.execute("UPDATE  books SET quantity=? where id=?", (str(bookquantity + 1), bookid))
                if bookquantity == 0:
                    cursor.execute("UPDATE  books SET status=? where id=?", ("Active", bookid))

                connect.commit()
                QMessageBox.information(self, "QMessageBox.Information()", "process succefully completed")


def main():
    application=QApplication(sys.argv)
    booklist=Booklist()
    sys.exit(application.exec_())

if __name__ == '__main__':
    main()