from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsBlurEffect, QMessageBox, QAction, QHeaderView
import psycopg2

conn = psycopg2.connect(database="SpiritsFitnessGym",
                        user="postgres",
                        host='localhost',
                        password="postgres",
                        port=5432)
cur = conn.cursor()

def login(self):
    username = self.username_input.text()
    password = self.password_input.text()
    sql_user_fetch = "SELECT admin_username, admin_password FROM admin WHERE admin_username = %s AND admin_password = %s"
    data_insert = (username, password)
    cur.execute(sql_user_fetch,data_insert)
    sql_fetch_data = cur.fetchone()
    if sql_fetch_data == None:
        self.login_error_label.setText("Invalid username or password. Try again.")
        return 0
    else:
        self.login_error_label.setText("")
        return 1
