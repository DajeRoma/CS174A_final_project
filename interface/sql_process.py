from __future__ import print_function
import csv
import sys

import mysql.connector
import subprocess as sb

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
        # check if the id has been in the db first
        if(self.__checkIdAvailability(eid)):
            print("[Warning] The employee {} has been in the database...\nno data inserted.".format(eid))
        else:
            """Insert a row of employee data into the database"""
            
            # encrypt salary
            salary = self.encryption(str(salary))
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
                print("Employee({})'s age is {} and salary is {}.".format(result[0], result[1], self.decryption(str(result[2]))))
            else:
                print("[Warning] There is no such employee with id {}".format(emp_id))


    def encryption(self, input_long):
        """CALL C program to do encryption using subprocess"""
        proc = sb.Popen(['./encrypt.out',input_long],stdout=sb.PIPE)
        encrypted_value = proc.stdout.readline()
        return encrypted_value

        
    def decryption(self, input_cipher):
        """ Call ./decrypt.out and do decryption"""
        proc = sb.Popen(['./decrypt.out',input_cipher],stdout=sb.PIPE)
        decrypted_res = proc.stdout.readline()
        return decrypted_res


    def select_sum(self):
        """Select the sum of salary of all employees"""
        query = """
            SELECT SUM_HE(salary) AS sum
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
                # decryption of the results
                decrypted_res = self.decryption(str(result[0]))
                print("The sum of salary of all employee is {}.".format(decrypted_res))
            else:
                print("[Warning]  There is no such employee under this criteria")

    def select_sum_where(self, condition):
        """Select the sum of salary of the employees under the Where (no groupby) condition"""
        query = """
            SELECT SUM_HE(salary) AS sum
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
                # decryption of the results
                decrypted_res = self.decryption(str(result[0]))
                print("The sum of salary of such employee is {}.".format(decrypted_res))
            else:
                print("[Warning] There is no such employee under this criteria")


    def select_sum_groupby(self, condition):
        """Select the sum of salary of all employees under the Where Group by and Having condition"""
        query = """
            SELECT age, SUM_HE(salary) AS sum
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
                print("The sum of salary of such employee with age {} is {}.".format(firstRow[0], self.decryption(str(firstRow[1]))))
            else:
                print("[Warning] There is no such employee under this criteria")
            for(age, sum) in self.__cursor:
                print("The sum of salary of such employee with age {} is {}.".format(age, self.decryption(str(sum))))


    def select_avg(self):
        """Select the average of salary of all employees"""
        count = 0
        sum = 0        
        ## Get the count first
        query1 = """
            SELECT COUNT(*) as count
            FROM Employees;
            """
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
                count = result[0]
                if(count == 0):
                    print("There is no employee in the database.")
                else:
                    print("There are {} employees.".format(count))
            else:
                print("[Warning] No row is returned.")
        ## If there are some employees, then we get the sum
        if(count > 0):
            query2 = """
                SELECT SUM_HE(salary) as sum
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
                    sum = self.decryption(str(result[0])) # decrypt the sum of salary
                    print("The sum of salary of all the employee is {}.".format(sum))
                    print("The average salary of all employee is " + str(sum*1.0/count))
                else:
                    print("[Warning] No row is returned...")                
        else:
            print("NULL    There is no employee in the database.")


    def select_avg_where(self, condition):
        """Select the average of salary of the employees under the where condition"""
        count = 0
        sum = 0        
        ## Get the count first
        query1 = """
            SELECT COUNT(*) as count
            FROM Employees
            """ + condition + ";"
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
                count = result[0]
                if(count == 0):
                    print("There is no such employee under this criteria in the database.")
                else:
                    print("There are {} such employees.".format(count))
            else:
                print("[Warning] No row is returned.")
        ## If there are some employees, then we get the sum
        if(count > 0):
            query2 = """
                SELECT SUM_HE(salary) as sum
                FROM Employees
                """ + condition + ";"
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
                    sum = self.decryption(str(result[0]))
                    print("The sum of salary of such employee is {}.".format(sum))
                    print("The average salary of such employee is " + str(sum*1.0/count))
                else:
                    print("[Warning] No row is returned...")                
        else:
            print("NULL    There is no employee in the database.")
        

    def select_avg_groupby(self, condition):
        """Select the average of salary of the employees under the where, groupby and having condition"""
        count = 0
        countList = []
        sum = 0        
        ## Get the count and sum
        query = """
            SELECT age, COUNT(*) as count, SUM(salary) as sum
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
                age = result[0]
                count = result[1]
                sum = self.decryption(str(result[2]))
                print("There are {} such employees with age {} and total salary {}.".format(age, count, sum))
                print("The average salaray of employees with age {} is {}".format(age, (sum*1.0/count)))
                for(ageI, countI, sumI) in self.__cursor:
                    sumI = self.decryption(str(sumI))
                    print("There are {} such employees with age {} and total salary {}.".format(ageI, countI, sumI))
                    print("The average salaray of employees with age {} is {}".format(ageI, (sumI*1.0/countI)))
            else:
                print("No row is returned...\nNULL    There is no such employee under this criteria")
        
  
    def roma(self):
        print("Forza Roma")




