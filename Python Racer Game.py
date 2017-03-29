def RaceResults (entries): 
   # This is the main function that calls the
   # function ResultsTable that in turn calls
   # the function ReadInput. 
    print('''
Welcome to the Racer Game!

This is a game where you put in the order
that you want some racers to finish in,
and you get to see a table with the results!
''')
    return  ResultsTable (ReadInput(entries))
#####################################################################
def ReadFile (filename):
    # This function unpacks the file 'fileName',
    # and creates the dictionary 'entries' with
    # the key racer number and values name and team
    try:
        entryDict={}
        fileHandle=open(filename,'r')
        for line in fileHandle:
            (k, v1, v2)= line.split()
            entryDict.setdefault(int(k), []).append(v1)
            entryDict.setdefault(int(k), []).append(v2)
    except ValueError:
        fileHandle.close( )
        return entryDict
    except IOError:
        print('''Error in ReadFile: Please use a file with correct entrant
information. You might check your spelling of the file name''')
#####################################################################
def ReadInput (entries):
    # reads the dictionary from ReadFile and returns
    # a lists of winner's data based on user input. It also
    # creates 4 lists that are then zipped into a final list
    # for use in the next fuction
    d=ReadFile (entries)
    racerNumberList=[]
    racerScore=[]
    winnersDict={}
    order=0
    listOfTeams=[]
    listOfFinishers=[]
    listOfPlaces=[]
    listOfNames=[]
    placeFirstList=()
    sumofwinningteam=0
    winningteammembers=[]
    countOfSum=0
    try:
        while True:
            racerNumberList=list(d.keys())
            racerNumber = int(input('''
Please enter the number of a racer,
in the order that they finished the race,
so the first racer you enter is the winner and so on.

Please use the racer numbers 150-180.

When you are finished enter the number '0' (zero) to stop.
 
'''))
            if racerNumber in racerNumberList and racerNumber !=0 and racerNumber not in racerScore:
                racerScore.append(racerNumber)
                for racer in racerScore:
                    winnersDict.setdefault(racer,d[racer])
                order+=1
                winnersDict[racer].append(order)
                for i in sorted(winnersDict.items()):
                    if i[0] not in listOfFinishers:
                        listOfTeams.append(i[1][1])
                        listOfFinishers.append(i[0])
                        listOfPlaces.append(i[1][2])
                        listOfNames.append(i[1][0])
                placeFirstList=sorted(set(zip(listOfPlaces,listOfTeams, listOfFinishers, listOfNames)))
                for colr in listOfTeams:
                    if listOfTeams.count(colr)>=3:
                        for i in sorted(placeFirstList):
                            if i[1]==colr:
                                winningteammembers.append(i[3])
                                if countOfSum<3:
                                    sumofwinningteam+=i[0]
                                    countOfSum+=1
                        print('''
Congratulations! There is a winner.
3 team members have finished and thier scores are:

SCORE = %s TEAM = %s: %s, %s, %s''' %(sumofwinningteam,colr,winningteammembers[0],winningteammembers[1],winningteammembers[2]))
                        break
            elif racerNumber not in racerNumberList and racerNumber !=0:
                print('''
*** Error in RaceResults: invalid number
- the racer number was not between 150-180.

''')
            elif racerNumber in racerScore:
                print('''
*** This number was already entered

''')
                continue
            else: # player entered '0'
                print('''
Great: you finished entering in the race results.
''')
                return placeFirstList
                break
    except ValueError :
        print('''*** Error in RaceResults: a racer number was
not entered. Please run again and enter valid racer numbers.''')
#####################################################################
def ResultsTable (placeFirstList):
    finalTableLst=[]
    teamScores={}
    teams={}
    scoringMembers={}
    listOfTeamsThatFinished=[]
    teamswith3ormorefinishers=[]
    teamMembers={}
    ivteamScores={}
    finalList=[]
    lowScore=0
    place=0
    for i in placeFirstList:
        teamName = i[1]
        if teamName not in teams:
            teams[teamName]=[(i[3],i[0])]
            #  team name as key: list tuples of (racer name, racer score)
        else:
            if len(teams[teamName]) != 3:
                teams[teamName] += [(i[3],i[0])]
    for team, lst in teams.items():
        if len(lst)==3:
            currentScore=0
            for tup in lst:
                currentScore+=tup[1]
                teamMembers.setdefault(team, []).append(tup[0])
                # creates a dict of teams : their members
                teamScores[team]=currentScore
                # creates dict team: score
    for key in (teamScores.keys()):
        ivteamScores[(teamScores[key])]=key        
    for score, teamm in sorted(ivteamScores.items()):
        if score==lowScore:
            finalList.append([place, score, teamm])
        else:
            place+=1
            finalList.append([place, score, teamm])
            score=lowScore
    print('''Here is a table of the top 3 from each team with 3 or more finishers:

%-3s %-6s %-6s %-1s''' % ( 'PLACE','SCORE','TEAM','SCORING MEMBERS'))
    for final in finalList:
        placeFinal=final[0]
        scoreFinal=final[1]
        teamFinal=final[2]
        first=teamMembers[teamFinal][0]
        second=teamMembers[teamFinal][1]
        third=teamMembers[teamFinal][2]
        print('%3i %5i %8s %6s %3s %3s'
              %(placeFinal, scoreFinal, teamFinal, first, second, third ))
    print('''
I hope you had fun, please play again !''')
#####################################################################
# use " RaceResults ('entries.txt') " in the shell when running the function
# if you do not have this file, here it is the text:
# 150 Jeff Green
# 151 Jack Green
# 152 Ned Green
# 153 Harry Green
# 154 Jim Green
# 155 John Green
# 156 Frank Green
# 157 Aeon Green
# 158 Amy Blue
# 159 Jackie Blue
# 160 Wonda Blue
# 161 Rhonda Blue
# 162 Paula Blue
# 163 Jamie Blue
# 164 Greda Blue
# 165 Edith Blue
# 166 Sam White
# 167 Amy White
# 168 Peg White
# 169 Jim White
# 170 Pam White
# 171 Ken White
# 172 Liz White
# 173 Dan White
# 174 Leo Red
# 175 Sue Red
# 176 Tim Red
# 177 Una Red
# 178 Pat Red
# 179 Yan Red
# 180 Ian Red

