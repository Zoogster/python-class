team_a_score = 0
team_b_score = 0
for i in range(4):
    team_a_quarter_score = int(input('Enter Team A score in this quarter: '))
    team_a_score = team_a_quarter_score + team_a_score
    print('Team A score so far: ', team_a_score)
    team_b_quarter_score = int(input('Enter Team B score in this quarter: '))
    team_b_score = team_b_quarter_score + team_b_score
    print('Team B score so far: ', team_b_score)
if team_a_score > team_b_score:
    print('Team A has won')
elif team_a_score < team_b_score:
    print('Team B has won')
else:
    print('It is a tie')
