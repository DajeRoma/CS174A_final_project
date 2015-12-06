from sql_process import SQL_Process

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
  Version:        0.1
  Last update:    Dec. 2, 2015
  
    """
    manu = """
    INSERT {emp_id} {emp_age} {emp_salary}
    manu(m):    Display the manu
    quit(q):    Quit the program
    """
    
    command = ""
    a = SQL_Process()
    #a.select_id("931883")
    #a.insert_data(931126, 54, 22200)
    #a.select_sum()
    #a.select_sum_where("WHERE age<26")
    #a.select_sum_groupby("GROUP BY age")
    #a.select_sum_groupby("GROUP BY age HAVING age<10")
    #a.select_avg()
    #a.select_avg_where("WHERE age<10")
    a.select_avg_groupby("WHERE age<26 GROUP BY age HAVING SUM(salary) > 100000")
##    print welcome_words
##    print manu
#     enc_test = a.encryption("0")

    raw_input()
    while(command != "quit" and command != "q"):
        if(command == "m" or command == "manu"):
            print manu
        command = raw_input("Please enter your command:\n")
        print "You entered: " + command
        if(command == "a"):
            a.select_sum_groupby("GROUP BY age HAVING age<10")
    







if __name__ == '__main__':
    interface();
