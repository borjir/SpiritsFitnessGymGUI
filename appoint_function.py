from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsBlurEffect, QMessageBox, QAction, QHeaderView
from datetime import datetime, timedelta
import psycopg2

conn = psycopg2.connect(database="SpiritsFitnessGym",
                        user="postgres",
                        host='localhost',
                        password="postgres",
                        port=5432)
cur = conn.cursor()

def delete_session_data(self):
    sql_delete_duplicate_session_today = "DELETE FROM training_session_today"
    cur.execute(sql_delete_duplicate_session_today)
    sql_insert_session_today = ("INSERT INTO training_session_today(today_session_date, member_id, trainer_id) "
                              "SELECT session_date, member_id, trainer_id FROM training_session WHERE CURRENT_DATE >= session_date")
    cur.execute(sql_insert_session_today)
    sql_delete_session_today = "DELETE FROM training_session_today WHERE CURRENT_DATE > today_session_date"
    cur.execute(sql_delete_session_today)
    sql_delete_session = "DELETE FROM training_session WHERE CURRENT_DATE > session_date"
    cur.execute(sql_delete_session)
    conn.commit()
def count_session_data(self):
    sql_count = "SELECT COUNT(session_id) FROM training_session"
    cur.execute(sql_count)
    fetch_count = cur.fetchone()
    fetch_count = str(fetch_count)
    fetch_count = fetch_count.replace("(", "")
    fetch_count = fetch_count.replace(")", "")
    fetch_count = fetch_count.replace(",", "")
    self.training_session_total_label.setText(fetch_count)
    self.training_session_total_label.setText(fetch_count)
    conn.commit()

def blur_appoint_components(self):
    blur_effect = QGraphicsBlurEffect()
    self.blur_add_schedule_components.setGraphicsEffect(blur_effect)
    if self.choose_member_schedule_comboBox.isEnabled():
        self.choose_trainer_schedule_comboBox.setEnabled(False)
        self.choose_schedule_date_comboBox.setEnabled(False)
        self.confirm_appoint_main_btn.setEnabled(False)
    else:
        blur_effect.setEnabled(False)
        self.choose_trainer_schedule_comboBox.setEnabled(True)
        self.choose_schedule_date_comboBox.setEnabled(True)
        self.confirm_appoint_main_btn.setEnabled(True)
def member_name_main(self):
    self.choose_member_schedule_comboBox.setEnabled(False)
    self.confirm_choose_mem_name_btn.setEnabled(False)

def appoint_main(self):
    member_name = self.choose_member_schedule_comboBox.currentText()
    trainer_name = self.choose_trainer_schedule_comboBox.currentText()
    sched_date = self.choose_schedule_date_comboBox.currentText()
    mem_num = "SELECT member_id FROM member WHERE member_full_name = %s"
    data_insert = (member_name,)
    cur.execute(mem_num,data_insert)
    mem_id_fetch = cur.fetchone()
    trainer_num = "SELECT trainer_id FROM trainer WHERE trainer_full_name = %s"
    data_insert = (trainer_name,)
    cur.execute(trainer_num, data_insert)
    trainer_id_fetch = cur.fetchone()
    check_trainer_date = "SELECT session_date FROM training_session WHERE trainer_id = %s AND session_date IN(%s)"
    data_insert = (trainer_id_fetch,sched_date)
    cur.execute(check_trainer_date,data_insert)
    check_trainer_exist = cur.fetchone()
    if check_trainer_exist == None:
        sql_insert = ("INSERT INTO training_session(session_date, member_id, trainer_id) "
                      "VALUES(%s, %s, %s)")
        data_insert = (sched_date, mem_id_fetch, trainer_id_fetch)
        cur.execute(sql_insert, data_insert)
        conn.commit()
        return 1
    else:
        self.appoint_main_sched_label.setText("Trainer is occupied on this date. Try again.")
        return 0


def cancel_appoint_main(self):
    name = self.member_cancel_appoint_comboBox.currentText()
    sql_mem_num = "SELECT member_id FROM member WHERE member_full_name = %s"
    data_insert = (name,)
    cur.execute(sql_mem_num, data_insert)
    fetch_mem_id = cur.fetchone()
    sql_session_date = "SELECT session_date FROM training_session WHERE member_id = %s"
    cur.execute(sql_session_date, fetch_mem_id)
    fetch_session_date = cur.fetchone()

    sql_session_year = "SELECT EXTRACT('YEAR' FROM session_date) FROM training_session WHERE member_id = %s;"
    data_insert = (fetch_mem_id,)
    cur.execute(sql_session_year, data_insert)
    session_year = cur.fetchone()
    session_year = str(session_year)
    session_year = session_year.replace(")", "")
    session_year = session_year.replace("Decimal", "")
    session_year = session_year.replace("(", "")
    session_year = session_year.replace(",", "")
    session_year = session_year.replace("'", "")
    sql_session_month = "SELECT EXTRACT('MONTH' FROM session_date) FROM training_session WHERE member_id = %s;"
    data_insert = (fetch_mem_id,)
    cur.execute(sql_session_month, data_insert)
    session_month = cur.fetchone()
    session_month = str(session_month)
    session_month = session_month.replace(")", "")
    session_month = session_month.replace("Decimal", "")
    session_month = session_month.replace("(", "")
    session_month = session_month.replace(",", "")
    session_month = session_month.replace("'", "")
    sql_session_day = "SELECT EXTRACT('DAY' FROM session_date) FROM training_session WHERE member_id = %s;"
    data_insert = (fetch_mem_id,)
    cur.execute(sql_session_day, data_insert)
    session_day = cur.fetchone()
    session_day = str(session_day)
    session_day = session_day.replace(")", "")
    session_day = session_day.replace("Decimal", "")
    session_day = session_day.replace("(", "")
    session_day = session_day.replace(",", "")
    session_day = session_day.replace("'", "")
    sched_date = datetime(int(session_year), int(session_month), int(session_day))
    date_data = (sched_date.strftime("%Y-%m-%d"))
    str(date_data)
    sql_delete_session = "DELETE FROM training_session WHERE session_date = %s AND member_id = %s"
    data_insert = (date_data,fetch_mem_id)
    cur.execute(sql_delete_session,data_insert)
    conn.commit()
    return 1
