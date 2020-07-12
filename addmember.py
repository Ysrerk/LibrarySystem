import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3
import membersl

bfont=QFont("Arial",10)
connect=sqlite3.connect("library.db")
cursor=connect.cursor()
class Membera(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Member Page")
        self.setGeometry(120,100,350,500)
        self.setStyleSheet("background-color:#e61919;")
        self.ui()

    def ui(self):
        ### title
        self.title=QLabel("MEMBER REGISTRATION",self)
        self.title.move(100,25)
        self.title.setFont(bfont)
        ###id
        self.idun = QLineEdit("")

        #########user name
        self.name=QLineEdit(self)
        self.name.move(110,75)
        self.name.setPlaceholderText("Your Name")
        self.name.setStyleSheet("background-color:#ffffff;")

        #####location
        self.location = QLineEdit(self)
        self.location.move(110, 110)
        self.location.setPlaceholderText("Location")
        self.location.setStyleSheet("background-color:#ffffff;")

        ###register button

        self.rgsbutton=QPushButton("Save",self)
        self.rgsbutton.move(130, 160)
        self.rgsbutton.resize(100,25)
        self.rgsbutton.setStyleSheet("background-color:#ffffff;")
        self.rgsbutton.clicked.connect(self.savefunc)
        #####update
        self.updatebutton = QPushButton("update", self)
        self.updatebutton.move(130, 190)
        self.updatebutton.resize(100, 25)
        self.updatebutton.setStyleSheet("background-color:#ffffff;")
        self.updatebutton.setEnabled(False)
        self.updatebutton.clicked.connect(self.updatefunc)

        ##########main amage
        userimage = QLabel(self)
        userimage.move(90, 250)
        userimage.setPixmap(QPixmap("images/register.png"))



        self.show()
    def savefunc(self):
        namev=self.name.text()
        locationv=self.location.text()

        cursor.execute("INSERT INTO members VALUES(?,?,?,?)",(None,namev,locationv,"Active"))
        QMessageBox.information(self,"QMessageBox.Information()","Nem member saved")
        connect.commit()
    def updatefunc(self):
        nameu=self.name.text()
        locationu=self.location.text()
        idu=self.idun.text()
        cursor.execute("UPDATE members SET name=?,Location=? where id=?",(nameu,locationu,idu))
        connect.commit()
        QMessageBox.information(self, "QMessageBox.Information()", "members  info updated")
        self.name.setText("")
        self.location.setText("")
        self.close()



################burasi silinecek
def main():
    application=QApplication(sys.argv)
    member=Membera()
    sys.exit(application.exec_())
if __name__ == '__main__':
    main()
#connect.close()