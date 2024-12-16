from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsBlurEffect, QMessageBox, QAction, QHeaderView
from datetime import datetime, timedelta
import psycopg2

conn = psycopg2.connect(database="SpiritsFitnessGym",
                        user="postgres",
                        host='localhost',
                        password="postgres",
                        port=5432)
cur = conn.cursor()

def changePass(self):
    old_pw = self.oldPassword_input.text()
    new_pw = self.newPassword_input.text()
    confirm_pw = self.confirmPassword_input.text()
    sql_select_pw = "SELECT admin_password FROM admin WHERE admin_password = %s"
    data_insert = (old_pw,)
    cur.execute(sql_select_pw,data_insert)
    sql_fetch_pw = cur.fetchone()
    if sql_fetch_pw == None:
        self.changePass_error_label.setText("Invalid password. Try again.")
        return 0
    elif new_pw != confirm_pw:
        self.changePass_error_label.setText("Confirm password does not match. Try again.")
        return 0
    elif new_pw == "" and confirm_pw == "":
        self.changePass_error_label.setText("Fill up first. Try again.")
    elif len(new_pw) > 50:
        self.changePass_error_label.setText("You have reached the limit of 50 characters. Try again.")
    else:
        sql_update_pw = "UPDATE admin SET admin_password = %s WHERE admin_username = 'admin'"
        data_insert = (new_pw,)
        print('test')
        cur.execute(sql_update_pw,data_insert)
        conn.commit()
        return 1


