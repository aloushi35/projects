#Fakhreddine, Ali

from collections import namedtuple
student = namedtuple("student","fname lname agrade egrade")
def GradeManager():
    "adds information about ICS-31 students and allows to search, edit or sort the info"
    StudentRoster = []
    while True:
        s = input("$ ")
        if s == 'Quit':
            return
        elif s == 'PrintRoster':
            for stud in StudentRoster:
                print(', '.join(stud))
        else:
            x = s.index(' ')
            newstud = s[x+1:].split(', ')
            if s[:x] == 'AddStudent':
                AddStudent = student(newstud[0], newstud[1], newstud[2], newstud[3])
                StudentRoster.append(AddStudent)
            if s[:x] == 'DeleteStudent':
                for stud in StudentRoster:
                    if newstud[0] == stud[0] and newstud[1] == stud[1]:
                        StudentRoster.remove(stud)
                        break
                else:
                    print('Error! No student with that name was found in the roster.')
            if s[:x] == 'FindByFName':
                for stud in StudentRoster:
                    if newstud[0] == stud[0]:
                        print(', '.join(stud))
            if s[:x] == 'FindByLName':
                for stud in StudentRoster:
                    if newstud[0] == stud[1]:
                        print(', '.join(stud))
            if s[:x] == 'GetAverage':
                if 'Assignment' in s:
                    roster_grades = []
                    for stud in StudentRoster:
                        roster_grades.append(int(stud[2]))
                    print(sum(roster_grades)/len(roster_grades))
                if 'Exam' in s:
                    roster_grades1 = []
                    for stud in StudentRoster:
                        roster_grades1.append(int(stud[3]))
                    print(sum(roster_grades1)/len(roster_grades1))
            if s[:x] == 'SortRoster':
                if 'Name' in s:
                    StudentRoster.sort(key = lambda StudentRoster:(StudentRoster[0], StudentRoster[1]))
                if 'Assignment' in s:
                    StudentRoster.sort(key = lambda StudentRoster:StudentRoster[2], reverse = True)
                if 'Exam' in s:
                    StudentRoster.sort(key = lambda StudentRoster:StudentRoster[3], reverse = True)
                for stud in StudentRoster:
                    print(', '.join(stud))
                
