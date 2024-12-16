import psycopg2

conn = psycopg2.connect(database="SpiritsFitnessGym",
                        user="postgres",
                        host='localhost',
                        password="postgres",
                        port=5432)
cur = conn.cursor()

def count_employee_data(self):
    sql_count = "SELECT COUNT(emp_id) FROM employee"
    cur.execute(sql_count)
    fetch_count = cur.fetchone()
    fetch_count = str(fetch_count)
    fetch_count = fetch_count.replace("(", "")
    fetch_count = fetch_count.replace(")", "")
    fetch_count = fetch_count.replace(",", "")
    self.employee_total_home_label.setText(fetch_count)
    self.employee_total_main_label.setText(fetch_count)
    conn.commit()
def add_employee(self):
    first_name = self.employee_first_name_main_input.text()
    last_name = self.employee_last_name_main_input.text()
    contact_num = self.employee_phone_num_input.text()
    first_name = first_name.upper()
    last_name = last_name.upper()
    sql_select = "SELECT emp_id FROM employee WHERE emp_fname = %s AND emp_lname = %s"
    data_select = (first_name, last_name,)
    cur.execute(sql_select, data_select)
    fetch_one = cur.fetchone()
    print(fetch_one)
    if first_name == "" or last_name == "" or contact_num == "":
        self.add_employee_main_error_notif.setText("Fill up first. Try again.")
        return 0
    elif len(contact_num) != 11:
        self.add_employee_main_error_notif.setText("Invalid phone number format. Try again.")
    else:
        try:
            int(contact_num)
            if fetch_one == None:
                sql_select_phone_num = "SELECT emp_id FROM employee WHERE emp_phone_num = %s"
                data_select_num = (contact_num,)
                cur.execute(sql_select_phone_num, data_select_num)
                fetch_one_num = cur.fetchone()
                if fetch_one_num == None:
                    str(contact_num)
                    sql_insert_emp = "INSERT INTO employee(emp_fname, emp_lname, emp_phone_num, gym_id) VALUES(%s, %s, %s, 1)"
                    data_insert = (first_name, last_name, contact_num)
                    cur.execute(sql_insert_emp, data_insert)
                    sql_update_emp = "UPDATE employee SET emp_full_name = CONCAT(%s, ' ', %s) WHERE emp_fname = %s AND emp_lname = %s"
                    data_update = (first_name, last_name, first_name, last_name)
                    cur.execute(sql_update_emp, data_update)
                    conn.commit()
                    return 1
                else:
                    self.add_employee_main_error_notif.setText("Phone number already exists. Try again.")
                    return 0
            else:
                self.add_employee_main_error_notif.setText("Name already exists. Try again.")
                return 0
        except ValueError:
            self.add_employee_main_error_notif.setText("Invalid phone number format. Try again.")
            return 0


def remove_employee(self):
    name = self.remove_employee_name_comboBox.currentText()
    sql_select_data = "SELECT trainer_id FROM trainer WHERE trainer_full_name = %s"
    data_insert = (name,)
    cur.execute(sql_select_data, data_insert)
    trainer_fetch_data = cur.fetchone()
    if trainer_fetch_data == None:
        self.remove_employee_error_notif_1.setText("")
        self.remove_employee_error_notif_2.setText("")
        sql_delete_employee = "DELETE FROM employee WHERE emp_full_name = %s"
        data_delete = (name,)
        cur.execute(sql_delete_employee, data_delete)
        conn.commit()
        return 1
    else:
        self.remove_employee_error_notif_1.setText("This employee is still currently")
        self.remove_employee_error_notif_2.setText("a trainer. Try again.")
        return 0

