if __name__ == '__main__':

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
        quit(q):    Quit the program

    """
    
    command = ""

    
    while(command != "quit" and command != "q"):
        print welcome_words
        print manu
        command = raw_input("Please enter your command:\n")
        print "You entered: " + command
    
