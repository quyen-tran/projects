"""
@author: Quyen Duchesneau
@subject: Foothill CS003A
@assignment: Lab Assignment 7 - Casino with Methods and a Class
@date: Feb 12, 2022
"""

# ---------- SOURCE ----------

import random as rand


# Helper Class
class MultipleString:
    """ Encapsulates a 3-string object """
    
    # intended class constants
    MIN_LEN = 1
    MAX_LEN = 50
    DEFAULT_STRING = "(undefined)"
    
    # constructor method
    def __init__(self, string1 = DEFAULT_STRING, string2 = DEFAULT_STRING, 
                 string3 = DEFAULT_STRING):
        """
        Initialize all three string inputs. Check that string inputs are valid.
        """
        # check String No. 1
        if self.valid_string(string1) is True:
            self.string1 = string1
        else:
            self.string1 = self.DEFAULT_STRING
        # check String No. 2
        if self.valid_string(string2) is True:
            self.string2 = string2
        else:
            self.string2 = self.DEFAULT_STRING
        # check String No. 3
        if self.valid_string(string3) is True:
            self.string3 = string3
        else:
            self.string3 = self.DEFAULT_STRING

    # mutator ("set") methods
    def set_string1(self, the_string):
        """
        Set String No. 1 in this class.
        @return valid_check Validity state of the input string; True = new
                            string set | False = default set
        """
        valid_check = self.valid_string(the_string)
        if valid_check is True:
            self.string1 = the_string
        return valid_check
    
    def set_string2(self, the_string):
        """
        Set String No. 2 in this class.
        @return valid_check Validity state of the input string; True = new
                            string set | False = default set
        """
        valid_check = self.valid_string(the_string)
        if valid_check is True:
            self.string2 = the_string
        return valid_check
    
    def set_string3(self, the_string):
        """
        Set String No. 3 in this class.
        @return valid_check Validity state of the input string; True = new
                            string set | False = default set
        """
        valid_check = self.valid_string(the_string)
        if valid_check is True:
            self.string3 = the_string
        return valid_check
    
    # accessor ("get") methods
    def get_string1(self):
        """
        Get String No. 1 in this class.
        @return String No. 1
        """
        return self.string1
    
    def get_string2(self):
        """
        Get String No. 2 in this class.
        @return String No. 2
        """
        return self.string2
    
    def get_string3(self):
        """
        Get String No. 3 in this class.
        @return String No. 3
        """
        return self.string3
    
    def to_string(self):
        """
        Get a single string that contain the string variables in this class.
        @return a combined string of the class variables (string)
        """
        return "[{}] [{}] [{}]".format(self.string1, self.string2, self.string3)
    
    # helper methods for the entire class
    def valid_string(self, the_string):
        """
        Determine whether a string is valid.
        @param the_string input string for validity check
        @return isValid TRUE if string's length is between MIN_LEN and MAX_LEN
        """
        is_valid = False
        if self.MIN_LEN <= len(the_string) <= self.MAX_LEN:
            is_valid = True
        return is_valid


# Global variables
MIN_BET = 0
MAX_BET = 50

# Global-Scope Functions
def get_bet():
    """
    Prompts user for input and returns the bet amount. Vet the bet amount that
    it is legal (0 < bet < 50).
    @return user_bet legal bet from user
    """
    done = False
    while not done:
        user_bet = int(input("How much would you like to bet (1-50) or 0 to "
                             "quit? "))
        if MIN_BET <= user_bet <= MAX_BET:
            return user_bet
            done = True

def pull():
    """
    Instantiate and return a MultipleString object: three random strings chosen
    according to the probabilities of "cherries", "BAR", "7", and "space".
    @return pull_result A MultipleString object
    """
    slots = [rand_string(), rand_string(), rand_string()]
    pull_result = MultipleString(slots[0], slots[1], slots[2])
    return pull_result

def rand_string():
    """
    Return a string from probabilities list: BAR (45%), cherries (40%), 
    space (5%), and 7 (10%).
    """
    # get a random integer between 0 and 100 (inclusive)
    chance = rand.randint(0, 100)
    # determine string output from probabilities list
    if chance <= 5:
        return " "
    elif 5 < chance <= 15:
        return "7"
    elif 15 < chance <= 55:
        return "cherries"
    elif 55 < chance <= 100:
        return "BAR"
    else:
        return "*Invalid*"

