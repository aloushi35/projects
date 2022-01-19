#Ali Fakhreddine
#16632023

class NoStaircaseSizeException(Exception):
    pass
class IntegerOutOfRangeException(Exception):
    pass

def getUserInput():
    while True:
        staircount = input('Please input your staircase size:')
        if staircount == 'DONE':
            done = 'Done Executing'
            return staircount
        stairs = int(staircount)
            
        return stairs
def printSteps(stepCount):
    counter = 0    
    if stepCount == 0:
        raise NoStaircaseSizeException
    if stepCount < 0:
        raise IntegerOutOfRangeException
    if stepCount >= 1000:
        raise IntegerOutOfRangeException


    if stepCount == 1:
        s = '+-+'
        s = s + '\n| |'
        s = s + '\n+-+'
        return s
    elif stepCount > 1000:
        return
    elif stepCount == 0:
        return
    elif stepCount < 1:
        return
    else:
        s = ' '*(2*stepCount-2)+'+-+'
        s = s + '\n' + ' '*(2*stepCount-2)+'| |'
        counter=(stepCount-2)*2
        for j in range(stepCount-2):
            s = s + '\n'+' '*(counter)
            s = s + '+-+-+'
            s = s + '\n' + ' '*(counter)
            s = s + '| |'
            counter=counter-2
        s = s + '\n+-+-+'
        s = s + '\n| |'
        s = s + '\n+-+'
        return s
def runProgram():
    while True:
        try:
            stairs = getUserInput() 
            if stairs == 'DONE':
                done = "Done Executing"
                return done
            drawstairs = printSteps(stairs)
            print(drawstairs)
        except NoStaircaseSizeException:
            print("I cannot draw a staircase with no steps.")
        except IntegerOutOfRangeException:
            print("That staircase size is out of range.")
        except ValueError:
            print("Invalid staircase value entered.")

                                
    
    
    
