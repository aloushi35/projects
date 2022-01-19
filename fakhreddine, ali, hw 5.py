#Fakhreddine, Ali
def DungeonGame():
    'Movement game that moves through dungeon rooms'
    dungeonlist = []
    load = False
    class Room:
        def __init__(self, roomnumb, descript, nroom, sroom, eroom, wroom):
            self.roomnumb = int(roomnumb)
            self.descript = descript
            self.nroom = int(nroom)
            self.sroom = int(sroom)
            self.eroom = int(eroom)
            self.wroom = int(wroom)
    while True:
        d = input('$ ').split()
        if d[0] == 'Quit':
            return
        elif d[0] == 'LoadDungeon':
            if load == False:
                for entry in open(d[1], 'r'):
                    elist = entry.split('+')
                    print(elist)
                    roomlist = elist[2].lstrip(' ').split(' ')
                    roomnumber = elist[0]
                    description = elist[1]
                    nroom = roomlist[0]
                    sroom = roomlist[1]
                    eroom = roomlist[2]
                    wroom = roomlist[3].rstrip('\n')
                    newroom = Room(roomnumber, description, nroom, sroom, eroom, wroom)
                    dungeonlist.append(newroom)
                    for self in dungeonlist:
                        self.descript
                print(dungeonlist[0].descript)
                currentroom = dungeonlist[0]
                load = True
            else:
                print('Dungeon already loaded!')
        elif d[0] == 'North':
            if currentroom.nroom == -1:
                print('There is no room')
            if currentroom.nroom == -2:
                print('This room is closed')
            else:
                for r in dungeonlist:
                    if r.roomnumb == currentroom.nroom:
                        currentroom = r
                        print(r.descript)
        elif d[0] == 'South':
            if currentroom.sroom == -1:
                print('There is no room')
            if currentroom.sroom == -2:
                print('This room is closed')
            else:
                for sr in dungeonlist:
                    if sr.roomnumb == currentroom.sroom:
                        currentroom = sr
                        print(sr.descript)
        elif d[0] == 'East':
            if currentroom.eroom == -1:
                print('There is no room')
            if currentroom.eroom == -2:
                print('This room is closed')
            else:
                for er in dungeonlist:
                    if er.roomnumb == currentroom.eroom:
                        currentroom = er
                        print(er.descript)
        elif d[0] == 'West':
            if currentroom.wroom == -1:
                print('There is no room')
            if currentroom.wroom == -2:
                print('This room is closed')
            else:
                for wr in dungeonlist:
                    if wr.roomnumb == currentroom.wroom:
                        currentroom = wr
                        print(wr.descript)
        elif d[0] == 'CloseDoor':
            if d[1] == 'North':
                if currentroom.nroom == -1:
                    print('There is no room')
                elif currentroom.nroom == -2:
                    print('This room is closed')
                else:
                    currentroom.nroom = -2
                    print('The door is closed now')
            if d[1] == 'South':
                if currentroom.sroom == -1:
                    print('There is no room')
                elif currentroom.sroom == -2:
                    print('This room is closed')
                else:
                    currentroom.sroom = -2
                    print('The door is closed now')
            if d[1] == 'East':
                if currentroom.eroom == -1:
                    print('There is no room')
                elif currentroom.eroom == -2:
                    print('This room is closed')
                else:
                    currentroom.eroom = -2
                    print('The door is closed now')
            if d[1] == 'West':
                if currentroom.wroom == -1:
                    print('There is no room')
                elif currentroom.wroom == -2:
                    print('This room is closed')
                else:
                    currentroom.wroom = -2
                    print('The door is closed now')
        else:
            print('Invalid input')
