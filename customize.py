
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsBlurEffect, QMessageBox, QAction, QHeaderView
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from datetime import datetime
from PyQt5.uic import loadUi
from BlurWindow.blurWindow import blur
from PyQt5 import QtGui



def login_customize(self):
    #shadow
    shadow = QGraphicsDropShadowEffect()
    shadow.setOffset(0, 0)
    shadow.setBlurRadius(70)
    self.login_mainFrame.setGraphicsEffect(shadow)
    #echoMode
    self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)

def changePass_customize(self):
    #shadow
    shadow = QGraphicsDropShadowEffect()
    shadow.setOffset(0, 0)
    shadow.setBlurRadius(70)
    self.changePass_mainFrame.setGraphicsEffect(shadow)
    #echoMode
    self.oldPassword_input.setEchoMode(QtWidgets.QLineEdit.Password)
    self.newPassword_input.setEchoMode(QtWidgets.QLineEdit.Password)
    self.confirmPassword_input.setEchoMode(QtWidgets.QLineEdit.Password)


def main_home_customize(self):
    shadow1 = QGraphicsDropShadowEffect()
    shadow1.setOffset(0, 0)
    shadow1.setBlurRadius(20)
    self.home_top_frame.setGraphicsEffect(shadow1)
    shadow2 = QGraphicsDropShadowEffect()
    shadow2.setOffset(0, 0)
    shadow2.setBlurRadius(20)
    self.entry_home_frame.setGraphicsEffect(shadow2)
    shadow3 = QGraphicsDropShadowEffect()
    shadow3.setOffset(0, 0)
    shadow3.setBlurRadius(20)
    self.member_home_frame.setGraphicsEffect(shadow3)
    shadow4 = QGraphicsDropShadowEffect()
    shadow4.setOffset(0, 0)
    shadow4.setBlurRadius(20)
    self.equipment_home_frame.setGraphicsEffect(shadow4)
    shadow5 = QGraphicsDropShadowEffect()
    shadow5.setOffset(0, 0)
    shadow5.setBlurRadius(20)
    self.session_home_frame.setGraphicsEffect(shadow5)
    shadow6 = QGraphicsDropShadowEffect()
    shadow6.setOffset(0, 0)
    shadow6.setBlurRadius(20)
    self.employee_home_frame.setGraphicsEffect(shadow6)
    shadow7 = QGraphicsDropShadowEffect()
    shadow7.setOffset(0, 0)
    shadow7.setBlurRadius(20)
    self.trainer_home_frame.setGraphicsEffect(shadow7)
    pass

def main_entry_customize(self):
    shadow = QGraphicsDropShadowEffect()
    shadow.setOffset(0, 0)
    shadow.setBlurRadius(20)
    self.entry_log_mainFrame.setGraphicsEffect(shadow)

def this_day(self):
    self.this_day_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

def this_week(self):
    self.this_week_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

def this_month(self):
    self.this_month_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

def date_current(self):
    now = datetime.now()  # current date and time
    year = now.strftime("%Y")
    month = now.strftime("%B")
    day = now.strftime("%d")
    self.year_label.setText(year)
    self.day_label.setText(day+",")
    self.month_label.setText(month.upper())

def date_current_home(self):
    now = datetime.now()  # current date and time
    year = now.strftime("%Y")
    month = now.strftime("%B")
    day = now.strftime("%d")
    self.year_label_home.setText(year)
    self.day_label_home.setText(day + ",")
    self.month_label_home.setText(month.upper())





def main_member_customize(self):
    shadow = QGraphicsDropShadowEffect()
    shadow.setOffset(0, 0)
    shadow.setBlurRadius(20)
    self.member_log_mainFrame.setGraphicsEffect(shadow)

    self.expired_mem_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.member_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.member_tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

def main_equipment_customize(self):
    shadow = QGraphicsDropShadowEffect()
    shadow.setOffset(0, 0)
    shadow.setBlurRadius(20)
    self.equipment_log_mainFrame.setGraphicsEffect(shadow)

    self.equipment_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.equipment_tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
    self.equipment_tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)


def main_schedule_customize(self):
    shadow = QGraphicsDropShadowEffect()
    shadow.setOffset(0, 0)
    shadow.setBlurRadius(20)
    self.session_log_mainFrame.setGraphicsEffect(shadow)
    self.session_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.session_tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
    self.mem_session_today_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

def main_employee_customize(self):
    shadow = QGraphicsDropShadowEffect()
    shadow.setOffset(0, 0)
    shadow.setBlurRadius(20)
    self.employee_log_mainFrame.setGraphicsEffect(shadow)
    self.employee_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.employee_tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

def main_trainer_customize(self):
    shadow = QGraphicsDropShadowEffect()
    shadow.setOffset(0, 0)
    shadow.setBlurRadius(20)
    self.trainer_log_mainFrame.setGraphicsEffect(shadow)
    self.trainer_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.trainer_tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
    self.trainer_tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)

def toggled(self):
    width = self.icon_text_widget.width()
    if width == 100:
        newWidth = 350
    else:
        newWidth = 100

    self.animation = QPropertyAnimation(self.icon_text_widget, b"minimumWidth")
    self.animation.setDuration(250)
    self.animation.setStartValue(width)
    self.animation.setEndValue(newWidth)
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    self.animation.start()

