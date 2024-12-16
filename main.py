import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QDialog, QApplication, QHeaderView, QDesktopWidget, QGraphicsBlurEffect, QMessageBox
from PyQt5.uic import loadUi
from BlurWindow.blurWindow import blur
from PyQt5 import QtGui
from PyQt5.uic.properties import QtCore
from PyQt5.QtCore import QTimer,QTime,Qt
from datetime import datetime, timedelta
import customize
import login_function
import changePass_function
import entry_function
import member_function
import equipment_function
import appoint_function
import employee_function
import trainer_function
import psycopg2

conn = psycopg2.connect(database="SpiritsFitnessGym",
                        user="postgres",
                        host='localhost',
                        password="postgres",
                        port=5432)
cur = conn.cursor()


#MAIN / LOGIN TAB
class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("main_window.ui",self)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1)
        #customize home page
        widget.setMinimumSize(1000, 800)
        customize.main_home_customize(self)
        customize.date_current_home(self)
        #buttons
        self.stackedWidget.setCurrentIndex(0)
        self.toggle_btn.clicked.connect(self.toggled)
        self.home_btn.clicked.connect(self.home_page)
        self.entry_btn.clicked.connect(self.entry_page)
        self.member_btn.clicked.connect(self.member_page)
        self.equipment_btn.clicked.connect(self.equipment_page)
        self.schedule_btn.clicked.connect(self.schedule_page)
        self.emp_btn.clicked.connect(self.employee_page)
        self.trainer_btn.clicked.connect(self.trainer_page)
        self.logout_btn.clicked.connect(self.logoutFunction)
        self.home_btn.setChecked(True)

#----------------------------ENTRY FUNCS--------------------------------------
        self.add_walk_in_entry_btn.clicked.connect(self.add_walk_in)
        self.confirm_add_walk_in_main_btn.clicked.connect(self.entry_main_confirm)
        self.cancel_add_walk_in_main_btn.clicked.connect(self.entry_main_cancel)
        #update
        entry_function.delete_entry_data(self)
        entry_function.count_entry_data(self)
        entry_function.count_profit_data(self)
#----------------------------MEMBER FUNCS--------------------------------------
        self.register_member_btn.clicked.connect(self.register_member)
        self.confirm_register_member_main_btn.clicked.connect(self.member_main_confirm)
        self.cancel_register_member_main_btn.clicked.connect(self.member_main_cancel)
        #update
        member_function.delete_member_data(self)
        member_function.count_member_data(self)
#----------------------------EQUIPMENT FUNCS------------------------------------
        #update
        equipment_function.count_equipment_data(self)
        #confirm
        self.add_equipment_btn.clicked.connect(self.add_equipment)
        self.confirm_add_equipment_main_btn.clicked.connect(self.add_equipment_main_confirm)
        self.cancel_add_equipment_main_btn.clicked.connect(self.add_equipment_main_cancel)
        #eedit
        self.edit_equipment_btn.clicked.connect(self.edit_equipment)
        self.confirm_equipment_id_main_btn.clicked.connect(self.equipment_id_main_confirm)
        self.add_equipment_amount_btn.clicked.connect(self.add_equipment_amount_main_confirm)
        self.deduct_equipment_amount_btn.clicked.connect(self.deduct_equipment_amount_main_confirm)
        self.confirm_edit_equipment_main_btn.clicked.connect(self.edit_equipment_main_confirm)
        self.cancel_edit_equipment_main_btn.clicked.connect(self.edit_equipment_main_cancel)
        #remove
        self.remove_equipment_btn.clicked.connect(self.remove_equipment)
        self.confirm_remove_equipment_btn.clicked.connect(self.remove_equipment_main_confirm)
        self.cancel_remove_equipment_btn.clicked.connect(self.remove_equipment_main_cancel)
#--------------------------------APPOINT FUNCS----------------------------------------------
        #update
        appoint_function.count_session_data(self)
        appoint_function.delete_session_data(self)
        #appoint
        self.appoint_btn.clicked.connect(self.appoint)
        self.confirm_choose_mem_name_btn.clicked.connect(self.member_name_main_confirm)
        self.confirm_appoint_main_btn.clicked.connect(self.appoint_main_confirm)
        self.cancel_appoint_main_btn.clicked.connect(self.appoint_main_cancel)
        #cancel
        self.cancel_schedule_btn.clicked.connect(self.cancel_schedule)
        self.confirm_appoint_cancel_btn.clicked.connect(self.cancel_appoint_confirm)
        self.cancel_appoint_cancel_btn.clicked.connect(self.cancel_appoint_cancel)
#------------------------------EMPLOYEE FUNCS-----------------------------------------------
        # update
        employee_function.count_employee_data(self)
        #add
        self.add_employee_btn.clicked.connect(self.add_employee)
        self.confirm_add_employee_btn.clicked.connect(self.add_employee_confirm)
        self.cancel_add_employee_btn.clicked.connect(self.add_employee_cancel)
        #remove
        self.remove_employee_btn.clicked.connect(self.remove_employee)
        self.confirm_remove_employee_btn.clicked.connect(self.remove_employee_confirm)
        self.cancel_remove_employee_btn.clicked.connect(self.remove_employee_cancel)

