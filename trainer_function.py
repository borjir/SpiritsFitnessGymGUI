from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsBlurEffect, QMessageBox, QAction, QHeaderView
import psycopg2

conn = psycopg2.connect(database="SpiritsFitnessGym",
                        user="postgres",
                        host='localhost',
                        password="postgres",
                        port=5432)
cur = conn.cursor()

def count_trainer_data(self):
    sql_count = "SELECT COUNT(trainer_id) FROM trainer"
    cur.execute(sql_count)
    fetch_count = cur.fetchone()
    fetch_count = str(fetch_count)
    fetch_count = fetch_count.replace("(", "")
    fetch_count = fetch_count.replace(")", "")
    fetch_count = fetch_count.replace(",", "")
    self.trainer_total_home_label.setText(fetch_count)
    self.trainer_total_main_label.setText(fetch_count)
    conn.commit()

def blur_add_trainer_components(self):
    blur_effect = QGraphicsBlurEffect()
    self.choose_trainer_blur_frame.setGraphicsEffect(blur_effect)
    if self.mem_or_emp_comboBox.isEnabled():
        self.choose_trainer_comboBox.setEnabled(False)
        self.confirm_add_trainer_btn.setEnabled(False)
    else:
        blur_effect.setEnabled(False)
        self.choose_trainer_comboBox.setEnabled(True)
        self.confirm_add_trainer_btn.setEnabled(True)

def trainer_option_confirm(self):
    self.mem_or_emp_comboBox.setEnabled(False)
    self.confirm_trainer_option_btn.setEnabled(False)

def add_trainer(self):
    name = self.choose_trainer_comboBox.currentText()
    name = name.upper()
    if name == "":
        pass
    else:
        sql_select_emp_id = "SELECT emp_id FROM employee WHERE emp_full_name = %s"
        data_select_name = (name,)
        cur.execute(sql_select_emp_id, data_select_name)
        fetch_one_emp_id = cur.fetchone()
        sql_insert_trainer = "INSERT INTO trainer(trainer_full_name, emp_id) VALUES(%s, %s)"
        data_insert = (name, fetch_one_emp_id)
        cur.execute(sql_insert_trainer, data_insert)
        conn.commit()
    return 1

def remove_trainer(self):
    name = self.remove_trainer_name_comboBox.currentText()
    sql_select_data = "SELECT trainer_id FROM trainer WHERE trainer_full_name = %s"
    data_insert = (name,)
    cur.execute(sql_select_data, data_insert)
    trainer_fetch_data = cur.fetchone()
    sql_select_session_data = "SELECT trainer_id FROM training_session WHERE trainer_id = %s"
    data_insert = (trainer_fetch_data,)
    cur.execute(sql_select_session_data, data_insert)
    trainer_session_fetch_data = cur.fetchone()
    if trainer_session_fetch_data == None:
        sql_delete_employee = "DELETE FROM trainer WHERE trainer_full_name = %s"
        data_delete = (name,)
        cur.execute(sql_delete_employee, data_delete)
        conn.commit()
        return 1
    else:
        self.remove_trainer_error_notif_1.setText("This trainer currently has")
        self.remove_trainer_error_notif_2.setText("a schedule. Try again.")
        return 0