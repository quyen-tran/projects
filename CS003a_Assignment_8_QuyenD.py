"""
@author: Quyen Duchesneau
@subject: Foothill CS003A
@assignment: Lab Assignment 8 - Computer Dating
@date: March 1, 2022
"""

# ---------- SOURCE ----------


class DateProfile:
    # define global variables
    MIN_NUMBER = 0
    MAX_NUMBER = 10
    MIN_NAME_LEN = 0
    MAX_NAME_LEN = 50
    DEFAULT_GEND = "F"
    DEFAULT_SEARCH_GEND = "F"
    DEFAULT_FIT_NUMBER = 0
    DEFAULT_NAME = "Jane Doe"
    
    # constructor method
    def __init__(self, gender, gender_search, romance, finance, dist, name):
        """
        Construct DateProfile instance
        """
        self.set_all(gender, gender_search, romance, finance, dist, name)
    
    # mutator ("set") methods
    def set_gender(self, gender):
        """
        Set gender class parameter
        """
        if self.valid_gender(gender):
            print(gender, "accepted as gender")
            self._gender = gender
        else:
            print(gender, "rejected as gender")
            self._gender = self.DEFAULT_GEND

    def set_gender_search(self, gender):
        """
        Set gender search class parameter
        """
        if self.valid_gender(gender):
            print(gender, "accepted as search gender")
            self._gender_search = gender
        else:
            print(gender, "rejected as search gender")
            self._gender_search = self.DEFAULT_SEARCH_GEND
            
    def set_romance(self, romance):
        """
        Set romance class parameter
        """
        if self.valid_number(romance):
            print(romance, "accepted as romance")
            self._romance = romance
        else:
            print(romance, "rejected as romance")
            self._romance = self.DEFAULT_FIT_NUMBER
            
    def set_finance(self, finance):
        """
        Set finance class parameter
        """
        if self.valid_number(finance):
            print(finance, "accepted as finance")
            self._finance = finance
        else:
            print(finance, "rejected as finance")
            self._finance = self.DEFAULT_FIT_NUMBER

    def set_distance(self, distance):
        """
        Set distance class parameter
        """
        if self.valid_number(distance):
            print(distance, "accepted as distance")
            self._distance = distance
        else:
            print(distance, "rejected as distance")
            self._distance = self.DEFAULT_FIT_NUMBER
    
    def set_name(self, name):
        """
        Set name class parameter
        """
        if self.valid_string(name):
            print(name, "accepted as name")
            self._name = name
        else:
            print(name, "rejected as name")
            self._name = self.DEFAULT_NAME
        
    def set_all(self, gender, gender_search, romance, finance, distance, name):
        """
        Set all six class parameters to input values or default if invalid
        """
        if self.valid_gender(gender):
            self._gender = gender
        else:
            self._gender = self.DEFAULT_GEND
            
        if self.valid_gender(gender_search):
            self._gender_search = gender_search
        else:
            self._gender_search = self.DEFAULT_SEARCH_GEND
            
        if self.valid_number(romance):
            self._romance = romance
        else:
            self._romance = self.DEFAULT_FIT_NUMBER
            
        if self.valid_number(finance):
            self._finance = finance
        else:
            self._finance = self.DEFAULT_FIT_NUMBER
            
        if self.valid_number(distance):
            self._distance = distance
        else:
            self._distance = self.DEFAULT_FIT_NUMBER
            
        if self.valid_string(name):
            self._name = name
        else:
            self._name = self.DEFAULT_NAME
        
    def set_defaults(self):
        """
        Set all six class parameters to default
        """
        self._gender = self.DEFAULT_GEND
        self._gender_search = self.DEFAULT_SEARCH_GEND
        self._romance = self.DEFAULT_FIT_NUMBER
        self._finance = self.DEFAULT_FIT_NUMBER
        self._distance = self.DEFAULT_FIT_NUMBER
        self._name = self.DEFAULT_NAME
    
    # accessor ("get") methods
    def get_gender(self):
        """
        @return gender class parameter
        """
        return self._gender.upper() 

    def get_gender_search(self):
        """
        @return gender search class parameter
        """
        return self._gender_search.upper()
    
    def get_romance(self):
        """
        @return romance class parameter
        """
        return self._romance
    
    def get_finance(self):
        """
        @return finance class parameter
        """
        return self._finance
    
    def get_distance(self):
        """
        @return distance class parameter
        """
        return self._distance
    
    def get_name(self):
        """
        @return name class parameter
        """
        return self._name
    
    def fit_value(self, partner):
        """
        @return fit value calculate from the average of fit parameters
        """
        gender_fit = self.determine_gender_fit(partner)
        if not gender_fit:
            return 0.0
        else:
            fit_values = [self.determine_romance_fit(partner), 
                          self.determine_finance_fit(partner), 
                          self.determine_distance_fit(partner)]
            return (sum(fit_values) / len(fit_values))
    
    # helper methods
    def interpolate_fit(self, delta):
        """
        Determine fit value from difference delta
        @return
        """
        
        # generate slope intercept equation for:
        # highest fit when delta is MIN_NUMBER >>> (0, 1)
        # lowest fit when delta is MAX_NUMBER - 1 >>> (MAX_NUMBER - 1, 0.1)
        y_intercept = 1.0
        y_1 = 1.0
        y_2 = 0.1
        slope = (y_2 - y_1)/((self.MAX_NUMBER - 1) - self.MIN_NUMBER)
        fit_value = slope * delta + y_intercept
        return fit_value
    
    def determine_gender_fit(self, partner):
        """
        Checks whether partner's gender fit gender search criteria
        @return 0 for not a good fit, 1 for a good fit
        """
        return (int(self.get_gender_search() == partner.get_gender()) and 
                int(self.get_gender() == partner.get_gender_search()))

    def determine_romance_fit(self, partner):
        """
        Calculate the fit value for partner's romance parameter against self
        @return interpolated fit value
        """
        delta = abs(partner.get_romance() - self.get_romance())
        return self.interpolate_fit(delta)

    def determine_finance_fit(self, partner):
        """
        Calculate the fit value for partner's finance parameter against self
        @return interpolated fit value
        """
        delta = abs(partner.get_finance() - self.get_finance())
        return self.interpolate_fit(delta)
        
    def determine_distance_fit(self, partner):
        """
        Calculate the fit value for partner's distance parameter against self
        @return interpolated fit value
        """
        delta = abs(partner.get_distance() - self.get_distance())
        return self.interpolate_fit(delta)

    def valid_string(cls, the_str):
        """
        Check validity of input string against length limits; empty string is 
        not valid
        @return isValid
        """
        return (len(the_str) > cls.MIN_NAME_LEN and 
                 len(the_str) <= cls.MAX_NAME_LEN)
     
    def valid_number(cls, the_val):
        """
        Check validity of input value against finance/romance range limits
        @return isValid
        """
        return (the_val >= cls.MIN_NUMBER and the_val <= cls.MAX_NUMBER)

    def valid_gender(self, gender):
        """
        Check validity of gender input
        @return True/False
        """
        return (gender.upper() == "M" or gender.upper() == "F")

    def __str__(self):
        """
        Output class parameters to string
        """
        return self.to_string()
         
    def to_string(self):
        """
        Output class parameters to string
        """
        output = "{}({}) searching for ({}), w/ rom={}, fin={}, and dist={}."
        return output.format(self.get_name(), self.get_gender(), 
                             self.get_gender_search(), self.get_romance(), 
                             self.get_finance(), self.get_distance())


