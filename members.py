import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import addmember
import sqlite3

lfont=QFont("Aria" ,12)
bfont=QFont("Arial",10)
connect=sqlite3.connect("library.db")

cursor=connect.cursor()

class Member(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,100,475,600)
        self.setWindowTitle("Members List")
        self.setStyleSheet("background-color:#e61919;")
        self.ui()

    def ui(self):
        #############image
        # membersimg = QLabel(self)
        # membersimg.setPixmap(QPixmap("images/memberlist2.png"))
        # membersimg.move(130, 25)

        ############# members list label
        memberslbl=QLabel("MEMBERS LIST",self)
        memberslbl.move(190,200)
        memberslbl.setFont(lfont)

        ################ list widget
        memberlistwidget=QListWidget(self)
        memberlistwidget.move(30,275)
        memberlistwidget.setStyleSheet("background-color:#ffffff;")

        membersl=cursor.execute("SELECT * FROM members")
        for member in membersl.fetchall():
            #print(member)
            memberlistwidget.addItem(str(member[0])+"-"+member[1]+" / "+member[2]+" / "+member[3])
        ###add new member button
        addmemberbtn = QPushButton("Add Member", self)
        addmemberbtn.move(310, 285)
        addmemberbtn.setStyleSheet("background-color:#ffffff;")
        addmemberbtn.resize(150, 25)
        addmemberbtn.setFont(bfont)
        addmemberbtn.setIcon(QIcon("images/people2.png"))
        addmemberbtn.clicked.connect(self.addmemberf)
        ########### update member info

        updatememberbtn = QPushButton("Update Member", self)
        updatememberbtn.move(310, 325)
        updatememberbtn.setStyleSheet("background-color:#ffffff;")
        updatememberbtn.resize(150, 25)
        updatememberbtn.setFont(bfont)
        updatememberbtn.setIcon(QIcon("images/update.png"))
        ##addmemberbtn.clicked.connect(self.addmember)

        #####Delete Member

        deletememberbtn = QPushButton("Delete Member", self)
        deletememberbtn.move(310, 365)
        deletememberbtn.setStyleSheet("background-color:#ffffff;")
        deletememberbtn.resize(150, 25)
        deletememberbtn.setFont(bfont)
        deletememberbtn.setIcon(QIcon("images/deleteuser.png"))

        #####Display  member info

        displaymemberbtn = QPushButton("Display Member", self)
        displaymemberbtn.move(310, 405)
        displaymemberbtn.setStyleSheet("background-color:#ffffff;")
        displaymemberbtn.resize(150, 25)
        displaymemberbtn.setFont(bfont)
        displaymemberbtn.setIcon(QIcon("images/displaymember.png"))

        self.show()

    def addmemberf(self):
        self.member = addmember.Membera()
        self.member.show()

#######################burasi silinecek
def main():
    application=QApplication(sys.argv)
    member=Member()
    sys.exit(application.exec_())
if __name__ == '__main__':
    main()

#connect.close()