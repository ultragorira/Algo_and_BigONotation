competitions= [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ]
results = [0, 0, 1]


def tournamentWinner(competitions, results):

	final_results = [0 for _ in competitions]
	for match_id in range(len(competitions)):
		teams = competitions[match_id]
		result = results[match_id]
		if (result == 1):
			final_results[match_id] = teams[0]
		else:
			final_results[match_id] = teams[1]
			
			
	return max(final_results,key=final_results.count)


#O(n) Time, O(k) Space => For the Map

HOME_TEAM_WON = 1

def tournamentWinner_2(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam:0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        home_team, away_team = competition

        winningTeam = home_team if result == HOME_TEAM_WON else away_team

        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam

def updateScores(team, points, scores):

    if team not in scores:
        scores[team] = 0

    scores[team] +=points

tournamentWinner_2(competitions, results)