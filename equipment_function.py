from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsBlurEffect, QMessageBox, QAction, QHeaderView
import psycopg2

conn = psycopg2.connect(database="SpiritsFitnessGym",
                        user="postgres",
                        host='localhost',
                        password="postgres",
                        port=5432)
cur = conn.cursor()

def count_equipment_data(self):
    sql_count = "SELECT COUNT(equipment_id) FROM equipment"
    cur.execute(sql_count)
    fetch_count = cur.fetchone()
    fetch_count = str(fetch_count)
    fetch_count = fetch_count.replace("(", "")
    fetch_count = fetch_count.replace(")", "")
    fetch_count = fetch_count.replace(",", "")
    self.equipment_total_home_label.setText(fetch_count)
    self.equipment_total_main_label.setText(fetch_count)
    conn.commit()
    sql_count_defect = "SELECT COUNT(equipment_id) FROM equipment WHERE equipment_status = 'DEFECT'"
    cur.execute(sql_count_defect)
    fetch_count = cur.fetchone()
    fetch_count = str(fetch_count)
    fetch_count = fetch_count.replace("(", "")
    fetch_count = fetch_count.replace(")", "")
    fetch_count = fetch_count.replace(",", "")
    self.defect_equipment_total_label.setText(fetch_count)
    conn.commit()


def add_equipment_main(self):
    name = self.equipment_add_name_input.text()
    qty =  self.equipment_add_qty_input.text()
    status = self.equipment_add_status_comboBox.currentText()
    name = name.upper()
    qty = qty.upper()
    status = status.upper()
    sql_select = "SELECT equipment_id FROM equipment WHERE equipment_name = %s"
    data_select = (name,)
    cur.execute(sql_select, data_select)
    fetch_one = cur.fetchone()
    print(fetch_one)
    if name == "" or qty == "":
        self.add_equipment_main_error_notif.setText("Fill up first. Try again.")
        return 0
    else:
        try:
            int(qty)
            if fetch_one == None:
                sql_insert_equipment = "INSERT INTO equipment(equipment_name, equipment_qty, equipment_status, gym_id) VALUES(%s, %s, %s, 1)"
                data_insert = (name, qty, status)
                cur.execute(sql_insert_equipment, data_insert)
                conn.commit()
                return 1
            else:
                self.add_equipment_main_error_notif.setText("Equipment already exists. Try again.")
                return 0
        except ValueError:
            self.add_equipment_main_error_notif.setText("Quantity must be a value. Try again.")
            return 0


def blur_edit_equipment_components(self):
    blur_effect = QGraphicsBlurEffect()
    self.edit_equipment_components_blur_frame.setGraphicsEffect(blur_effect)
    if self.equipment_edit_name_comboBox.isEnabled():
        self.equipment_edit_qty_input.setEnabled(False)
        self.add_equipment_amount_btn.setEnabled(False)
        self.deduct_equipment_amount_btn.setEnabled(False)
        self.equipment_edit_status_input.setEnabled(False)
        self.confirm_edit_equipment_main_btn.setEnabled(False)
    else:
        blur_effect.setEnabled(False)
        self.equipment_edit_qty_input.setEnabled(True)
        self.add_equipment_amount_btn.setEnabled(True)
        self.deduct_equipment_amount_btn.setEnabled(True)
        self.equipment_edit_status_input.setEnabled(True)
        self.confirm_edit_equipment_main_btn.setEnabled(True)


def equipment_id_main(self):
    self.equipment_edit_name_comboBox.setEnabled(False)
    self.confirm_equipment_id_main_btn.setEnabled(False)
    name = self.equipment_edit_name_comboBox.currentText()
    sql_status = "SELECT equipment_status FROM equipment WHERE equipment_name = %s"
    data_insert = (name,)
    cur.execute(sql_status, data_insert)
    fetch_data = cur.fetchone()
    fetch_data = str(fetch_data)
    fetch_data = fetch_data.replace("(", "")
    fetch_data = fetch_data.replace(")", "")
    fetch_data = fetch_data.replace(",", "")
    fetch_data = fetch_data.replace("'", "")
    fetch_data = fetch_data.replace("'", "")
    print(fetch_data)
    if fetch_data == 'OPERATIONAL':
        self.equipment_edit_status_input.clear()
        self.equipment_edit_status_input.addItem("Operational")
        self.equipment_edit_status_input.addItem("Defect")
    else:
        self.equipment_edit_status_input.clear()
        self.equipment_edit_status_input.addItem("Defect")
        self.equipment_edit_status_input.addItem("Operational")


def equipment_qty_data(self):
    name = self.equipment_edit_name_comboBox.currentText()
    sql_qty = "SELECT equipment_qty FROM equipment WHERE equipment_name = %s"
    data_insert = (name,)
    cur.execute(sql_qty, data_insert)
    fetch_count = cur.fetchone()
    fetch_count = str(fetch_count)
    fetch_count = fetch_count.replace("(", "")
    fetch_count = fetch_count.replace(")", "")
    fetch_count = fetch_count.replace(",", "")
    self.equipment_current_qty_label.setText(fetch_count)
    conn.commit()

def add_equipment_amount_main(self):
    qty = self.equipment_edit_qty_input.text()
    current_qty = self.equipment_current_qty_label.text()
    if qty == "":
        self.edit_equipment_main_error_notif.setText("Fill up first. Try again.")
        return 0
    else:
        try:
            int(qty)
            sum = 0
            sum += int(qty) + int(current_qty)
            self.equipment_current_qty_label.setText(str(sum))
            self.edit_equipment_main_error_notif.setText("")
        except ValueError:
            self.edit_equipment_main_error_notif.setText("Quantity must be a value. Try again.")
            return 0

def deduct_equipment_amount_main(self):
    qty = self.equipment_edit_qty_input.text()
    current_qty = self.equipment_current_qty_label.text()
    if qty == "":
        self.edit_equipment_main_error_notif.setText("Fill up first. Try again.")
        return 0
    else:
        try:
            int(qty)
            diff = 0
            diff += int(current_qty) - int(qty)
            if diff < 0:
                self.edit_equipment_main_error_notif.setText("Quantity reached below 0. Try again.")
            else:
                self.edit_equipment_main_error_notif.setText("")
                self.equipment_current_qty_label.setText(str(diff))
        except ValueError:
            self.edit_equipment_main_error_notif.setText("Quantity must be a value. Try again.")
            return 0

def edit_equipment_main(self):
    name = self.equipment_edit_name_comboBox.currentText()
    status = self.equipment_edit_status_input.currentText()
    status = status.upper()
    qty = self.equipment_current_qty_label.text()
    sql_update_status = "UPDATE equipment SET equipment_status = %s WHERE equipment_name = %s"
    data_insert = (status, name,)
    cur.execute(sql_update_status, data_insert)
    sql_update_qty = "UPDATE equipment SET equipment_qty = %s WHERE equipment_name = %s"
    data_insert_qty = (int(qty),name,)
    cur.execute(sql_update_qty,data_insert_qty)
    conn.commit()
    return 1

def remove_equipment_main(self):
    name = self.remove_equipment_comboBox.currentText()
    sql_delete_equipment = "DELETE FROM equipment WHERE equipment_name = %s"
    data_delete = (name,)
    cur.execute(sql_delete_equipment, data_delete)
    conn.commit()
    return 1