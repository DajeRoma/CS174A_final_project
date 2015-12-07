from sql_process import SQL_Process
import sys

def interface():
    welcome_words = """
  ################################################################################
  ##                                                                            ##
  ##  ########     ###    ######## ####  ######    #######     ###    ##        ##
  ##  ##     ##   ## ##      ##     ##  ##    ##  ##     ##   ## ##   ##        ##
  ##  ##     ##  ##   ##     ##     ##  ##        ##     ##  ##   ##  ##        ##
  ##  ########  ##     ##    ##     ##  ##   #### ##     ## ##     ## ##        ##
  ##  ##     ## #########    ##     ##  ##    ##  ##     ## ######### ##        ##
  ##  ##     ## ##     ##    ##     ##  ##    ##  ##     ## ##     ## ##        ##
  ##  ########  ##     ##    ##    ####  ######    #######  ##     ## ########  ##      
  ##                                                                            ##
  ################################################################################

  Team:           BatiGoal
  Developers:     Runsheng Song && Yiting Ju
  Version:        BETA 1.0
  Last update:    Dec. 7, 2015
  
    """
    manu = """
Operations
1. SQL operations:
    INSERT {emp_id} {emp_age} {emp_salary}
        example: INSERT 12 45 95000
          -- insert into the database an employee with id=12, age=45, and salary = 95000
          
    SELECT {emp_id}
        example: SELECT 25
          -- display the id, age and salary of the employee with id=25

    SELECT SUM [WHERE conditions (optional)] [GROUP BY age (optional)] [HAVING conditions (optional)]
        example: SELECT SUM WHERE age > 25
          -- display the total salary of those employees whose age is larger than 25
        example: SELECT SUM GROUP BY age HAVING COUNT(*) > 2
          -- display the age and total salary of those employees grouped by age, and
             there are more than 2 such employees in this age

    SELECT AVG [WHERE conditions (optional)] [GROUP BY age (optional)] [HAVING (optional)]
        example: SELECT AVG WHERE age < 30 GROUP BY age
          -- display the age and average salary of those employees who are younger than 30.
             grouped by age
             
2. Other operations:    
    manu(m):    Display the manu
    quit(q):    Quit the program
    """
    
    
    ## Testing starts
##    a = SQL_Process()
##    a.insert_data(11, 25, 1000)
##    a.insert_data(31, 25, 2000)
##    a.insert_data(32, 25, 3000)
##    a.insert_data(200, 45, 2200)
##    a.insert_data(123, 35, 2100)
##    a.insert_data(42, 14, 1235)
##    a.insert_data(53, 60, 5245)
##    a.insert_data(15, 55, 5235)
##    a.insert_data(16, 35, 1035)
##    a.insert_data(17, 35, 20000)
##    a.insert_data(2, 42, 200000)
##    a.insert_data(0, 33, 10000)
##    a.select_sum()
##    a.select_id("2")
##    a.select_sum_where("WHERE age<26")
##    a.select_sum_groupby("GROUP BY age")
##    a.select_sum_groupby("GROUP BY age HAVING age<10")
##    a.select_avg()
##    a.select_avg_where("WHERE age<10")
##    a.select_avg_groupby("WHERE age<26 GROUP BY age HAVING SUM(salary) > 100000")
##    enc_test = a.encryption("100")
##    dec_test = a.decryption(enc_test)
##    print dec_test
    ## Testing ends

    ## Program starts
    command = ""

    print welcome_words
    print manu
    sp = SQL_Process() ## connect to SQL server
    
    while(command != "quit" and command != "q"):
        # Accept input
        command = raw_input("Please enter your command:\n")        
        print "You entered: " + command
        command = command.lower()
        if(command == "m" or command == "manu"):
            print("Here is the manual")
            print manu
        elif(command == "q" or command == "quit"):
            print("Bye")
            sp.close()
            sys.exit(1)
        ## INSERT
        elif(command[:7] == "insert "):
            commandSplit = command.split()
            if(len(commandSplit) == 4):
                if(commandSplit[1].isdigit() and commandSplit[2].isdigit() and commandSplit[3].isdigit()):
                    sp.insert_data(commandSplit[1], commandSplit[2], commandSplit[3])                    
                else:
                    print("Invalid input... insert commant takes and only takes 3 digital arguments")
            else:
                print("Invalid input... insert commant takes and only takes 3 digital arguments")
        ## SELECT
        elif(command[:7] == "select "):
            commandSplit = command.split()
            ## SELECT emp_id
            if(len(commandSplit) == 2 and commandSplit[1].isdigit()):
                sp.select_id(commandSplit[1])
            ## SELECT *
            elif(len(commandSplit) == 2 and commandSplit[1] == "*"):
                sp.select_all()                
            ## SELECT SUM
            elif(len(commandSplit) >= 2 and "sum" in command and "where" not in command and "group" not in command and "having" not in command):
                sp.select_sum()
            ## SELECT SUM WHERE condition
            elif(len(commandSplit) >= 4 and "sum" in command and "where" in command and "group" not in command and "having" not in command):
                where_condition_index = command.find("where") 
                sp.select_sum_where(command[where_condition_index:])
            ## SELECT SUM WHERE condition GROUP BY condition HAVING condition
            elif(len(commandSplit) >= 5 and "sum" in command and "group by" in command):
                where_condition_index = command.find("where")
                group_condition_index = command.find("group")
                having_condition_index = command.find("having")
                if(command[group_condition_index+9:group_condition_index+12] == "age"): # only group by "age"
##                    # not necessary to check use in having clause
##                    if(command.rfind("sum") != command.find("sum")):    # Check if there is "sum" in Having
##                        command = command[:command.rfind("sum")+3]+"_he"+command[command.rfind("sum")+3:]   # Revise command
                    if(where_condition_index <= 0):     # no where clause
                        sp.select_sum_groupby(command[group_condition_index:])
                    else:       # there is where clause
                        sp.select_sum_groupby(command[where_condition_index:])
                else:
                    print("Invalid input... only group by 'age'")
            ## SELECT AVG
            elif(len(commandSplit) >= 2 and "avg" in command and "where" not in command and "group" not in command and "having" not in command):
                sp.select_avg()
            ## SELECT AVG WHERE condition
            elif(len(commandSplit) >= 4 and "avg" in command and "where" in command and "group" not in command and "having" not in command):
                where_condition_index = command.find("where") 
                sp.select_avg_where(command[where_condition_index:])
            ## SELECT AVG WHERE condition GROUP BY condition HAVING condition
            elif(len(commandSplit) >= 5 and "avg" in command and "group by" in command):
                where_condition_index = command.find("where")
                group_condition_index = command.find("group")
                if(command[group_condition_index+9:group_condition_index+12] == "age"): # only group by "age"
##                    # not necessary to check use in having clause
##                    if(command.rfind("sum") != command.find("sum")):    # Check if there is "sum" in Having
##                        command = command[:command.rfind("sum")+3]+"_he"+command[command.rfind("sum")+3:]   # Revise command
                    if(where_condition_index <= 0):     # no where clause
                        sp.select_avg_groupby(command[group_condition_index:])
                    else:   # there is where clause
                        sp.select_avg_groupby(command[where_condition_index:])
                else:
                    print("Invalid input... only group by 'age'")
            else:
                print("Invalid input...")
        else:
            print("Invalid input...")

    
if __name__ == '__main__':
    interface();

