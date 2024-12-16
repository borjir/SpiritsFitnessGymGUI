import psycopg2
from PyQt5.QtWidgets import QDialog, QApplication, QHeaderView, QDesktopWidget, QGraphicsBlurEffect, QMessageBox

conn = psycopg2.connect(database="SpiritsFitnessGym",
                        user="postgres",
                        host='localhost',
                        password="postgres",
                        port=5432)
cur = conn.cursor()

def count_profit_data(self):
    pass
    sql_count_walk_in = "SELECT COUNT(entry_month_id) FROM entry_this_month WHERE entry_month_status = 'WALK-IN'"
    cur.execute(sql_count_walk_in)
    fetch_count_walk_in = cur.fetchone()
    fetch_count_walk_in = str(fetch_count_walk_in)
    fetch_count_walk_in = fetch_count_walk_in.replace("(", "")
    fetch_count_walk_in = fetch_count_walk_in.replace(")", "")
    fetch_count_walk_in = fetch_count_walk_in.replace(",", "")
    walk_in_sum = int(fetch_count_walk_in) * 25
    sql_count_member = "SELECT COUNT(entry_month_id) FROM entry_this_month WHERE entry_month_status = 'MEMBER'"
    cur.execute(sql_count_member)
    fetch_count_member = cur.fetchone()
    fetch_count_member = str(fetch_count_member)
    fetch_count_member = fetch_count_member.replace("(", "")
    fetch_count_member = fetch_count_member.replace(")", "")
    fetch_count_member = fetch_count_member.replace(",", "")
    member_sum = int(fetch_count_member) * 150
    total_profit = walk_in_sum + member_sum
    self.total_profit_home_label.setText("P" + str(total_profit) + ".00")
    conn.commit()
def count_entry_data(self):
    sql_count = "SELECT COUNT(entry_day_id) FROM entry_this_day"
    cur.execute(sql_count)
    fetch_count = cur.fetchone()
    fetch_count = str(fetch_count)
    fetch_count = fetch_count.replace("(", "")
    fetch_count = fetch_count.replace(")", "")
    fetch_count = fetch_count.replace(",", "")
    self.entry_daily_total_label.setText(fetch_count)
    conn.commit()

def delete_entry_data(self):
    sql_delete_day = "DELETE FROM entry_this_day WHERE CURRENT_DATE > entry_day_date"
    cur.execute(sql_delete_day)
    conn.commit()
    sql_delete_week = ("DELETE FROM entry_this_week WHERE EXTRACT(week FROM CURRENT_DATE::date) > EXTRACT(week FROM entry_week_date::date) "
                       "OR EXTRACT(year FROM CURRENT_DATE::date) > EXTRACT(year FROM entry_week_date::date)")
    cur.execute(sql_delete_week)
    conn.commit()
    sql_delete_month = ("DELETE FROM entry_this_month WHERE EXTRACT(month FROM CURRENT_DATE::date) > EXTRACT(month FROM entry_month_date::date) "
                       "OR EXTRACT(year FROM CURRENT_DATE::date) > EXTRACT(year FROM entry_month_date::date)")
    cur.execute(sql_delete_month)
    conn.commit()


def entry_main(self):
    first_name = self.walk_in_first_name_main_input.text()
    last_name = self.walk_in_last_name_main_input.text()
    first_name = first_name.upper()
    last_name = last_name.upper()
    sql_select = "SELECT entry_day_id FROM entry_this_day WHERE entry_day_fname = %s AND entry_day_lname = %s"
    data_select = (first_name, last_name,)
    cur.execute(sql_select, data_select)
    fetch_one = cur.fetchone()
    print(fetch_one)
    if first_name == "" or last_name == "":
        self.entry_main_error_notif.setText("Fill up first. Try again.")
        return 0
    else:
        if fetch_one == None:
            sql_insert_day = "INSERT INTO entry_this_day(entry_day_fname, entry_day_lname, entry_day_status) VALUES(%s, %s, 'WALK-IN')"
            data_insert = (first_name, last_name)
            cur.execute(sql_insert_day, data_insert)
            sql_update_day = "UPDATE entry_this_day SET entry_day_fullname = CONCAT(%s, ' ', %s) WHERE entry_day_fname = %s AND entry_day_lname = %s"
            data_update = (first_name, last_name, first_name, last_name)
            cur.execute(sql_update_day, data_update)
            sql_insert_week = "INSERT INTO entry_this_week(entry_week_fname, entry_week_lname, entry_week_status) VALUES(%s, %s, 'WALK-IN')"
            data_insert = (first_name, last_name)
            cur.execute(sql_insert_week, data_insert)
            sql_update_week = "UPDATE entry_this_week SET entry_week_fullname = CONCAT(%s, ' ', %s) WHERE entry_week_fname = %s AND entry_week_lname = %s"
            cur.execute(sql_update_week, data_update)
            sql_insert_month = "INSERT INTO entry_this_month(entry_month_fname, entry_month_lname, entry_month_status) VALUES(%s, %s, 'WALK-IN')"
            data_insert = (first_name, last_name)
            cur.execute(sql_insert_month, data_insert)
            sql_update_month = "UPDATE entry_this_month SET entry_month_fullname = CONCAT(%s, ' ', %s) WHERE entry_month_fname = %s AND entry_month_lname = %s"
            cur.execute(sql_update_month, data_update)
            return 1
        else:
            self.entry_main_error_notif.setText("Name already exists. Try again.")
            return 0






