#Fakhreddine, Ali

from collections import namedtuple
student = namedtuple("student","fname lname agrade egrade")
def GradeManager():
    "adds information about ICS-31 students and allows to search, edit or sort the info"
    roster = []
    while True:
        s = input("$ ")
        if s == 'Quit':
            return
        elif s == 'PrintRoster':
            for stud in roster:
                print(', '.join(stud))
        else:
            x = s.index(' ')
            newstud = s[x+1:].split(', ')
            if s[:x] == 'AddStudent':
                AddStudent = student(newstud[0], newstud[1], newstud[2], newstud[3])
                roster.append(AddStudent)
                print(roster)
            if s[:x] == 'DeleteStudent':
                for stud in roster:
                    if newstud[0] == stud[0] and newstud[1] == stud[1]:
                        roster.remove(stud)
                        break
                else:
                    print('Error! No student with that name was found in the roster.')
            if s[:x] == 'FindByFName':
                for stud in roster:
                    if newstud[0] == stud[0]:
                        print(', '.join(stud))
            if s[:x] == 'FindByLName':
                for stud in roster:
                    if newstud[0] == stud[1]:
                        print(', '.join(stud))
            if s[:x] == 'GetAverage':
                if 'Assignment' in s:
                    roster_grades = []
                    for stud in roster:
                        roster_grades.append(int(stud[2]))
                    print(sum(roster_grades)/len(roster_grades))
                if 'Exam' in s:
                    roster_grades1 = []
                    for stud in roster:
                        roster_grades1.append(int(stud[3]))
                    print(sum(roster_grades1)/len(roster_grades1))
            if s[:x] == 'SortRoster':
                if 'Name' in s:
                    roster.sort(key = lambda roster:(roster[0], roster[1]))
                if 'Assignment' in s:
                    roster.sort(key = lambda roster:roster[2], reverse = True)
                if 'Exam' in s:
                    roster.sort(key = lambda roster:roster[3], reverse = True)
                for stud in roster:
                    print(', '.join(stud))
                