def entry_sideFrame(self):
    blur_effect = QGraphicsBlurEffect()
    self.entry_log_mainFrame.setGraphicsEffect(blur_effect)
    width = self.entry_log_sideFrame.width()
    if width == 1:
        newWidth = 450
    else:
        blur_effect.setEnabled(False)
        newWidth = 1

    self.animation = QPropertyAnimation(self.entry_log_sideFrame, b"minimumWidth")
    self.animation.setDuration(250)
    self.animation.setStartValue(width)
    self.animation.setEndValue(newWidth)
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    self.animation.start()

def member_sideFrame(self):
    blur_effect = QGraphicsBlurEffect()
    self.member_log_mainFrame.setGraphicsEffect(blur_effect)
    width = self.member_log_sideFrame.width()
    if width == 1:
        newWidth = 450
    else:
        blur_effect.setEnabled(False)
        newWidth = 1

    self.animation = QPropertyAnimation(self.member_log_sideFrame, b"minimumWidth")
    self.animation.setDuration(250)
    self.animation.setStartValue(width)
    self.animation.setEndValue(newWidth)
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    self.animation.start()


def equipment_sideFrame(self):
    blur_effect = QGraphicsBlurEffect()
    self.equipment_log_mainFrame.setGraphicsEffect(blur_effect)
    width = self.equipment_log_sideFrame.width()
    if width == 1:
        newWidth = 450
    else:
        blur_effect.setEnabled(False)
        newWidth = 1

    self.animation = QPropertyAnimation(self.equipment_log_sideFrame, b"minimumWidth")
    self.animation.setDuration(250)
    self.animation.setStartValue(width)
    self.animation.setEndValue(newWidth)
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    self.animation.start()

def schedule_sideFrame(self):
    blur_effect = QGraphicsBlurEffect()
    self.session_log_mainFrame.setGraphicsEffect(blur_effect)
    width = self.session_log_sideFrame.width()
    if width == 1:
        newWidth = 450
    else:
        blur_effect.setEnabled(False)
        newWidth = 1

    self.animation = QPropertyAnimation(self.session_log_sideFrame, b"minimumWidth")
    self.animation.setDuration(250)
    self.animation.setStartValue(width)
    self.animation.setEndValue(newWidth)
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    self.animation.start()

def employee_sideFrame(self):
    blur_effect = QGraphicsBlurEffect()
    self.employee_log_mainFrame.setGraphicsEffect(blur_effect)
    width = self.employee_log_sideFrame.width()
    if width == 1:
        newWidth = 450
    else:
        blur_effect.setEnabled(False)
        newWidth = 1

    self.animation = QPropertyAnimation(self.employee_log_sideFrame, b"minimumWidth")
    self.animation.setDuration(250)
    self.animation.setStartValue(width)
    self.animation.setEndValue(newWidth)
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    self.animation.start()

def trainer_sideFrame(self):
    blur_effect = QGraphicsBlurEffect()
    self.trainer_log_mainFrame.setGraphicsEffect(blur_effect)
    width = self.trainer_log_sideFrame.width()
    if width == 1:
        newWidth = 450
    else:
        blur_effect.setEnabled(False)
        newWidth = 1

    self.animation = QPropertyAnimation(self.trainer_log_sideFrame, b"minimumWidth")
    self.animation.setDuration(250)
    self.animation.setStartValue(width)
    self.animation.setEndValue(newWidth)
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    self.animation.start()

def disable_components(self):
    self.toggle_btn.setEnabled(False)
    self.home_btn.setEnabled(False)
    self.entry_btn.setEnabled(False)
    self.member_btn.setEnabled(False)
    self.equipment_btn.setEnabled(False)
    self.schedule_btn.setEnabled(False)
    self.emp_btn.setEnabled(False)
    self.trainer_btn.setEnabled(False)
    self.logout_btn.setEnabled(False)
    self.this_day_btn.setEnabled(False)
    self.this_week_btn.setEnabled(False)
    self.this_month_btn.setEnabled(False)
    self.add_walk_in_entry_btn.setEnabled(False)
    self.register_member_btn.setEnabled(False)
    self.add_equipment_btn.setEnabled(False)
    self.edit_equipment_btn.setEnabled(False)
    self.remove_equipment_btn.setEnabled(False)
    self.appoint_btn.setEnabled(False)
    self.cancel_schedule_btn.setEnabled(False)
    self.add_employee_btn.setEnabled(False)
    self.remove_employee_btn.setEnabled(False)
    self.add_trainer_btn.setEnabled(False)
    self.remove_trainer_btn.setEnabled(False)

def enable_components(self):
    self.toggle_btn.setEnabled(True)
    self.home_btn.setEnabled(True)
    self.entry_btn.setEnabled(True)
    self.member_btn.setEnabled(True)
    self.equipment_btn.setEnabled(True)
    self.schedule_btn.setEnabled(True)
    self.emp_btn.setEnabled(True)
    self.trainer_btn.setEnabled(True)
    self.logout_btn.setEnabled(True)
    self.this_day_btn.setEnabled(True)
    self.this_week_btn.setEnabled(True)
    self.this_month_btn.setEnabled(True)
    self.add_walk_in_entry_btn.setEnabled(True)
    self.register_member_btn.setEnabled(True)
    self.add_equipment_btn.setEnabled(True)
    self.edit_equipment_btn.setEnabled(True)
    self.remove_equipment_btn.setEnabled(True)
    self.appoint_btn.setEnabled(True)
    self.cancel_schedule_btn.setEnabled(True)
    self.add_employee_btn.setEnabled(True)
    self.remove_employee_btn.setEnabled(True)
    self.add_trainer_btn.setEnabled(True)
    self.remove_trainer_btn.setEnabled(True)






