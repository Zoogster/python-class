d_won = 0
r_won = 0
for i in range(5):
    people_think_d_won = float(
        input("What percentage of people think Democrat's candidate has won? "))
    people_think_r_won = float(
        input("What percentage of people think Republican's candidate has won? "))
    if people_think_d_won > people_think_r_won+3:
        d_won = 1 + d_won
        print("Democrat's Candidate has won this debate.")
    elif people_think_r_won > people_think_d_won+3:
        r_won = 1 + r_won
        print("Republican's Candidate has won this debate.")
    else:
        print("It is statistically a tie")
print("Number of debates Democrat's candidate has won: ", d_won)
print("Number of debates Republican's candidate has won: ", r_won)
if d_won > r_won:
    print("The Democrate's candidate has won the most debates")
elif r_won > d_won:
    print("The Republican's candidate has won the most debates")
else:
    print("The two candidates have won the same number of debates")
