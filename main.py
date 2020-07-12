import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import membersl,addmember,addbook,booklistp

bfont=QFont("Arial",10)
tfont=QFont("Arial",16)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library System")
        self.setGeometry(100,100,350,500)
        self.setStyleSheet("background-color:#e61919;")

        self.ui()


    def ui(self):
        yasarerkan=QLabel("@Yasar ERKAN",self)
        yasarerkan.move(260,480)
        mainimage=QLabel(self)
        mainimage.move(90,250)
        mainimage.setPixmap(QPixmap("images/book.png"))


        mbrlistbtn = QPushButton("List Members", self)
        mbrlistbtn.move(110,50)
        mbrlistbtn.setStyleSheet("background-color:#ffffff;")
        mbrlistbtn.resize(150, 25)
        mbrlistbtn.setFont(bfont)
        mbrlistbtn.setIcon(QIcon("images/people2.png"))
        mbrlistbtn.clicked.connect(self.memberlist)


        ########add member define
        addmemberbtn = QPushButton("Add Member", self)
        addmemberbtn.move(110, 100)
        addmemberbtn.setStyleSheet("background-color:#ffffff;")
        addmemberbtn.resize(150, 25)
        addmemberbtn.setFont(bfont)
        addmemberbtn.setIcon(QIcon("images/people2.png"))
        addmemberbtn.clicked.connect(self.addmember)
        #############Add book define
        addbookbtn = QPushButton("Add Book", self)
        addbookbtn.move(110, 150)
        addbookbtn.setStyleSheet("background-color:#ffffff;")
        addbookbtn.resize(150, 25)
        addbookbtn.setFont(bfont)
        addbookbtn.setIcon(QIcon("images/addbook.png"))
        addbookbtn.clicked.connect(self.addbook)
        ##########List Book define
        listbookbtn = QPushButton("List Book", self)
        listbookbtn.move(110, 200)
        listbookbtn.setStyleSheet("background-color:#ffffff;")
        listbookbtn.resize(150, 25)
        listbookbtn.setFont(bfont)
        listbookbtn.setIcon(QIcon("images/booklist.png"))
        listbookbtn.clicked.connect(self.booklist)
        self.show()

    def memberlist(self):
        self.member = membersl.Memberl()
        self.member.show()

    def addmember(self):
        self.member = addmember.Membera()
    def addbook(self):
        self.book=addbook.Addbook()
        self.show()
    def booklist(self):
        self.bookl=booklistp.Booklist()
        self.show()












def main():
    aplication=QApplication(sys.argv)
    window=Window()
    sys.exit(aplication.exec_())
if __name__ == '__main__':
    main()