def get_pay_multiplier(the_pull):
    """
    Determines the payout for the selected pull (MultipleString object).
    cherries    [not cherries]      [any]               5x bet
    cherries    cherries            [not cherries]      15x bet
    cherries    cherries            cherries            30x bet
    BAR         BAR                 BAR                 50x bet
    7           7                   7                   100x bet
    @return payout Winning payout for current MultipleString object
    """
    # initialize return variable
    payout = 0
    # access the individual strings from the MultipleString object
    slot_1 = the_pull.get_string1()
    slot_2 = the_pull.get_string2()
    slot_3 = the_pull.get_string3()
    # short hand definitions for the various slot options
    c = "cherries"
    b = "BAR"
    s = "7"
    # check the various slots per specific configurations for payout
    if slot_1 is c and slot_2 is not c:
        payout = 5
    elif slot_1 is c and slot_2 is c and slot_3 is not c:
        payout = 15
    elif slot_1 is c and slot_2 is c and slot_3 is c:
        payout = 30
    elif slot_1 is b and slot_2 is b and slot_3 is b:
        payout = 50
    elif slot_1 is s and slot_2 is s and slot_3 is s:
        payout = 100
    else:
        payout = 0
    # return the final payout amount
    return payout

def display(the_pull, winnings):
    """
    Display the_pull (MultipleString object), winnings, and whether you won
    or lost.
    """
    print("whirrrrrr... and your pull is...")
    print(the_pull.to_string())
    if winnings == 0:
        print("Sorry -- You lost!")
    else:
        print("Congrats! You won ${}.".format(winnings))


# Main Program
def main():
    """
    Simulates a casino slot machine while utilizing the MultipleString class
    """
    done = False
    print("*** Welcome to the MultipleString Casino! ***")
    while not done:
        bet = get_bet()
        if bet > 0:
            the_pull = pull()
            bet_multiplier = get_pay_multiplier(the_pull)
            winnings = bet * bet_multiplier
            display(the_pull, winnings)
        else:
            done = True  
    print("\n*** End of program. ***")

if __name__ == "__main__":
    main()


