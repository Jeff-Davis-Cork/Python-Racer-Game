# Python-Racer-Game
This is my python effort to show a race in which the score of each entrant is the place in which they finish, and the score of a team is the sum of the scores of its first three finishers. Any finishers from a team after the third do not contribute to that team’s score; teams with fewer than three finishers are eliminated.

The team with the lowest overall score places first, that with the next lowest score places second, and so forth. Registration data for all entrants is stored in a file, with each line consisting of the racer number, personal name, and team name for that entrant; for example:
152 Ned Green
117 Amy Blue
213 Jim Green

I have assumed that both personal names and team names are single words. Racer numbers are all distinct; personal and team names need not be.The Python program first reads in this data file, and then read in from the keyboard, one per line, the racer numbers of entrants in the order in which they finish. Invalid race numbers trigger an error message, but otherwise are skipped. The number 0 signals the end of the keyboard input.

As soon as the third member of any team finishes, the program outputs the team score, its name, and the names of its three scoring members in their finishing order; for example:

SCORE = 15 TEAM = Green : Jim, Pam, Ken

The program finally outputs a table containing, for each team with three or more finishers, the team place, its score, its name, and the names of its scoring members, sorted in increasing order of team place, where teams on equal scores are given the same place; for example:

PLACE SCORE TEAM SCORING MEMBERS
 1     6     Blue  Sam, Amy, Peg
 2    21     Green  Jim, Pam, Ken
 2    21     Red  Liz, Dan, Leo
 4     30    White  Sue, Tim, Una

The program contains a function:
RaceResults( entries )
which performs the entire task described above, where ‘entries’ is the name of the input file (the registration data). 

The program contains helper functions as well...
