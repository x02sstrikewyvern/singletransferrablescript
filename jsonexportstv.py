import json
SEATS = 4

candidates = ["a", "b", "c", "d", "e", "f"]

file = open("votes.json", "r")
inputBallots = json.loads(file.readline())
file.close()

ballots = inputBallots.copy()

candidateVotes = {}
for i in candidates:
    candidateVotes[i] = 0

quota = len(ballots) // len(candidates)
elected = []
currentVotes = []
emptyBallots = 0

quotaNotReached = False
while len(elected) < SEATS:
    for i in ballots:
        try:
            currentVotes.append(i[0])
        except:
            emptyBallots += 1
    if len(ballots) == emptyBallots:
        quotaNotReached = True
        break

    for i in candidates:
        candidateVotes[i] = 0
    for i in currentVotes:
        candidateVotes[i] += 1
    
    highestCandidate = max(candidateVotes, key=candidateVotes.get)
    if candidateVotes[highestCandidate] > quota:
        # elect candidate
        
        elected.append(highestCandidate)

        # transfer vote after election, prepared for next round
        
        for i in ballots:
            if highestCandidate in i:
                i.remove(highestCandidate)

    else:
        # there are no votes to transfer, eliminate least popular candidate and transfer their votes (next round)
        lowestCandidate = min(candidateVotes, key=candidateVotes.get)
        for i in ballots:
            if lowestCandidate in i:
                i.remove(lowestCandidate)
else:
    if quotaNotReached:
        while len(elected) < SEATS:
            highestCandidate = max(candidateVotes, key=candidateVotes.get)
            # elect candidate
            
            elected.append(highestCandidate)

            # transfer vote after election, prepared for next round
            
            for i in ballots:
                if highestCandidate in i:
                    i.remove(highestCandidate)

file = open("seats.json", "w")
file.write(json.dumps(elected))
file.close()
