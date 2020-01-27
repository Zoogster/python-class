print("Please enter Jean's scores one by one.")
j_list = []
for i in range(4):
    score = float(input('Enter a score: '))
    j_list.append(score)
print("Jean's scores: ", j_list)
k_list = []
print("Please enter Kayla's scores one by one.")
for i in range(4):
    score = float(input('Enter a score: '))
    k_list.append(score)
print("Kayla's scores: ", k_list)
c_list = []
print("Please enter Connie's scores one by one.")
for i in range(4):
    score = float(input('Enter a score: '))
    c_list.append(score)
print("Connie's scores: ", c_list)
all_scores = [j_list[:], k_list[:], c_list[:]]
print('All scores: ', all_scores)
for i in range(3):
    for y in range(4):
        all_scores[i][y] = all_scores[i][y] + 1
print('All scores after extra point: ', all_scores)
for i in range(3):
    all_scores[i].sort()
print('All scores after sorting: ', all_scores)
