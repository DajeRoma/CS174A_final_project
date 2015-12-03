from __future__ import print_function
import csv
import sys

import mysql.connector

config = {
        'user': 'batigoal',
        'password': 'clicc', 
        'host': '54.183.181.128', # Localhost. If your MySQL Server is running on your own computer.
        'port': '3306', # Default port on Windows/Linux is 3306. On Mac it may be 3307.
        'database': 'project',
    }

class SQL_Process:
    def connect_to_server(self):
        try:
          cnx = mysql.connector.connect(**config)
          cursor = cnx.cursor()
        except mysql.connector.Error as err:
          print("Connection Error: {}".format(err))
          sys.exit(1)

    
    def roma(self):
        print("Forza Roma")
