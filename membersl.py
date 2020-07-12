import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import addmember
import sqlite3

lfont=QFont("Aria" ,12)
bfont=QFont("Arial",10)
connect=sqlite3.connect("library.db")

cursor=connect.cursor()

class Memberl(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,100,475,600)
        self.setWindowTitle("Members List")
        self.setStyleSheet("background-color:#e61919;")
        self.ui()

    def ui(self):
        ############# members list label
        memberslbl = QLabel("MEMBERS LIST", self)
        memberslbl.move(190, 200)
        memberslbl.setFont(lfont)
        ################ list widget
        self.memberlist = QListWidget(self)
        self.memberlist.move(30, 275)
        self.memberlist.setStyleSheet("background-color:#ffffff;")
        memberslst=cursor.execute("SELECT * FROM members")
        for memberr in memberslst.fetchall():
            print(memberr)
            self.memberlist.addItem(str(memberr[0])+"-"+memberr[1]+" / "+memberr[2]+" / "+memberr[3])
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
        updatememberbtn.clicked.connect(self.updatememberf)
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
    def updatememberf(self):

        self.member=addmember.Membera()
        self.member.show()
        #self.close()
        mmember=self.memberlist.currentItem().text()
        #print(mmember)####buradan devam edeceksin
        global id
        id=mmember[0]
        print(id)
        cursor.execute("select * from members where id=?",(id,))
        for i in cursor.fetchall():
            self.member.name.setText(i[1])
            self.member.location.setText(i[2])
            self.member.idun.setText(id)
            self.member.rgsbutton.setEnabled(False)
            self.member.updatebutton.setEnabled(True)

#######################burasi silinecek

def main():
    application=QApplication(sys.argv)
    member=Memberl()
    sys.exit(application.exec_())
if __name__ == '__main__':
    main()

#connect.close()  this is fault