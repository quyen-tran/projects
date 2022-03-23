"""
@author: Quyen Duchesneau
@subject: Foothill CS003A
@assignment: Lab Assignment 9 - World Series Champions
@date: March 7, 2022
"""

# ---------- SOURCE ----------

def read_data():
    """
    Read in file, strip away '\n', and output list of winners while checking
    for IOError
    @return winners_list list of World Series winners
    """
    file_path = "WorldSeriesWinners.txt"
    winners_list = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                winners_list.append(line.strip('\n'))
    except IOError as e:
        print(e)
    return winners_list

def make_dictionaries(winners_list):
    """
    Make [year : team] and [team : number of wins] dictionaries
    @param winners_list list of winners
    @return year_dict dictionary of year [key] and team [value]
    @return win_dict dictionary of team [key] and number of wins [value]
    """
    # initialize variables
    start_year = 1903
    end_year = 2021
    current_year = start_year
    list_index = 0
    count = 0
    
    year_dict = {}
    win_dict = {}
    
    # get the non-played years
    exclude_years = []
    
    for winner in winners_list:
        if "World Series Not Played" in winner:
            exclude_years.append(get_numeric_in_string(winner))
    
    # create [year : team] dictionary
    for year in range(start_year, end_year + 1):
        if year not in exclude_years:
            year_dict[year] = winners_list[list_index]
        current_year += 1
        list_index += 1

    unique_teams = no_duplicates(year_dict)
    
    # create [team : number of wins] dictionary
    for team in unique_teams:
        for winner in winners_list:
            if team == winner:
                count += 1
        win_dict[team] = count
        count = 0
        
    return year_dict, win_dict
        
def no_duplicates(year_dict):
    """
    Convert dictionary to set of unique teams
    @return set of unique teams
    """
    return set(year_dict.values())

def create_file_no_duplicates(win_dict):
    """
    Write output to binary file
    @param win_dict dictionary of [team : number of wins]
    """
    file_path = "WorldSeriesWinnersND.txt"
    with open(file_path, 'wb') as file:
        try:
            for team, win in win_dict.items():
                output_string = " ".join(str(i) for i in [team, win, "\n"])
                file.write(bytes(output_string.encode('ascii')))
        except IOError as e:
            print(e)

def get_numeric_in_string(the_string):
    """
    Helper function to find the numeric values in a string
    @return numeric values in the string (in order)
    """
    numeric = ""
    if the_string:
        for character in the_string:
            if character.isdigit():
                numeric += character
        return int(numeric)
    else:
        return 0   

# Main Program
def main():
    """
    Identify World Series Champion based on year range
    """
    min_year = 1903
    max_year = 2021
    exclude_year = [1904, 1994]
    
    winners_list = read_data()
    year_dict, win_dict = make_dictionaries(winners_list)
    no_dupe = no_duplicates(year_dict)
    create_file_no_duplicates(win_dict)
    
    print("\n*** Output - List of Unique Teams Winning the World Series ***")
    for team in no_dupe:
        print(team)
    
    done = False
    
    while not done:
        user_input = input("Enter a year in the range 1903-2021: ")
    
        if user_input.isdigit():
            year = int(user_input)
            if year < min_year or year > max_year:
                print("The data for year {}"
                      " is not included in our database.".format(year))
            elif year in exclude_year:
                print("There was no World Series in {}.".format(year))
            else:
                winning_team = year_dict[year]
                winning_score = win_dict[winning_team]
                print("The team that won the"" World Series in"
                      " {} is the {}.".format(year, winning_team))
                print("They won the World Series"
                      " {} times.".format(winning_score))
                done = True
        else:
            print("Only positive integer numbers are accepted.")
    
    print("\n*** End of program. ***")

if __name__ == "__main__":
    main()

""" ---------- RUN ----------

    ---------- RUN #1 ----------
    
*** Output - List of Unique Teams Winning the World Series ***
Philadelphia Athletics
Washington Senators
Chicago White Sox
Toronto Blue Jays
Brooklyn Dodgers
Milwaukee Braves
Atlanta Braves
Los Angeles Dodgers
Baltimore Orioles
Cleveland Indians
Washington Nationals
New York Yankees
Boston Red Sox
Anaheim Angels
New York Mets
Florida Marlins
Boston Braves
Detroit Tigers
Chicago Cubs
Huston Astros
St. Louis Cardinals
New York Giants
Oakland Athletics
Cincinnati Reds
San Francisco Giants
Pittsburgh Pirates
Kansas City Royals
Minnesota Twins
Arizona Diamondbacks
Boston Americans
Philadelphia Phillies

Enter a year in the range 1903-2021: rt
Only positive integer numbers are accepted.

Enter a year in the range 1903-2021: 3000
The data for year 3000 is not included in our database.

Enter a year in the range 1903-2021: r5
Only positive integer numbers are accepted.

Enter a year in the range 1903-2021: -1234
Only positive integer numbers are accepted.

Enter a year in the range 1903-2021: 2000
The team that won the World Series in 2000 is the New York Yankees.
They won the World Series 27 times.

*** End of program. ***

    ---------- RUN #2 ----------
    
*** Output - List of Unique Teams Winning the World Series ***
Minnesota Twins
Chicago White Sox
Arizona Diamondbacks
Pittsburgh Pirates
San Francisco Giants
Chicago Cubs
Toronto Blue Jays
Washington Nationals
Philadelphia Athletics
Anaheim Angels
New York Giants
Boston Americans
Milwaukee Braves
Brooklyn Dodgers
Boston Red Sox
Kansas City Royals
Los Angeles Dodgers
St. Louis Cardinals
Huston Astros
Atlanta Braves
Cincinnati Reds
Florida Marlins
Philadelphia Phillies
Oakland Athletics
Washington Senators
Cleveland Indians
New York Mets
Detroit Tigers
Boston Braves
Baltimore Orioles
New York Yankees

Enter a year in the range 1903-2021: -9876
Only positive integer numbers are accepted.

Enter a year in the range 1903-2021: p
Only positive integer numbers are accepted.

Enter a year in the range 1903-2021: 10000
The data for year 10000 is not included in our database.

Enter a year in the range 1903-2021: 1994
There was no World Series in 1994.

Enter a year in the range 1903-2021: 1904
There was no World Series in 1904.

Enter a year in the range 1903-2021: 1907
The team that won the World Series in 1907 is the Chicago Cubs.
They won the World Series 3 times.

*** End of program. ***

"""