""" ---------- RUN ----------

    --- RUN #1: 40 pulls, BARS in # (2, 8, 37), cherries in # (31, 39) ---
    
*** Welcome to the MultipleString Casino! ***

How much would you like to bet (1-50) or 0 to quit? -1

How much would you like to bet (1-50) or 0 to quit? 51

How much would you like to bet (1-50) or 0 to quit? 1
whirrrrrr... and your pull is...
[BAR] [cherries] [cherries]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 2
whirrrrrr... and your pull is...
[BAR] [BAR] [BAR]
Congrats! You won $100.

How much would you like to bet (1-50) or 0 to quit? 3
whirrrrrr... and your pull is...
[cherries] [cherries] [BAR]
Congrats! You won $45.

How much would you like to bet (1-50) or 0 to quit? 4
whirrrrrr... and your pull is...
[BAR] [BAR] [ ]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 5
whirrrrrr... and your pull is...
[cherries] [BAR] [BAR]
Congrats! You won $25.

How much would you like to bet (1-50) or 0 to quit? 6
whirrrrrr... and your pull is...
[cherries] [cherries] [BAR]
Congrats! You won $90.

How much would you like to bet (1-50) or 0 to quit? 7
whirrrrrr... and your pull is...
[ ] [BAR] [cherries]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 8
whirrrrrr... and your pull is...
[BAR] [BAR] [BAR]
Congrats! You won $400.

How much would you like to bet (1-50) or 0 to quit? 9
whirrrrrr... and your pull is...
[cherries] [7] [cherries]
Congrats! You won $45.

How much would you like to bet (1-50) or 0 to quit? 10
whirrrrrr... and your pull is...
[cherries] [BAR] [cherries]
Congrats! You won $50.

How much would you like to bet (1-50) or 0 to quit? 11
whirrrrrr... and your pull is...
[cherries] [cherries] [7]
Congrats! You won $165.

How much would you like to bet (1-50) or 0 to quit? 12
whirrrrrr... and your pull is...
[cherries] [BAR] [BAR]
Congrats! You won $60.

How much would you like to bet (1-50) or 0 to quit? 13
whirrrrrr... and your pull is...
[cherries] [cherries] [BAR]
Congrats! You won $195.

How much would you like to bet (1-50) or 0 to quit? 14
whirrrrrr... and your pull is...
[BAR] [cherries] [BAR]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 15
whirrrrrr... and your pull is...
[7] [cherries] [cherries]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 16
whirrrrrr... and your pull is...
[cherries] [cherries] [BAR]
Congrats! You won $240.

How much would you like to bet (1-50) or 0 to quit? 17
whirrrrrr... and your pull is...
[cherries] [cherries] [BAR]
Congrats! You won $255.

How much would you like to bet (1-50) or 0 to quit? 18
whirrrrrr... and your pull is...
[cherries] [ ] [BAR]
Congrats! You won $90.

How much would you like to bet (1-50) or 0 to quit? 19
whirrrrrr... and your pull is...
[cherries] [BAR] [cherries]
Congrats! You won $95.

How much would you like to bet (1-50) or 0 to quit? 20
whirrrrrr... and your pull is...
[BAR] [cherries] [BAR]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 21
whirrrrrr... and your pull is...
[BAR] [cherries] [cherries]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 22
whirrrrrr... and your pull is...
[BAR] [cherries] [BAR]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 23
whirrrrrr... and your pull is...
[7] [7] [BAR]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 24
whirrrrrr... and your pull is...
[cherries] [cherries] [BAR]
Congrats! You won $360.

How much would you like to bet (1-50) or 0 to quit? 25
whirrrrrr... and your pull is...
[BAR] [BAR] [cherries]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 26
whirrrrrr... and your pull is...
[cherries] [BAR] [BAR]
Congrats! You won $130.

How much would you like to bet (1-50) or 0 to quit? 27
whirrrrrr... and your pull is...
[BAR] [BAR] [cherries]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 28
whirrrrrr... and your pull is...
[BAR] [cherries] [BAR]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 29
whirrrrrr... and your pull is...
[cherries] [cherries] [7]
Congrats! You won $435.

How much would you like to bet (1-50) or 0 to quit? 30
whirrrrrr... and your pull is...
[BAR] [7] [BAR]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 31
whirrrrrr... and your pull is...
[cherries] [cherries] [cherries]
Congrats! You won $930.

How much would you like to bet (1-50) or 0 to quit? 32
whirrrrrr... and your pull is...
[cherries] [cherries] [BAR]
Congrats! You won $480.

How much would you like to bet (1-50) or 0 to quit? 33
whirrrrrr... and your pull is...
[ ] [BAR] [cherries]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 34
whirrrrrr... and your pull is...
[BAR] [cherries] [BAR]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 35
whirrrrrr... and your pull is...
[cherries] [BAR] [BAR]
Congrats! You won $175.

How much would you like to bet (1-50) or 0 to quit? 36
whirrrrrr... and your pull is...
[BAR] [ ] [cherries]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 37
whirrrrrr... and your pull is...
[BAR] [BAR] [BAR]
Congrats! You won $1850.

How much would you like to bet (1-50) or 0 to quit? 38
whirrrrrr... and your pull is...
[BAR] [cherries] [BAR]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 39
whirrrrrr... and your pull is...
[cherries] [cherries] [cherries]
Congrats! You won $1170.

How much would you like to bet (1-50) or 0 to quit? 40
whirrrrrr... and your pull is...
[BAR] [cherries] [cherries]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 0

*** End of program. ***

    --- RUN #2: 40 pulls, BARS in # (11, 16, 32), cherries in # (8) ---

*** Welcome to the MultipleString Casino! ***

How much would you like to bet (1-50) or 0 to quit? -10

How much would you like to bet (1-50) or 0 to quit? 100

How much would you like to bet (1-50) or 0 to quit? 1
whirrrrrr... and your pull is...
[BAR] [7] [BAR]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 2
whirrrrrr... and your pull is...
[cherries] [BAR] [BAR]
Congrats! You won $10.

How much would you like to bet (1-50) or 0 to quit? 3
whirrrrrr... and your pull is...
[cherries] [BAR] [BAR]
Congrats! You won $15.

How much would you like to bet (1-50) or 0 to quit? 4
whirrrrrr... and your pull is...
[cherries] [cherries] [BAR]
Congrats! You won $60.

How much would you like to bet (1-50) or 0 to quit? 5
whirrrrrr... and your pull is...
[ ] [cherries] [BAR]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 6
whirrrrrr... and your pull is...
[BAR] [BAR] [cherries]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 7
whirrrrrr... and your pull is...
[cherries] [cherries] [BAR]
Congrats! You won $105.

How much would you like to bet (1-50) or 0 to quit? 8
whirrrrrr... and your pull is...
[cherries] [cherries] [cherries]
Congrats! You won $240.

How much would you like to bet (1-50) or 0 to quit? 9
whirrrrrr... and your pull is...
[7] [cherries] [cherries]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 10
whirrrrrr... and your pull is...
[cherries] [BAR] [7]
Congrats! You won $50.

How much would you like to bet (1-50) or 0 to quit? 11
whirrrrrr... and your pull is...
[BAR] [BAR] [BAR]
Congrats! You won $550.

How much would you like to bet (1-50) or 0 to quit? 12
whirrrrrr... and your pull is...
[BAR] [cherries] [7]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 13
whirrrrrr... and your pull is...
[cherries] [BAR] [cherries]
Congrats! You won $65.

How much would you like to bet (1-50) or 0 to quit? 14
whirrrrrr... and your pull is...
[cherries] [ ] [BAR]
Congrats! You won $70.

How much would you like to bet (1-50) or 0 to quit? 15
whirrrrrr... and your pull is...
[cherries] [BAR] [cherries]
Congrats! You won $75.

How much would you like to bet (1-50) or 0 to quit? 16
whirrrrrr... and your pull is...
[BAR] [BAR] [BAR]
Congrats! You won $800.

How much would you like to bet (1-50) or 0 to quit? 17
whirrrrrr... and your pull is...
[7] [cherries] [cherries]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 18
whirrrrrr... and your pull is...
[ ] [cherries] [BAR]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 19
whirrrrrr... and your pull is...
[cherries] [cherries] [BAR]
Congrats! You won $285.

How much would you like to bet (1-50) or 0 to quit? 20
whirrrrrr... and your pull is...
[cherries] [7] [cherries]
Congrats! You won $100.

How much would you like to bet (1-50) or 0 to quit? 21
whirrrrrr... and your pull is...
[cherries] [BAR] [cherries]
Congrats! You won $105.

How much would you like to bet (1-50) or 0 to quit? 22
whirrrrrr... and your pull is...
[BAR] [7] [cherries]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 23
whirrrrrr... and your pull is...
[cherries] [cherries] [BAR]
Congrats! You won $345.

How much would you like to bet (1-50) or 0 to quit? 24
whirrrrrr... and your pull is...
[cherries] [BAR] [7]
Congrats! You won $120.

How much would you like to bet (1-50) or 0 to quit? 25
whirrrrrr... and your pull is...
[cherries] [7] [BAR]
Congrats! You won $125.

How much would you like to bet (1-50) or 0 to quit? 26
whirrrrrr... and your pull is...
[cherries] [BAR] [BAR]
Congrats! You won $130.

How much would you like to bet (1-50) or 0 to quit? 27
whirrrrrr... and your pull is...
[cherries] [BAR] [BAR]
Congrats! You won $135.

How much would you like to bet (1-50) or 0 to quit? 28
whirrrrrr... and your pull is...
[cherries] [BAR] [cherries]
Congrats! You won $140.

How much would you like to bet (1-50) or 0 to quit? 29
whirrrrrr... and your pull is...
[cherries] [BAR] [cherries]
Congrats! You won $145.

How much would you like to bet (1-50) or 0 to quit? 30
whirrrrrr... and your pull is...
[BAR] [cherries] [BAR]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 31
whirrrrrr... and your pull is...
[ ] [BAR] [7]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 32
whirrrrrr... and your pull is...
[BAR] [BAR] [BAR]
Congrats! You won $1600.

How much would you like to bet (1-50) or 0 to quit? 33
whirrrrrr... and your pull is...
[7] [BAR] [BAR]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 34
whirrrrrr... and your pull is...
[BAR] [BAR] [7]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 35
whirrrrrr... and your pull is...
[cherries] [ ] [cherries]
Congrats! You won $175.

How much would you like to bet (1-50) or 0 to quit? 36
whirrrrrr... and your pull is...
[ ] [cherries] [cherries]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 37
whirrrrrr... and your pull is...
[cherries] [7] [cherries]
Congrats! You won $185.

How much would you like to bet (1-50) or 0 to quit? 38
whirrrrrr... and your pull is...
[7] [BAR] [cherries]
Sorry -- You lost!

How much would you like to bet (1-50) or 0 to quit? 39
whirrrrrr... and your pull is...
[cherries] [BAR] [cherries]
Congrats! You won $195.

How much would you like to bet (1-50) or 0 to quit? 40
whirrrrrr... and your pull is...
[cherries] [BAR] [BAR]
Congrats! You won $200.

How much would you like to bet (1-50) or 0 to quit? 0

*** End of program. ***


"""

