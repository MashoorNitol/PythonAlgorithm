home_team_won = 1
def tournamentWinner(competitions, results):
  bestTeam = ""
  scores = {bestTeam: 0}
  for idx, competition in enumerate(competitions):
    result = results[idx]
    homeTeam, awayTeam = competition
    winingTeam = homeTeam if result == home_team_won else awayTeam
    updateScores(winingTeam,3,scores)
    if scores[winingTeam] > scores[bestTeam]:
      bestTeam = winingTeam
  return bestTeam

def updateScores(team, points, scores):
  if team not in scores:
    scores[team] = 0
  
  scores[team] += points
  
