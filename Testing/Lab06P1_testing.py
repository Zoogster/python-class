orignal_scores = []
for i in range(5):
    score = float(input('Enter a test score: '))
    orignal_scores.append(score)
print('All scores:', orignal_scores)
new_scores = orignal_scores[:]
for i in range(5):
    if i < 60:
        new_scores[i] = new_scores[i] + 10
print(new_scores)