# ------------------------------TRAINER FUNCS-----------------------------------------------
        #update
        trainer_function.count_trainer_data(self)
        #add
        self.add_trainer_btn.clicked.connect(self.add_trainer)
        self.confirm_add_trainer_btn.clicked.connect(self.add_trainer_confirm)
        self.cancel_add_trainer_btn.clicked.connect(self.add_trainer_cancel)
        #remove
        self.remove_trainer_btn.clicked.connect(self.remove_trainer)
        self.confirm_remove_trainer_btn.clicked.connect(self.remove_trainer_confirm)
        self.cancel_remove_trainer_btn.clicked.connect(self.remove_trainer_cancel)

    def showTime(self):
        currentTime = QTime.currentTime()
        display_Txt = currentTime.toString("hh:mm:ss")
        self.time_label.setText(display_Txt)
    def toggled(self):
        customize.toggled(self)
#--------------------------------------------------------------------------------------------------------------
#================================================================================================================
    def home_page(self):
        self.stackedWidget.setCurrentIndex(0)

#-------------------------------ENTRY PAGE---------------------------------------------------------------------------
# ================================================================================================================
    def entry_page(self):
        self.stackedWidget.setCurrentIndex(1)
        self.entry_logs_widget.setCurrentIndex(0)
        customize.main_entry_customize(self)
        customize.this_day(self)
        entry_function.count_profit_data(self)
        self.this_day_btn.clicked.connect(self.this_day)
        self.this_day_btn.setChecked(True)
        self.this_week_btn.clicked.connect(self.this_week)
        self.this_month_btn.clicked.connect(self.this_month)

        this_day_table = "select entry_day_fullname, entry_day_date, DATE_TRUNC('second', entry_day_time), entry_day_status from entry_this_day ORDER BY entry_day_id"
        cur.execute(this_day_table)
        fetch_this_day_table = cur.fetchall()
        self.this_day_tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(fetch_this_day_table):
            self.this_day_tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.this_day_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        this_week_table = "select entry_week_fullname, entry_week_date, DATE_TRUNC('second', entry_week_time), entry_week_status from entry_this_week ORDER BY entry_week_id"
        cur.execute(this_week_table)
        fetch_this_week_table = cur.fetchall()
        self.this_week_tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(fetch_this_week_table):
            self.this_week_tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.this_week_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        this_month_table = "select entry_month_fullname, entry_month_date, DATE_TRUNC('second', entry_month_time), entry_month_status from entry_this_month ORDER BY entry_month_id"
        cur.execute(this_month_table)
        fetch_this_month_table = cur.fetchall()
        self.this_month_tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(fetch_this_month_table):
            self.this_month_tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.this_month_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def this_day(self):
        self.entry_logs_widget.setCurrentIndex(0)

    def this_week(self):
        self.entry_logs_widget.setCurrentIndex(1)
        customize.this_week(self)

    def this_month(self):
        self.entry_logs_widget.setCurrentIndex(2)
        customize.this_month(self)

    def add_walk_in(self):
        customize.disable_components(self)
        customize.entry_sideFrame(self)

    def entry_main_confirm(self):
        n = entry_function.entry_main(self)
        if n == 1:
            customize.enable_components(self)
            customize.entry_sideFrame(self)
            customize.main_entry_customize(self)
            entry_function.delete_entry_data(self)
            entry_function.count_entry_data(self)
            self.walk_in_first_name_main_input.setText("")
            self.walk_in_last_name_main_input.setText("")
            self.entry_main_error_notif.setText("")
            entry_function.count_profit_data(self)
            this_day_table = "select entry_day_fullname, entry_day_date, DATE_TRUNC('second', entry_day_time), entry_day_status from entry_this_day ORDER BY entry_day_id"
            cur.execute(this_day_table)
            fetch_this_day_table = cur.fetchall()
            self.this_day_tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(fetch_this_day_table):
                self.this_day_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.this_day_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            this_week_table = "select entry_week_fullname, entry_week_date, DATE_TRUNC('second', entry_week_time), entry_week_status from entry_this_week ORDER BY entry_week_id"
            cur.execute(this_week_table)
            fetch_this_week_table = cur.fetchall()
            self.this_week_tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(fetch_this_week_table):
                self.this_week_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.this_week_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            this_month_table = "select entry_month_fullname, entry_month_date, DATE_TRUNC('second', entry_month_time), entry_month_status from entry_this_month ORDER BY entry_month_id"
            cur.execute(this_month_table)
            fetch_this_month_table = cur.fetchall()
            self.this_month_tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(fetch_this_month_table):
                self.this_month_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.this_month_tableWidget.setItem(row_number, column_number,
                                                        QtWidgets.QTableWidgetItem(str(data)))

    def entry_main_cancel(self):
        customize.enable_components(self)
        customize.entry_sideFrame(self)
        customize.main_entry_customize(self)
        self.walk_in_first_name_main_input.setText("")
        self.walk_in_last_name_main_input.setText("")
        self.entry_main_error_notif.setText("")


