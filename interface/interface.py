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
#     a.insert_data(11, 25, 1000)
#     a.insert_data(31, 25, 2000)
#     a.insert_data(32, 25, 3000)
#     a.insert_data(200, 45, 2200)
#     a.insert_data(123, 35, 2100)
#     a.insert_data(42, 14, 1235)
#     a.insert_data(53, 60, 5245)
#     a.insert_data(15, 55, 5235)
#     a.insert_data(16, 35, 1035)
#     a.insert_data(17, 35, 20000)
#     a.insert_data(2, 42, 200000)
#     a.insert_data(0, 33, 10000)
    a.select_sum()
#     a.select_id("2")
    a.select_sum_where("WHERE age<26")
    #a.select_sum_groupby("GROUP BY age")
    #a.select_sum_groupby("GROUP BY age HAVING age<10")
    #a.select_avg()
    #a.select_avg_where("WHERE age<10")
#     a.select_avg_groupby("WHERE age<26 GROUP BY age HAVING SUM(salary) > 100000")
##    print welcome_words
##    print manu
#     enc_test = a.encryption("100")
#     dec_test = a.decryption("enc_test")
#     print dec_test
    
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
