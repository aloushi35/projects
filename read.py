from pathlib import Path
import csv
from sportclub import SportClub
from typing import List, Tuple

def readFile(file: Path) -> List[Tuple[str, str, str]]:
    """Read a CSV file and return its content

    A good CSV file will have the header "City,Team Name,Sport" and appropriate content.

    Args:
        file: a path to the file to be read

    Returns:
        a list of tuples that each contain (city, name, sport) of the SportClub

    Raises:
        ValueError: if the reading csv has missing data (empty fields)  
    """
    readonefile = []
    errors = []
    with open(file, 'r') as survey:
        readsurveydata = csv.reader(survey)
        for surv in readsurveydata:
            readonefile.append(tuple(surv))
        del readonefile[0]
        for data in readonefile:
            for field in data:
                if field == '':
                    raise ValueError
            
        
    
    # TODO: Complete the function
        return readonefile


def readAllFiles() -> List[SportClub]:
    """Read all the csv files in the current working directory to create a list of SportClubs that contain unique SportClubs with their corresponding counts

    Take all the csv files in the current working directory, calls readFile(file) on each of them, and accumulates the data gathered into a list of SportClubs.
    Create a new file called "report.txt" in the current working directory containing the number of good files and good lines read. 
    Create a new file called "error_log.txt" in the current working directory containing the name of the error/bad files read.

    Returns:
        a list of unique SportClub objects with their respective counts
    """

    p = Path('.').glob('*.csv')
    sportlist = []
    errors = []
    countsport = {}
    countfile = 0
    countline = 0
    for file in p:
        try:
            twofiles = readFile(file)
            countfile += 1
            countline += int(len(twofiles))
            sportlist += twofiles
            #filecount = len(list(Path('.').glob('*.csv')))
            #lines = len(list(sportlist))
        except:
            errors.append(str(file))
            with open('error_log.txt', 'w', newline='') as errorfile:
                errorfile.write('\n'.join(errors))
    with open('report.txt', 'w', newline='') as reportfile:
        reportfile.write('Number of files read: ')
        reportfile.write(str(countfile))
        reportfile.write('\nNumber of lines read: ')
        reportfile.write(str(countline))
        reportfile.write('\n')
    for i in sportlist:
        if i in countsport:
            countsport[i].incrementCount()
        else:
            countsport[i] = SportClub(i[0],i[1],i[2],1)
    
    return list(countsport.values())
    # TODO: Complete the function

if __name__ == "__main__":
    print(len(readAllFiles()))