#--------------------------------------MEMBER PAGE-------------------------------------------------------------------
# ================================================================================================================
    def member_page(self):
        self.stackedWidget.setCurrentIndex(2)
        customize.main_member_customize(self)
        member_table = "select member_id, member_full_name, member_start_date, member_end_date from member ORDER BY member_id"
        cur.execute(member_table)
        fetch_member_table = cur.fetchall()
        self.member_tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(fetch_member_table):
            self.member_tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.member_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        expired_member_table = "select member_full_name from expired_member NATURAL JOIN member ORDER BY member_id"
        cur.execute(expired_member_table)
        fetch_expired_member_table = cur.fetchall()
        self.expired_mem_tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(fetch_expired_member_table):
            self.expired_mem_tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.expired_mem_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def register_member(self):
        customize.disable_components(self)
        customize.member_sideFrame(self)

    def member_main_confirm(self):
        n = member_function.member_main(self)
        if n == 1:
            customize.enable_components(self)
            customize.member_sideFrame(self)
            customize.main_member_customize(self)
            entry_function.delete_entry_data(self)
            entry_function.count_entry_data(self)
            member_function.delete_member_data(self)
            member_function.count_member_data(self)
            entry_function.count_profit_data(self)
            self.member_first_name_main_input.setText("")
            self.member_last_name_main_input.setText("")
            self.member_main_error_notif.setText("")
            member_table = "select member_id, member_full_name, member_start_date, member_end_date from member ORDER BY member_id"
            cur.execute(member_table)
            fetch_member_table = cur.fetchall()
            self.member_tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(fetch_member_table):
                self.member_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.member_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            expired_member_table = "select member_full_name from expired_member NATURAL JOIN member ORDER BY member_id"
            cur.execute(expired_member_table)
            fetch_expired_member_table = cur.fetchall()
            self.expired_mem_tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(fetch_expired_member_table):
                self.expired_mem_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.expired_mem_tableWidget.setItem(row_number, column_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

    def member_main_cancel(self):
        customize.enable_components(self)
        customize.member_sideFrame(self)
        customize.main_member_customize(self)
        self.member_first_name_main_input.setText("")
        self.member_last_name_main_input.setText("")
        self.member_main_error_notif.setText("")


#-------------------------------EQUIPMENT PAGE-----------------------------------------------------------------------
# ================================================================================================================
    def equipment_page(self):
        self.stackedWidget.setCurrentIndex(3)
        customize.main_equipment_customize(self)
        equipment_table = "select equipment_id, equipment_name, equipment_qty, equipment_status, equipment_date_added from equipment ORDER BY equipment_id"
        cur.execute(equipment_table)
        fetch_equipment_table = cur.fetchall()
        self.equipment_tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(fetch_equipment_table):
            self.equipment_tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.equipment_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    # ------------------------------------------------------------------------------
    def add_equipment(self):
        self.equipment_stackedWidget.setCurrentIndex(0)
        customize.disable_components(self)
        customize.equipment_sideFrame(self)

    def add_equipment_main_confirm(self):
        n = equipment_function.add_equipment_main(self)
        if n == 1:
            customize.enable_components(self)
            customize.equipment_sideFrame(self)
            customize.main_equipment_customize(self)
            equipment_function.count_equipment_data(self)
            self.equipment_add_name_input.setText("")
            self.equipment_add_qty_input.setText("")
            self.add_equipment_main_error_notif.setText("")
            equipment_table = "select equipment_id, equipment_name, equipment_qty, equipment_status, equipment_date_added from equipment ORDER BY equipment_id"
            cur.execute(equipment_table)
            fetch_equipment_table = cur.fetchall()
            self.equipment_tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(fetch_equipment_table):
                self.equipment_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.equipment_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def add_equipment_main_cancel(self):
        customize.enable_components(self)
        customize.equipment_sideFrame(self)
        customize.main_equipment_customize(self)
        self.equipment_add_name_input.setText("")
        self.equipment_add_qty_input.setText("")
        self.add_equipment_main_error_notif.setText("")

    # ------------------------------------------------------------------------------
    def edit_equipment(self):
        cur.execute("select equipment_name from equipment ORDER BY equipment_name")
        equipment_edit_list = cur.fetchall()
        conn.commit()
        equipment_edit_list_string = [item[0] for item in equipment_edit_list]
        self.equipment_edit_name_comboBox.clear()
        self.equipment_edit_name_comboBox.addItems(equipment_edit_list_string)
        check_equipment_name = self.equipment_edit_name_comboBox.currentText()
        if check_equipment_name == "":
            dialog = QMessageBox(self)
            dialog.setWindowTitle('Warning')
            dialog.setText('\nThere is no equipment available.')
            dialog.setStyleSheet("QMessageBox{background-color: white;}"
                                 "QLabel{border-color: white;font: bold 20px Arial, serif;color: #037a28;}"
                                 "QPushButton{padding: 5px 40px 5px 40px;border-color: #FF3E3F;background-color: #ff3e3f;color: rgb(255, 255, 255);border-radius: 10px;font: bold 20px Arial, serif;cursor: grab;}"
                                 "QPushButton:hover{border-color:#cc3132;background-color: #cc3132;}")
            dialog.show()
        else:
            self.equipment_stackedWidget.setCurrentIndex(1)
            customize.disable_components(self)
            customize.equipment_sideFrame(self)
            equipment_function.blur_edit_equipment_components(self)

    def equipment_id_main_confirm(self):
        equipment_function.equipment_id_main(self)
        equipment_function.blur_edit_equipment_components(self)
        equipment_function.equipment_qty_data(self)

    def add_equipment_amount_main_confirm(self):
        equipment_function.add_equipment_amount_main(self)

    def deduct_equipment_amount_main_confirm(self):
        equipment_function.deduct_equipment_amount_main(self)

    def edit_equipment_main_confirm(self):
        n = equipment_function.edit_equipment_main(self)
        if n == 1:
            customize.enable_components(self)
            customize.equipment_sideFrame(self)
            customize.main_equipment_customize(self)
            equipment_function.count_equipment_data(self)
            self.equipment_edit_qty_input.setText("")
            self.equipment_current_qty_label.setText("")
            self.edit_equipment_main_error_notif.setText("")
            self.equipment_edit_name_comboBox.setEnabled(True)
            self.confirm_equipment_id_main_btn.setEnabled(True)
            self.equipment_edit_status_input.clear()
            equipment_table = "select equipment_id, equipment_name, equipment_qty, equipment_status, equipment_date_added from equipment ORDER BY equipment_id"
            cur.execute(equipment_table)
            fetch_equipment_table = cur.fetchall()
            self.equipment_tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(fetch_equipment_table):
                self.equipment_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.equipment_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def edit_equipment_main_cancel(self):
        customize.enable_components(self)
        customize.equipment_sideFrame(self)
        customize.main_equipment_customize(self)
        self.equipment_edit_qty_input.setText("")
        self.equipment_current_qty_label.setText("")
        self.edit_equipment_main_error_notif.setText("")
        self.equipment_edit_name_comboBox.setEnabled(True)
        self.confirm_equipment_id_main_btn.setEnabled(True)
        self.equipment_edit_status_input.clear()

    # ------------------------------------------------------------------------------
    def remove_equipment(self):
        cur.execute("select equipment_name from equipment ORDER BY equipment_name")
        equipment_remove_list = cur.fetchall()
        conn.commit()
        equipment_remove_list_string = [item[0] for item in equipment_remove_list]
        self.remove_equipment_comboBox.clear()
        self.remove_equipment_comboBox.addItems(equipment_remove_list_string)
        check_name = self.remove_equipment_comboBox.currentText()
        if check_name == "":
            dialog = QMessageBox(self)
            dialog.setWindowTitle('Warning')
            dialog.setText('\nThere is no equipment available.')
            dialog.setStyleSheet("QMessageBox{background-color: white;}"
                                 "QLabel{border-color: white;font: bold 20px Arial, serif;color: #037a28;}"
                                 "QPushButton{padding: 5px 40px 5px 40px;border-color: #FF3E3F;background-color: #ff3e3f;color: rgb(255, 255, 255);border-radius: 10px;font: bold 20px Arial, serif;cursor: grab;}"
                                 "QPushButton:hover{border-color:#cc3132;background-color: #cc3132;}")
            dialog.show()
        else:
            self.equipment_stackedWidget.setCurrentIndex(2)
            customize.disable_components(self)
            customize.equipment_sideFrame(self)

    def remove_equipment_main_confirm(self):
        n = equipment_function.remove_equipment_main(self)
        if n == 1:
            customize.enable_components(self)
            customize.equipment_sideFrame(self)
            customize.main_equipment_customize(self)
            equipment_function.count_equipment_data(self)
            self.remove_equipment_comboBox.clear()
            equipment_table = "select equipment_id, equipment_name, equipment_qty, equipment_status, equipment_date_added from equipment ORDER BY equipment_id"
            cur.execute(equipment_table)
            fetch_equipment_table = cur.fetchall()
            self.equipment_tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(fetch_equipment_table):
                self.equipment_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.equipment_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def remove_equipment_main_cancel(self):
        customize.enable_components(self)
        customize.equipment_sideFrame(self)
        customize.main_equipment_customize(self)


#---------------------------------SCHEDULE PAGE------------------------------------------------------------------------
# ================================================================================================================
    def schedule_page(self):
        self.stackedWidget.setCurrentIndex(4)
        customize.main_schedule_customize(self)
        schedule_table = "select session_id, member_full_name, trainer_full_name, session_date from training_session NATURAL JOIN member NATURAL JOIN trainer"
        cur.execute(schedule_table)
        fetch_schedule_table = cur.fetchall()
        self.session_tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(fetch_schedule_table):
            self.session_tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.session_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        today_schedule_table = "select member_full_name from training_session_today NATURAL JOIN member ORDER BY member_id"
        cur.execute(today_schedule_table)
        fetch_today_schedule_table = cur.fetchall()
        self.mem_session_today_tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(fetch_today_schedule_table):
            self.mem_session_today_tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.mem_session_today_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    #------------------------------------------------------------------------------
    def appoint(self):
        cur.execute("select member.member_full_name from member "
                    "WHERE NOT EXISTS(SELECT training_session.session_id FROM training_session"
                    " WHERE training_session.member_id = member.member_id) ORDER BY member.member_full_name")
        member_add_list = cur.fetchall()
        member_add_list_string = [item[0] for item in member_add_list]
        self.choose_member_schedule_comboBox.clear()
        self.choose_member_schedule_comboBox.addItems(member_add_list_string)
        cur.execute("SELECT trainer_full_name from trainer")
        trainer_add_list = cur.fetchone()
        check_name_member = self.choose_member_schedule_comboBox.currentText()
        if check_name_member == "" and trainer_add_list == None:
            dialog = QMessageBox(self)
            dialog.setWindowTitle('Warning')
            dialog.setText('\nThere are no members and trainers available.')
            dialog.setStyleSheet("QMessageBox{background-color: white;}"
                                 "QLabel{border-color: white;font: bold 20px Arial, serif;color: #037a28;}"
                                 "QPushButton{padding: 5px 40px 5px 40px;border-color: #FF3E3F;background-color: #ff3e3f;color: rgb(255, 255, 255);border-radius: 10px;font: bold 20px Arial, serif;cursor: grab;}"
                                 "QPushButton:hover{border-color:#cc3132;background-color: #cc3132;}")
            dialog.show()
        elif check_name_member == "":
            dialog = QMessageBox(self)
            dialog.setWindowTitle('Warning')
            dialog.setText('\nThere are no members available.')
            dialog.setStyleSheet("QMessageBox{background-color: white;}"
                                 "QLabel{border-color: white;font: bold 20px Arial, serif;color: #037a28;}"
                                 "QPushButton{padding: 5px 40px 5px 40px;border-color: #FF3E3F;background-color: #ff3e3f;color: rgb(255, 255, 255);border-radius: 10px;font: bold 20px Arial, serif;cursor: grab;}"
                                 "QPushButton:hover{border-color:#cc3132;background-color: #cc3132;}")
            dialog.show()
        elif trainer_add_list == None:
            dialog = QMessageBox(self)
            dialog.setWindowTitle('Warning')
            dialog.setText('\nThere are no trainers available.')
            dialog.setStyleSheet("QMessageBox{background-color: white;}"
                                 "QLabel{border-color: white;font: bold 20px Arial, serif;color: #037a28;}"
                                 "QPushButton{padding: 5px 40px 5px 40px;border-color: #FF3E3F;background-color: #ff3e3f;color: rgb(255, 255, 255);border-radius: 10px;font: bold 20px Arial, serif;cursor: grab;}"
                                 "QPushButton:hover{border-color:#cc3132;background-color: #cc3132;}")
            dialog.show()
        else:
            self.schedule_stackedWidget.setCurrentIndex(0)
            customize.disable_components(self)
            customize.schedule_sideFrame(self)
            appoint_function.blur_appoint_components(self)

    def member_name_main_confirm(self):
        appoint_function.member_name_main(self)
        appoint_function.blur_appoint_components(self)
        cur.execute("SELECT trainer_full_name from trainer")
        trainer_add_list = cur.fetchall()
        conn.commit()
        trainer_add_list_string = [item[0] for item in trainer_add_list]
        self.choose_trainer_schedule_comboBox.clear()
        self.choose_trainer_schedule_comboBox.addItems(trainer_add_list_string)
        cur.execute("SELECT EXTRACT('Year' FROM CURRENT_DATE);")
        year_current = cur.fetchone()
        year_current = str(year_current)
        year_current = year_current.replace(")", "")
        year_current = year_current.replace("Decimal", "")
        year_current = year_current.replace("(", "")
        year_current = year_current.replace(",", "")
        year_current = year_current.replace("'", "")
        cur.execute("SELECT EXTRACT('Month' FROM CURRENT_DATE);")
        month_current = cur.fetchone()
        month_current = str(month_current)
        month_current = month_current.replace(")", "")
        month_current = month_current.replace("Decimal", "")
        month_current = month_current.replace("(", "")
        month_current = month_current.replace(",", "")
        month_current = month_current.replace("'", "")
        cur.execute("SELECT EXTRACT('Day' FROM CURRENT_DATE);")
        day_current = cur.fetchone()
        day_current = str(day_current)
        day_current = day_current.replace(")", "")
        day_current = day_current.replace("Decimal", "")
        day_current = day_current.replace("(", "")
        day_current = day_current.replace(",", "")
        day_current = day_current.replace("'", "")
        name = self.choose_member_schedule_comboBox.currentText()
        sql_mem_year = "SELECT EXTRACT('YEAR' FROM member_end_date) FROM member WHERE member_full_name = %s;"
        data_insert = (name,)
        cur.execute(sql_mem_year, data_insert)
        mem_year = cur.fetchone()
        mem_year = str(mem_year)
        mem_year = mem_year.replace(")", "")
        mem_year = mem_year.replace("Decimal", "")
        mem_year = mem_year.replace("(", "")
        mem_year = mem_year.replace(",", "")
        mem_year = mem_year.replace("'", "")
        sql_mem_month = "SELECT EXTRACT('MONTH' FROM member_end_date) FROM member WHERE member_full_name = %s;"
        data_insert = (name,)
        cur.execute(sql_mem_month, data_insert)
        mem_month = cur.fetchone()
        mem_month = str(mem_month)
        mem_month = mem_month.replace(")", "")
        mem_month = mem_month.replace("Decimal", "")
        mem_month = mem_month.replace("(", "")
        mem_month = mem_month.replace(",", "")
        mem_month = mem_month.replace("'", "")
        sql_mem_day = "SELECT EXTRACT('DAY' FROM member_end_date) FROM member WHERE member_full_name = %s;"
        data_insert = (name,)
        cur.execute(sql_mem_day, data_insert)
        mem_day = cur.fetchone()
        mem_day = str(mem_day)
        mem_day = mem_day.replace(")", "")
        mem_day = mem_day.replace("Decimal", "")
        mem_day = mem_day.replace("(", "")
        mem_day = mem_day.replace(",", "")
        mem_day = mem_day.replace("'", "")
        start_date = datetime(int(year_current), int(month_current), int(day_current)+1)
        end_date = datetime(int(mem_year), int(mem_month), int(mem_day)-1)
        sched_date = start_date
        while sched_date <= end_date:
            self.choose_schedule_date_comboBox.addItem(sched_date.strftime("%Y-%m-%d"))
            sched_date += timedelta(days=1)

    def appoint_main_confirm(self):
        n = appoint_function.appoint_main(self)
        if n == 1:
            customize.enable_components(self)
            customize.schedule_sideFrame(self)
            customize.main_schedule_customize(self)
            appoint_function.delete_session_data(self)
            self.choose_member_schedule_comboBox.setEnabled(True)
            self.confirm_choose_mem_name_btn.setEnabled(True)
            self.choose_member_schedule_comboBox.clear()
            self.choose_trainer_schedule_comboBox.clear()
            self.choose_schedule_date_comboBox.clear()
            self.appoint_main_sched_label.setText("")
            appoint_function.count_session_data(self)
            schedule_table = "select session_id, member_full_name, trainer_full_name, session_date from training_session NATURAL JOIN member NATURAL JOIN trainer"
            cur.execute(schedule_table)
            fetch_schedule_table = cur.fetchall()
            self.session_tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(fetch_schedule_table):
                self.session_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.session_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            today_schedule_table = "select member_full_name from training_session_today NATURAL JOIN member ORDER BY member_id"
            cur.execute(today_schedule_table)
            fetch_today_schedule_table = cur.fetchall()
            self.mem_session_today_tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(fetch_today_schedule_table):
                self.mem_session_today_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.mem_session_today_tableWidget.setItem(row_number, column_number,
                                                               QtWidgets.QTableWidgetItem(str(data)))


    def appoint_main_cancel(self):
        customize.enable_components(self)
        customize.schedule_sideFrame(self)
        customize.main_schedule_customize(self)
        self.choose_member_schedule_comboBox.setEnabled(True)
        self.confirm_choose_mem_name_btn.setEnabled(True)
        self.choose_member_schedule_comboBox.clear()
        self.choose_trainer_schedule_comboBox.clear()
        self.choose_schedule_date_comboBox.clear()
        self.appoint_main_sched_label.setText("")

    # ------------------------------------------------------------------------------
    def cancel_schedule(self):
        cur.execute("SELECT member_full_name from member NATURAL JOIN training_session")
        member_remove_list = cur.fetchall()
        conn.commit()
        member_remove_list_string = [item[0] for item in member_remove_list]
        self.member_cancel_appoint_comboBox.clear()
        self.member_cancel_appoint_comboBox.addItems(member_remove_list_string)
        check_name = self.member_cancel_appoint_comboBox.currentText()
        if check_name == "":
            dialog = QMessageBox(self)
            dialog.setWindowTitle('Warning')
            dialog.setText('\nThere are no schedules available.')
            dialog.setStyleSheet("QMessageBox{background-color: white;}"
                                 "QLabel{border-color: white;font: bold 20px Arial, serif;color: #037a28;}"
                                 "QPushButton{padding: 5px 40px 5px 40px;border-color: #FF3E3F;background-color: #ff3e3f;color: rgb(255, 255, 255);border-radius: 10px;font: bold 20px Arial, serif;cursor: grab;}"
                                 "QPushButton:hover{border-color:#cc3132;background-color: #cc3132;}")
            dialog.show()
        else:
            self.schedule_stackedWidget.setCurrentIndex(1)
            customize.disable_components(self)
            customize.schedule_sideFrame(self)


    def cancel_appoint_confirm(self):
        n = appoint_function.cancel_appoint_main(self)
        if n == 1:
            customize.enable_components(self)
            customize.schedule_sideFrame(self)
            customize.main_schedule_customize(self)
            appoint_function.delete_session_data(self)
            self.member_cancel_appoint_comboBox.clear()
            schedule_table = "select session_id, member_full_name, trainer_full_name, session_date from training_session NATURAL JOIN member NATURAL JOIN trainer"
            cur.execute(schedule_table)
            fetch_schedule_table = cur.fetchall()
            self.session_tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(fetch_schedule_table):
                self.session_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.session_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            today_schedule_table = "select member_full_name from training_session_today NATURAL JOIN member ORDER BY member_id"
            cur.execute(today_schedule_table)
            fetch_today_schedule_table = cur.fetchall()
            self.mem_session_today_tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(fetch_today_schedule_table):
                self.mem_session_today_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.mem_session_today_tableWidget.setItem(row_number, column_number,
                                                               QtWidgets.QTableWidgetItem(str(data)))

    def cancel_appoint_cancel(self):
        customize.enable_components(self)
        customize.schedule_sideFrame(self)
        customize.main_schedule_customize(self)
        self.member_cancel_appoint_comboBox.clear()

# ---------------------------------EMPLOYEE PAGE------------------------------------------------------------------------
# ================================================================================================================
    def employee_page(self):
        self.stackedWidget.setCurrentIndex(5)
        customize.main_employee_customize(self)
        employee_table = "select emp_id, emp_full_name, emp_phone_num, emp_date_employed from employee"
        cur.execute(employee_table)
        fetch_employee_table = cur.fetchall()
        self.employee_tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(fetch_employee_table):
            self.employee_tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.employee_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def add_employee(self):
        self.employee_stackedWidget.setCurrentIndex(0)
        customize.disable_components(self)
        customize.employee_sideFrame(self)

    def add_employee_confirm(self):
        n = employee_function.add_employee(self)
        if n == 1:
            customize.enable_components(self)
            customize.employee_sideFrame(self)
            customize.main_employee_customize(self)
            employee_function.count_employee_data(self)
            self.employee_first_name_main_input.setText("")
            self.employee_last_name_main_input.setText("")
            self.employee_phone_num_input.setText("")
            self.add_employee_main_error_notif.setText("")
            employee_table = "select emp_id, emp_full_name, emp_phone_num, emp_date_employed from employee"
            cur.execute(employee_table)
            fetch_employee_table = cur.fetchall()
            print(fetch_employee_table)
            self.employee_tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(fetch_employee_table):
                self.employee_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.employee_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def add_employee_cancel(self):
        customize.enable_components(self)
        customize.employee_sideFrame(self)
        customize.main_employee_customize(self)
        self.employee_first_name_main_input.setText("")
        self.employee_last_name_main_input.setText("")
        self.employee_phone_num_input.setText("")
        self.add_employee_main_error_notif.setText("")

    def remove_employee(self):
        cur.execute("select emp_full_name from employee ORDER BY emp_full_name")
        employee_remove_list = cur.fetchall()
        conn.commit()
        employee_remove_list_string = [item[0] for item in employee_remove_list]
        self.remove_employee_name_comboBox.clear()
        self.remove_employee_name_comboBox.addItems(employee_remove_list_string)
        check_name = self.remove_employee_name_comboBox.currentText()
        if check_name == "":
            dialog = QMessageBox(self)
            dialog.setWindowTitle('Warning')
            dialog.setText('\nThere are no employees available.')
            dialog.setStyleSheet("QMessageBox{background-color: white;}"
                                 "QLabel{border-color: white;font: bold 20px Arial, serif;color: #037a28;}"
                                 "QPushButton{padding: 5px 40px 5px 40px;border-color: #FF3E3F;background-color: #ff3e3f;color: rgb(255, 255, 255);border-radius: 10px;font: bold 20px Arial, serif;cursor: grab;}"
                                 "QPushButton:hover{border-color:#cc3132;background-color: #cc3132;}")
            dialog.show()
        else:
            self.employee_stackedWidget.setCurrentIndex(1)
            customize.disable_components(self)
            customize.employee_sideFrame(self)

    def remove_employee_confirm(self):
        n = employee_function.remove_employee(self)
        if n == 1:
            customize.enable_components(self)
            customize.employee_sideFrame(self)
            customize.main_employee_customize(self)
            employee_function.count_employee_data(self)
            self.remove_employee_error_notif_1.setText("")
            self.remove_employee_error_notif_2.setText("")
            employee_table = "select emp_id, emp_full_name, emp_phone_num, emp_date_employed from employee"
            cur.execute(employee_table)
            fetch_employee_table = cur.fetchall()
            print(fetch_employee_table)
            self.employee_tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(fetch_employee_table):
                self.employee_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.employee_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def remove_employee_cancel(self):
        customize.enable_components(self)
        customize.employee_sideFrame(self)
        customize.main_employee_customize(self)
        self.remove_employee_name_comboBox.clear()
        self.remove_employee_error_notif_1.setText("")
        self.remove_employee_error_notif_2.setText("")


# ---------------------------------TRAINER PAGE------------------------------------------------------------------------
# ================================================================================================================

    def trainer_page(self):
        self.stackedWidget.setCurrentIndex(6)
        customize.main_trainer_customize(self)
        trainer_table = "select trainer_id, trainer_full_name, trainer_date_hired, emp_id from trainer"
        cur.execute(trainer_table)
        fetch_trainer_table = cur.fetchall()
        print(fetch_trainer_table)
        self.trainer_tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(fetch_trainer_table):
            self.trainer_tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.trainer_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


    def add_trainer(self):
        cur.execute("select employee.emp_full_name from employee "
                    "WHERE NOT EXISTS(SELECT trainer.emp_id FROM trainer WHERE trainer.emp_id = employee.emp_id) ORDER BY employee.emp_full_name")
        trainer_add_list = cur.fetchall()
        conn.commit()
        trainer_add_list_string = [item[0] for item in trainer_add_list]
        self.choose_trainer_comboBox.clear()
        self.choose_trainer_comboBox.addItems(trainer_add_list_string)
        check_name = self.choose_trainer_comboBox.currentText()
        if check_name == "":
            dialog = QMessageBox(self)
            dialog.setWindowTitle('Warning')
            dialog.setText('\nThere are no trainers available.')
            dialog.setStyleSheet("QMessageBox{background-color: white;}"
                                 "QLabel{border-color: white;font: bold 20px Arial, serif;color: #037a28;}"
                                 "QPushButton{padding: 5px 40px 5px 40px;border-color: #FF3E3F;background-color: #ff3e3f;color: rgb(255, 255, 255);border-radius: 10px;font: bold 20px Arial, serif;cursor: grab;}"
                                 "QPushButton:hover{border-color:#cc3132;background-color: #cc3132;}")
            dialog.show()
        else:
            self.trainer_stackedWidget.setCurrentIndex(0)
            customize.disable_components(self)
            customize.trainer_sideFrame(self)

    def add_trainer_confirm(self):
        n = trainer_function.add_trainer(self)
        if n == 1:
            customize.enable_components(self)
            customize.trainer_sideFrame(self)
            customize.main_trainer_customize(self)
            trainer_function.count_trainer_data(self)
            self.choose_trainer_comboBox.clear()
            trainer_table = "select trainer_id, trainer_full_name, trainer_date_hired, emp_id from trainer"
            cur.execute(trainer_table)
            fetch_trainer_table = cur.fetchall()
            self.trainer_tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(fetch_trainer_table):
                self.trainer_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.trainer_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def add_trainer_cancel(self):
        customize.enable_components(self)
        customize.trainer_sideFrame(self)
        customize.main_trainer_customize(self)
        self.choose_trainer_comboBox.clear()

    def remove_trainer(self):
        cur.execute("select trainer_full_name from trainer ORDER BY trainer_full_name")
        trainer_remove_list = cur.fetchall()
        conn.commit()
        trainer_remove_list_string = [item[0] for item in trainer_remove_list]
        self.remove_trainer_name_comboBox.clear()
        self.remove_trainer_name_comboBox.addItems(trainer_remove_list_string)
        check_name = self.remove_trainer_name_comboBox.currentText()
        if check_name == "":
            dialog = QMessageBox(self)
            dialog.setWindowTitle('Warning')
            dialog.setText('\nThere are no trainers available.')
            dialog.setStyleSheet("QMessageBox{background-color: white;}"
                                 "QLabel{border-color: white;font: bold 20px Arial, serif;color: #037a28;}"
                                 "QPushButton{padding: 5px 40px 5px 40px;border-color: #FF3E3F;background-color: #ff3e3f;color: rgb(255, 255, 255);border-radius: 10px;font: bold 20px Arial, serif;cursor: grab;}"
                                 "QPushButton:hover{border-color:#cc3132;background-color: #cc3132;}")
            dialog.show()
        else:
            self.trainer_stackedWidget.setCurrentIndex(1)
            customize.disable_components(self)
            customize.trainer_sideFrame(self)

    def remove_trainer_confirm(self):
        n = trainer_function.remove_trainer(self)
        if n == 1:
            customize.enable_components(self)
            customize.trainer_sideFrame(self)
            customize.main_trainer_customize(self)
            trainer_function.count_trainer_data(self)
            self.remove_trainer_name_comboBox.clear()
            self.remove_trainer_error_notif_1.setText("")
            self.remove_trainer_error_notif_2.setText("")
            trainer_table = "select trainer_id, trainer_full_name, trainer_date_hired, emp_id from trainer"
            cur.execute(trainer_table)
            fetch_trainer_table = cur.fetchall()
            self.trainer_tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(fetch_trainer_table):
                self.trainer_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.trainer_tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def remove_trainer_cancel(self):
        customize.enable_components(self)
        customize.trainer_sideFrame(self)
        customize.main_trainer_customize(self)
        self.remove_trainer_name_comboBox.clear()
        self.remove_trainer_error_notif_1.setText("")
        self.remove_trainer_error_notif_2.setText("")

    # ================================================================================================================
    def logoutFunction(self):
        login = Login()
        widget.addWidget(login)
        widget.showMaximized()
        widget.setCurrentIndex(widget.currentIndex() + 1)



class Login(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("login.ui", self)
        #customize
        customize.login_customize(self)
        #BUTTONS
        self.login_button.clicked.connect(self.login_to_home)
        self.changePass_button.clicked.connect(self.changePassword)

    def login_to_home(self):
        n = login_function.login(self)
        if n == 1:
            main_window = MainWindow()
            widget.addWidget(main_window)
            widget.showMaximized()
            widget.setCurrentIndex(widget.currentIndex() + 1)
    def changePassword(self):
        self.login_error_label.setText("")
        changePass = ChangePassword()
        widget.addWidget(changePass)
        widget.setCurrentIndex(widget.currentIndex() + 1)

#CHANGE PASSWORD TAB
class ChangePassword(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("changepassword.ui", self)
        #customize
        customize.changePass_customize(self)

        #BUTTONS
        self.confirm_changePass_btn.clicked.connect(self.changePassFunction_confirm)
        self.cancel_changePass_btn.clicked.connect(self.changePassFunction_cancel)


    def changePassFunction_confirm(self):
        n = changePass_function.changePass(self)
        if n == 1:
            dialog = QMessageBox(self)
            dialog.setWindowTitle(' ')
            dialog.setText('\nPassword has beeen successfully changed!')
            dialog.setStyleSheet("QMessageBox{background-color: white;}"
                                 "QLabel{border-color: white;font: bold 20px Arial, serif;color: #037a28;}"
                                 "QPushButton{padding: 5px 40px 5px 40px;border-color: #FF3E3F;background-color: #ff3e3f;color: rgb(255, 255, 255);border-radius: 10px;font: bold 20px Arial, serif;cursor: grab;}"
                                 "QPushButton:hover{border-color:#cc3132;background-color: #cc3132;}")
            dialog.show()
            login = Login()
            widget.addWidget(login)
            widget.showMaximized()
            widget.setCurrentIndex(widget.currentIndex() + 1)

    def changePassFunction_cancel(self):
        login = Login()
        widget.addWidget(login)
        widget.showMaximized()
        widget.setCurrentIndex(widget.currentIndex() + 1)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Login()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.showMaximized()
    widget.setMinimumSize(800, 600)
    widget.setWindowTitle("Spirit's Fitness Gym")
    widget.setWindowIcon(QtGui.QIcon('spiritfitnessgymlogo.png'))
    widget.show()

    app.exec_()
    sys.exit(app.exec_())