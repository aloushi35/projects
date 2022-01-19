import csv
from sportclub import SportClub
from typing import List, Iterable

def separateSports(all_clubs: List[SportClub]) -> Iterable[List[SportClub]]:
    """Separate a list of SportClubs into their own sports

    For example, given the list [SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA"), SportClub("LA", "Angels", "MLB")],
    return the iterable [[SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA")], [SportClub("LA", "Angels", "MLB")]]

    Args:
        all_clubs: A list of SportClubs that contain SportClubs of 1 or more sports.

    Returns:
        An iterable of lists of sportclubs that only contain clubs playing the same sport. 
    """
    list_of_lists = all_clubs
    uniquesport = set([i.getSport() for i in all_clubs])
    group_list = [[i for i in list_of_lists if i.getSport() == sport] for sport in uniquesport]
    return group_list
    
    # TODO: Complete the function


def sortSport(sport: List[SportClub]) -> List[SportClub]:
    """Sort a list of SportClubs by the inverse of their count and their name

    For example, given the list [SportClub("Houston", "Rockets", "NBA", 80), SportClub("LA", "Warriors", "NBA", 130), SportClub("LA", "Lakers", "NBA", 130)] 
    return the list [SportClub("LA", "Lakers", "NBA", 130), SportClub("LA", "Warriors", "NBA", 130), SportClub("Houston", "Rockets", "NBA", 80)]

    Args:
        sport: A list of SportClubs that only contain clubs playing the same sport

    Returns:
        A sorted list of the SportClubs  
    """
    reverselist = []
    reverse = sorted(sport, reverse = True)
    for i in reverse:
        reverselist.append(i)
    return reverselist
    # TODO: Complete the function
    # hint: check documentation for sorting lists 
    # ( https://docs.python.org/3/library/functions.html#sorted , https://docs.python.org/3/howto/sorting.html#sortinghowto )


def outputSports(sorted_sports: Iterable[List[SportClub]]) -> None:
    """Create the output csv given an iterable of list of sorted clubs

    Create the csv "survey_database.csv" in the current working directory, and output the information:
    "City,Team Name,Sport,Number of Times Picked" for the top 3 teams in each sport.

    Args:
        sorted_sports: an Iterable of different sports, each already sorted correctly
    """
    #listofsports = sortSport('sport')
    
    print(sorted_sports)       
    with open('survey_database.csv', 'w', newline='') as myCSVFile:
        writeToMyCSV = csv.writer(myCSVFile)
        writeToMyCSV.writerow(['City','Team Name','Sport','Number of Times Picked'])

        for i in sorted_sports:
            for j in i[:3]:
                survey = []
                survey.append(j.getCity())
                survey.append(j.getName())
                survey.append(j.getSport())
                survey.append(j.getCount())
                writeToMyCSV.writerow(survey)
    # TODO: Complete the function
