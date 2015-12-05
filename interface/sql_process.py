from __future__ import print_function
import csv
import sys

import mysql.connector

config = {
        'user': 'batigoal',
        'password': 'clicc', 
        'host': '54.67.83.25', # Localhost. If your MySQL Server is running on your own computer.
        'port': '3306', # Default port on Windows/Linux is 3306. On Mac it may be 3307.
        'database': 'project',
    }

class SQL_Process:
    def __init__(self):
        try:
          self.__cnx = mysql.connector.connect(**config)
          self.__cnx.get_warnings = True
          self.__cursor = self.__cnx.cursor()
        except mysql.connector.Error as err:
          print("Connection Error: {}".format(err))
          #sys.exit(1)

    def __execute(self, query, values):
        your_query = query % values
        print("Executing: {} ... ".format(query % values), end="")
        try:
            self.__cursor.execute(query, values, multi=True)
        except mysql.connector.Error as err:
            print("ERROR\nMySQL Error: {}\n".format(err))
            #sys.exit(1)
        else:
            print("\nSuccess\n")


    def insert_data(self, eid, age, salary):
        if(self.__checkIdAvailability(eid)):
            print("[Warning] The employee {} has been in the database...\nno data inserted.".format(eid))
        else:
            """Insert a row of employee data into the database"""
            value = {
                "emp_id": eid,
                "emp_age": age,
                "emp_salary": salary}
            query = (
                "INSERT INTO Employees(id, age, salary) VALUES"
                "(%(emp_id)s, %(emp_age)s, %(emp_salary)s);")
            print("Executing: {} ... ".format(query % value), end="")
            try:
                self.__cursor.execute(query, value)
                self.__cnx.commit()
            except mysql.connector.Error as err:
                print("ERROR\nMySQL Error: {}\n".format(err))
                #sys.exit(1)
            else:
                print("\nSuccess\n")


    def __checkIdAvailability(self, eid):
        value = {'emp_id': eid}
        query = """
            SELECT *
            FROM Employees
            WHERE id= %(emp_id)s"""
        try:
            self.__cursor.execute(query, value)
        except mysql.connector.Error as err:
            print("ERROR\nMySQL Error: {}\n".format(err))
            #sys.exit(1)
        else:
            #print("\nSuccess\n")
            result = self.__cursor.fetchone()
            if(result is not None):
                return True
            else:
                return False
    
    def select_id(self, emp_id):
        """Select the information about a specific employee with id"""
        value = {'emp_id': emp_id}
        query = """
            SELECT id AS emp_id, age AS emp_age, salary AS emp_salary
            FROM Employees
            WHERE id= %(emp_id)s"""
        print("Executing: {} ... ".format(query % value), end="")
        try:
            self.__cursor.execute(query, value)
        except mysql.connector.Error as err:
            print("ERROR\nMySQL Error: {}\n".format(err))
            #sys.exit(1)
        else:
            print("\nSuccess\n")
            result = self.__cursor.fetchone()
            if(result is not None):   # check if there is any row return
                print("Employee({})'s age is {} and salary is {}.".format(result[0], result[1], self.decryption(result[2])))
            else:
                print("[Warning] There is no such employee with id {}".format(emp_id))


    def decryption(self, code):
        return "a"


    def select_sum(self):
        """Select the sum of salary of all employees"""
        query = """
            SELECT SUM(salary) AS sum
            FROM Employees
            """
        print("Executing: {} ... ".format(query), end="")
        try:
            self.__cursor.execute(query)
        except mysql.connector.Error as err:
            print("ERROR\nMySQL Error: {}\n".format(err))
            #sys.exit(1)
        else:
            print("\nSuccess\n")
            result = self.__cursor.fetchone()
            if(result is not None):   # check if there is any row return
                print("The sum of salary of all employee is {}.".format(self.decryption(result[0])))
            else:
                print("[Warning]  There is no such employee under this criteria")


    def select_sum_where(self, condition):
        """Select the sum of salary of the employees under the Where (no groupby) condition"""
        query = """
            SELECT SUM(salary) AS sum
            FROM Employees
            """ + condition + ";"
        print("Executing: {} ... ".format(query), end="")
        try:
            self.__cursor.execute(query)
        except mysql.connector.Error as err:
            print("ERROR\nMySQL Error: {}\n".format(err))
            #sys.exit(1)
        else:
            print("\nSuccess\n")
            result = self.__cursor.fetchone()
            if(result is not None):   # check if there is any row return
                print("The sum of salary of such employee is {}.".format(result[0]))
            else:
                print("[Warning] There is no such employee under this criteria")


    def select_sum_groupby(self, condition):
        """Select the sum of salary of all employees under the Where Group by and Having condition"""
        query = """
            SELECT age, SUM(salary) AS sum
            FROM Employees
            """ + condition + ";"
        print("Executing: {} ... ".format(query), end="")
        try:
            self.__cursor.execute(query)
        except mysql.connector.Error as err:
            print("ERROR\nMySQL Error: {}\n".format(err))
            #sys.exit(1)
        else:
            print("\nSuccess\n")
            firstRow = self.__cursor.fetchone()
            if(firstRow is not None):   # check if there is any row return
                print("The sum of salary of such employee with age {} is {}.".format(firstRow[0], firstRow[1]))
            else:
                print("[Warning] There is no such employee under this criteria")
            for(age, sum) in self.__cursor:
                print("The sum of salary of such employee with age {} is {}.".format(age, sum))


    def select_avg(self):
        """Select the average of salary of all employees"""
        query1 = """
            SELECT SUM(salary) as sum
            FROM Employees;
            """
        sum = 0
        count = 0
        print("Executing: {} ... ".format(query1), end="")
        try:
            self.__cursor.execute(query1)
        except mysql.connector.Error as err:
            print("ERROR\nMySQL Error: {}\n".format(err))
            #sys.exit(1)
        else:
            print("\nSuccess\n")
            result = self.__cursor.fetchone()
            if(result is not None):   # check if there is any row return
                sum = result[0]
                print("The sum of salary of all employee is {}.".format(self.decryption(result[0])))
            else:
                print("[Warning]  There is no such employee under this criteria")
        query2 = """
            SELECT COUNT(*) as count
            FROM Employees;
            """
        print("Executing: {} ... ".format(query2), end="")
        try:
            self.__cursor.execute(query2)
        except mysql.connector.Error as err:
            print("ERROR\nMySQL Error: {}\n".format(err))
            #sys.exit(1)
        else:
            print("\nSuccess\n")
            result = self.__cursor.fetchone()
            if(result is not None):   # check if there is any row return
                count = result[0]
                print("The sum of salary of all employee is {}.".format(self.decryption(result[0])))
            else:
                print("[Warning]  There is no such employee under this criteria")
        if(sum != 0 and count != 0):
            print("The average of salary of all employee is " + str(sum*1.0/count))

        
        
    
    def roma(self):
        print("Forza Roma")