# define global scope functions
def display_two_profiles(profile1, profile2):
    """
    Display fit value between two DateProfiles
    """
    profile1_name = profile1.get_name()
    profile2_name = profile2.get_name()
    fit_value = round(profile1.fit_value(profile2), 3)
    profile_string = "Fit between {} and {}:".format(profile1_name, 
                                                     profile2_name)
    fit_string = "{fit: .3f}".format(fit = fit_value)
    output = "{:<50} {:<50}".format(profile_string, fit_string)
    print(output)

# Main Program
def main():
    """
    Simulates a dating platform between different profiles
    """
    print("\n*** Welcome to Computer Dating! ***")
    
    print("\n*** Part 1: Four Simple Objects without Loops ***\n")
    
    # create DateProfile objects
    profile1 = DateProfile("f", "f", 9, 5, 3, "Sarah Somebody")
    profile2 = DateProfile("m", "f", 10, 2, 9, "Steve Nobody")
    profile3 = DateProfile("f", "f", 2, 9, 1, "Jane Peabody")
    profile4 = DateProfile("f", "m", 7, 3, 10, "Helen Anybody")
    
    # display profile information
    print("Date profile:\n ", profile1.to_string())
    print("Date profile:\n ", profile2.to_string())
    print("Date profile:\n ", profile3.to_string())
    print("Date profile:\n ", profile4.to_string())
    
    # display fit information
    
    # fit against profile 1
    print()
    display_two_profiles(profile1, profile1)
    display_two_profiles(profile1, profile2)
    display_two_profiles(profile1, profile3)
    display_two_profiles(profile1, profile4)
    
    # fit against profile 2
    print()
    display_two_profiles(profile2, profile1)
    display_two_profiles(profile2, profile2)
    display_two_profiles(profile2, profile3)
    display_two_profiles(profile2, profile4)
    
    # fit against profile 3
    print()
    display_two_profiles(profile3, profile1)
    display_two_profiles(profile3, profile2)
    display_two_profiles(profile3, profile3)
    display_two_profiles(profile3, profile4)
    
    # fit against profile 4
    print()
    display_two_profiles(profile4, profile1)
    display_two_profiles(profile4, profile2)
    display_two_profiles(profile4, profile3)
    display_two_profiles(profile4, profile4)
    
    # testing mutators
    print("\nTesting mutators:")
    test = DateProfile("m", "m", 1, 1, 1, "tester")
    print(test.to_string())
    test.set_gender("Q")
    test.set_gender_search("f")
    test.set_romance(-5)
    test.set_finance(3)
    test.set_distance(11)
    test.set_name("")
    print(test.to_string())
    
    print("\n*** Part 2: Four Simple Objects with Lists and Loops ***")
    
    # create DateProfile list
    profile_list = [profile1, profile2, profile3, profile4]
    
    # display profile information
    print()
    for profile in profile_list:
        print("Date profile:\n", profile.to_string())

    # display fit information
    for i in range(len(profile_list)):
        print()
        for j in range(len(profile_list)):
            display_two_profiles(profile_list[i], profile_list[j])
        
    print("\n*** End of program. ***")

