import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="name of input file")
args = parser.parse_args()

plan_matches = {} #A dictionary which has as key the day and as value
                  #the matches of the day
players = {} #A dictionary which has as key the day and as value the players
             # of the day
players[0] = []

with open(args.filename) as file:
    matches = []
    for line in file:
        line = line.rstrip()
        line = line.split(' ')
        player1 = line[0]
        player2 = line[1]
        tempMatch =  [player1,player2]
        tempMatch.sort()
        matches.append(tempMatch)
        day = 0
        ok = False #this variable is False until the match[i] find a day
        while ok == False :
            if (player1 not in players[day] and player2 not in players[day]):
                if day in plan_matches.keys():
                     plan_matches[day].append(tempMatch)
                else:
                      plan_matches[day] = [tempMatch]
                ok = True
                players[day].append(player1)
                players[day].append(player2)
            else:
                day = day + 1
                if day not in players.keys():
                    players[day] = []

####sort the matches alphabetically####
matches.sort()
#####this method finds the key-day of a match####
def find_value(match):
    for k,v in plan_matches.items():
        lengthOfValues = len(plan_matches[k])
        for v in range(lengthOfValues):
            if match ==  plan_matches[k][v]:
                return k

###print the solution####
for i in range(len(matches)):
    key = find_value(matches[i])
    print ('(' + matches[i][0] + ',', matches[i][1] + ')' , key)
