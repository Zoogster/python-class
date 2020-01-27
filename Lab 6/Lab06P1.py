orignal_scores = []
for i in range(5):
    score = int(input('Enter a test score: '))
    orignal_scores.append(score)
print('All scores:', orignal_scores)
new_scores = orignal_scores[:]
for i in range(5):
    if new_scores[i] < 60:
        new_scores[i] = new_scores[i] + 10
    else:
        new_scores[i] = new_scores[i]
print(new_scores)