if __name__ == "__main__":
    main()

""" ---------- RUN ----------

*** Welcome to Computer Dating! ***

*** Part 1: Four Simple Objects without Loops ***

Date profile:
  Sarah Somebody(F) searching for (F), w/ rom=9, fin=5, and dist=3.
Date profile:
  Steve Nobody(M) searching for (F), w/ rom=10, fin=2, and dist=9.
Date profile:
  Jane Peabody(F) searching for (F), w/ rom=2, fin=9, and dist=1.
Date profile:
  Helen Anybody(F) searching for (M), w/ rom=7, fin=3, and dist=10.

Fit between Sarah Somebody and Sarah Somebody:      1.000                                            
Fit between Sarah Somebody and Steve Nobody:        0.000                                            
Fit between Sarah Somebody and Jane Peabody:        0.567                                            
Fit between Sarah Somebody and Helen Anybody:       0.000                                            

Fit between Steve Nobody and Sarah Somebody:        0.000                                            
Fit between Steve Nobody and Steve Nobody:          0.000                                            
Fit between Steve Nobody and Jane Peabody:          0.000                                            
Fit between Steve Nobody and Helen Anybody:         0.833                                            

Fit between Jane Peabody and Sarah Somebody:        0.567                                            
Fit between Jane Peabody and Steve Nobody:          0.000                                            
Fit between Jane Peabody and Jane Peabody:          1.000                                            
Fit between Jane Peabody and Helen Anybody:         0.000                                            

Fit between Helen Anybody and Sarah Somebody:       0.000                                            
Fit between Helen Anybody and Steve Nobody:         0.833                                            
Fit between Helen Anybody and Jane Peabody:         0.000                                            
Fit between Helen Anybody and Helen Anybody:        0.000                                            

Testing mutators:
tester(M) searching for (M), w/ rom=1, fin=1, and dist=1.
Q rejected as gender
f accepted as search gender
-5 rejected as romance
3 accepted as finance
11 rejected as distance
 rejected as name
Jane Doe(F) searching for (F), w/ rom=0, fin=3, and dist=0.

*** Part 2: Four Simple Objects with Lists and Loops ***

Date profile:
 Sarah Somebody(F) searching for (F), w/ rom=9, fin=5, and dist=3.
Date profile:
 Steve Nobody(M) searching for (F), w/ rom=10, fin=2, and dist=9.
Date profile:
 Jane Peabody(F) searching for (F), w/ rom=2, fin=9, and dist=1.
Date profile:
 Helen Anybody(F) searching for (M), w/ rom=7, fin=3, and dist=10.

Fit between Sarah Somebody and Sarah Somebody:      1.000                                            
Fit between Sarah Somebody and Steve Nobody:        0.000                                            
Fit between Sarah Somebody and Jane Peabody:        0.567                                            
Fit between Sarah Somebody and Helen Anybody:       0.000                                            

Fit between Steve Nobody and Sarah Somebody:        0.000                                            
Fit between Steve Nobody and Steve Nobody:          0.000                                            
Fit between Steve Nobody and Jane Peabody:          0.000                                            
Fit between Steve Nobody and Helen Anybody:         0.833                                            

Fit between Jane Peabody and Sarah Somebody:        0.567                                            
Fit between Jane Peabody and Steve Nobody:          0.000                                            
Fit between Jane Peabody and Jane Peabody:          1.000                                            
Fit between Jane Peabody and Helen Anybody:         0.000                                            

Fit between Helen Anybody and Sarah Somebody:       0.000                                            
Fit between Helen Anybody and Steve Nobody:         0.833                                            
Fit between Helen Anybody and Jane Peabody:         0.000                                            
Fit between Helen Anybody and Helen Anybody:        0.000                                            

*** End of program. ***
"""