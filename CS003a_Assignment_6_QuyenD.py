"""
@author: Quyen Duchesneau
@subject: Foothill CS003A
@assignment: Lab Assignment 6 - A Multiple String Class
@date: Feb 10, 2022
"""

# ---------- SOURCE ----------

import random as rand


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
        return "[{}, {}, {}]".format(self.string1, self.string2, self.string3)
    
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


def main():
    """
    Create MultipleString objects do the following operations: display, mutate,
    and access the various string properties.
    """
    # create 4 or more MultipleString objects
    list_multi_string = [MultipleString("apple", "orange", "pear"), 
                         MultipleString("egg", "bacon", "milk"), 
                         MultipleString("even", "odd", ""), 
                         MultipleString()]
    
    # display all objects
    print("--- Displaying all MultipleString objects ---")
    index = 1
    for ms_obj in list_multi_string:
        print("Object[" + str(index) + "]: ", ms_obj.to_string())
        # prep next object index
        index += 1
    print()
    
    # generate test cases for the mutation examples
    test_cases = ["123", "!@#$%^&*()_+", "", "*", "Stephen Hawking", 
                  "Richard Feynman", "Marie Curie", "Henrietta Lacks"]
    
    # mutate one or more members of every object
    print("--- Mutating one or more members of every objects [Implicit] ---")
    index = 1
    for ms_obj in list_multi_string:
        # mutate String 2 with a random test case
        test_string = test_cases[rand.randint(0,len(test_cases)-1)]
        print("Mutating Object[" + str(index) 
              + "], String[2] with: ", test_string)
        ms_obj.set_string2(test_string)
        # mutate String 3 with a random test case
        test_string = test_cases[rand.randint(0,len(test_cases)-1)]
        print("Mutating Object[" + str(index) 
              + "], String[3] with: ", test_string)
        ms_obj.set_string3(test_string)
        # prep next object index
        print()
        index += 1   
    
    # display all objects a second time
    print("--- Displaying all MultipleString objects after mutators ---")
    index = 1
    for ms_obj in list_multi_string:
        print("Object[" + str(index) + "]: ", ms_obj.to_string())
        index += 1
    print()
    
    # complete two explicit mutator tests, with true and false output
    print("--- Mutating one or more members of every objects [Explicit] ---")
    index = 1
    for ms_obj in list_multi_string:
        # mutate String 2 with a random test case
        test_string = test_cases[rand.randint(0,len(test_cases)-1)]
        print("Mutating Object[" + str(index) 
              + "], String[2] with: ", test_string)
        if ms_obj.set_string2(test_string) is False:
            print(">>> Status: Invalid mutation.")
        else:
            print(">>> Status: Success")
        # mutate String 3 with a random test case
        test_string = test_cases[rand.randint(0,len(test_cases)-1)]
        print("Mutating Object[" + str(index) 
              + "], String[2] with: ", test_string)
        if ms_obj.set_string2(test_string) is False:
            print(">>> Status: Invalid mutation.")
        else:
            print(">>> Status: Success")
        # prep next object index
        print()
        index += 1  

    # display all objects a third time
    print("--- Displaying all MultipleString objects after mutators ---")
    index = 1
    for ms_obj in list_multi_string:
        print("Object[" + str(index) + "]: ", ms_obj.to_string())
        index += 1
    print()
    
    # make accessor calls
    print("--- Accessing one or more members of every objects ---")
    index = 1
    for ms_obj in list_multi_string:
        # get String 1
        output_string = ms_obj.get_string1()
        print("Getting Object[" + str(index) + "], String[1]: ", output_string)
        # get String 2
        output_string = ms_obj.get_string2()
        print("Getting Object[" + str(index) + "], String[2]: ", output_string)
        # get String 3
        output_string = ms_obj.get_string3()
        print("Getting Object[" + str(index) + "], String[3]: ", output_string)
        # prep next object index
        print()
        index += 1 

    print("*** End of program. ***")

if __name__ == "__main__":
    main()
    

