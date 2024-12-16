from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QGraphicsBlurEffect
from PyQt5.uic import loadUi
from BlurWindow.blurWindow import blur


def function(oldPass: str = "null", newPass:str = "null", confirmPass: str = "null"):
    print(oldPass, newPass, confirmPass)

#changepassword.function(self.oldpassword.text(), self.newpassword.text(), self.confirmpassword.text())

class Testing(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("testing.ui", self)
        self.pushButton.clicked.connect(self.test)
        self.blur_effect = QGraphicsBlurEffect()
        self.widget = None

    def test(self):
        self.hidden = True
        self.close()
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)