""" ---------- RUN ----------

    ---------- RUN #1 ----------

--- Displaying all MultipleString objects ---
Object[1]:  [apple, orange, pear]
Object[2]:  [egg, bacon, milk]
Object[3]:  [even, odd, (undefined)]
Object[4]:  [(undefined), (undefined), (undefined)]

--- Mutating one or more members of every objects [Implicit] ---
Mutating Object[1], String[2] with:  123
Mutating Object[1], String[3] with:  123

Mutating Object[2], String[2] with:  
Mutating Object[2], String[3] with:  

Mutating Object[3], String[2] with:  123
Mutating Object[3], String[3] with:  Marie Curie

Mutating Object[4], String[2] with:  
Mutating Object[4], String[3] with:  Richard Feynman

--- Displaying all MultipleString objects after mutators ---
Object[1]:  [apple, 123, 123]
Object[2]:  [egg, bacon, milk]
Object[3]:  [even, 123, Marie Curie]
Object[4]:  [(undefined), (undefined), Richard Feynman]

--- Mutating one or more members of every objects [Explicit] ---
Mutating Object[1], String[2] with:  *
Status: Success
Mutating Object[1], String[2] with:  123
Status: Success

Mutating Object[2], String[2] with:  !@#$%^&*()_+
Status: Success
Mutating Object[2], String[2] with:  Stephen Hawking
Status: Success

Mutating Object[3], String[2] with:  
Status: Invalid mutation.
Mutating Object[3], String[2] with:  Richard Feynman
Status: Success

Mutating Object[4], String[2] with:  *
Status: Success
Mutating Object[4], String[2] with:  Richard Feynman
Status: Success

--- Displaying all MultipleString objects after mutators ---
Object[1]:  [apple, 123, 123]
Object[2]:  [egg, Stephen Hawking, milk]
Object[3]:  [even, Richard Feynman, Marie Curie]
Object[4]:  [(undefined), Richard Feynman, Richard Feynman]

--- Accessing one or more members of every objects ---
Getting Object[1], String[1]:  apple
Getting Object[1], String[2]:  123
Getting Object[1], String[3]:  123

Getting Object[2], String[1]:  egg
Getting Object[2], String[2]:  Stephen Hawking
Getting Object[2], String[3]:  milk

Getting Object[3], String[1]:  even
Getting Object[3], String[2]:  Richard Feynman
Getting Object[3], String[3]:  Marie Curie

Getting Object[4], String[1]:  (undefined)
Getting Object[4], String[2]:  Richard Feynman
Getting Object[4], String[3]:  Richard Feynman

*** End of program. ***
   
    ---------- RUN #2 ----------
    
--- Displaying all MultipleString objects ---
Object[1]:  [apple, orange, pear]
Object[2]:  [egg, bacon, milk]
Object[3]:  [even, odd, (undefined)]
Object[4]:  [(undefined), (undefined), (undefined)]

--- Mutating one or more members of every objects [Implicit] ---
Mutating Object[1], String[2] with:  Richard Feynman
Mutating Object[1], String[3] with:  Richard Feynman

Mutating Object[2], String[2] with:  
Mutating Object[2], String[3] with:  

Mutating Object[3], String[2] with:  *
Mutating Object[3], String[3] with:  Richard Feynman

Mutating Object[4], String[2] with:  
Mutating Object[4], String[3] with:  Marie Curie

--- Displaying all MultipleString objects after mutators ---
Object[1]:  [apple, Richard Feynman, Richard Feynman]
Object[2]:  [egg, bacon, milk]
Object[3]:  [even, *, Richard Feynman]
Object[4]:  [(undefined), (undefined), Marie Curie]

--- Mutating one or more members of every objects [Explicit] ---
Mutating Object[1], String[2] with:  Richard Feynman
Status: Success
Mutating Object[1], String[2] with:  Richard Feynman
Status: Success

Mutating Object[2], String[2] with:  Henrietta Lacks
Status: Success
Mutating Object[2], String[2] with:  !@#$%^&*()_+
Status: Success

Mutating Object[3], String[2] with:  123
Status: Success
Mutating Object[3], String[2] with:  !@#$%^&*()_+
Status: Success

Mutating Object[4], String[2] with:  Henrietta Lacks
Status: Success
Mutating Object[4], String[2] with:  Richard Feynman
Status: Success

--- Displaying all MultipleString objects after mutators ---
Object[1]:  [apple, Richard Feynman, Richard Feynman]
Object[2]:  [egg, !@#$%^&*()_+, milk]
Object[3]:  [even, !@#$%^&*()_+, Richard Feynman]
Object[4]:  [(undefined), Richard Feynman, Marie Curie]

--- Accessing one or more members of every objects ---
Getting Object[1], String[1]:  apple
Getting Object[1], String[2]:  Richard Feynman
Getting Object[1], String[3]:  Richard Feynman

Getting Object[2], String[1]:  egg
Getting Object[2], String[2]:  !@#$%^&*()_+
Getting Object[2], String[3]:  milk

Getting Object[3], String[1]:  even
Getting Object[3], String[2]:  !@#$%^&*()_+
Getting Object[3], String[3]:  Richard Feynman

Getting Object[4], String[1]:  (undefined)
Getting Object[4], String[2]:  Richard Feynman
Getting Object[4], String[3]:  Marie Curie

*** End of program. ***   

    ---------- RUN #3 ----------
    
--- Displaying all MultipleString objects ---
Object[1]:  [apple, orange, pear]
Object[2]:  [egg, bacon, milk]
Object[3]:  [even, odd, (undefined)]
Object[4]:  [(undefined), (undefined), (undefined)]

--- Mutating one or more members of every objects [Implicit] ---
Mutating Object[1], String[2] with:  !@#$%^&*()_+
Mutating Object[1], String[3] with:  !@#$%^&*()_+

Mutating Object[2], String[2] with:  !@#$%^&*()_+
Mutating Object[2], String[3] with:  Stephen Hawking

Mutating Object[3], String[2] with:  Henrietta Lacks
Mutating Object[3], String[3] with:  Marie Curie

Mutating Object[4], String[2] with:  
Mutating Object[4], String[3] with:  Marie Curie

--- Displaying all MultipleString objects after mutators ---
Object[1]:  [apple, !@#$%^&*()_+, !@#$%^&*()_+]
Object[2]:  [egg, !@#$%^&*()_+, Stephen Hawking]
Object[3]:  [even, Henrietta Lacks, Marie Curie]
Object[4]:  [(undefined), (undefined), Marie Curie]

--- Mutating one or more members of every objects [Explicit] ---
Mutating Object[1], String[2] with:  *
Status: Success
Mutating Object[1], String[2] with:  !@#$%^&*()_+
Status: Success

Mutating Object[2], String[2] with:  
Status: Invalid mutation.
Mutating Object[2], String[2] with:  123
Status: Success

Mutating Object[3], String[2] with:  123
Status: Success
Mutating Object[3], String[2] with:  *
Status: Success

Mutating Object[4], String[2] with:  
Status: Invalid mutation.
Mutating Object[4], String[2] with:  *
Status: Success

--- Displaying all MultipleString objects after mutators ---
Object[1]:  [apple, !@#$%^&*()_+, !@#$%^&*()_+]
Object[2]:  [egg, 123, Stephen Hawking]
Object[3]:  [even, *, Marie Curie]
Object[4]:  [(undefined), *, Marie Curie]

--- Accessing one or more members of every objects ---
Getting Object[1], String[1]:  apple
Getting Object[1], String[2]:  !@#$%^&*()_+
Getting Object[1], String[3]:  !@#$%^&*()_+

Getting Object[2], String[1]:  egg
Getting Object[2], String[2]:  123
Getting Object[2], String[3]:  Stephen Hawking

Getting Object[3], String[1]:  even
Getting Object[3], String[2]:  *
Getting Object[3], String[3]:  Marie Curie

Getting Object[4], String[1]:  (undefined)
Getting Object[4], String[2]:  *
Getting Object[4], String[3]:  Marie Curie

*** End of program. ***
"""