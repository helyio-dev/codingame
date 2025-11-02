teams = input().split(',')
scores1 = input().split(',')
scores2 = input().split(',')

points = [5, 2, 3, 3]

def parse_scores(score_str):
    res = []
    for s in score_str:
        res.append(list(map(int, s.strip().split()))) if s.strip() else res.append([])
    return res

scores_team1 = parse_scores(scores1)
scores_team2 = parse_scores(scores2)

events = []
for i, score_list in enumerate(scores_team1):
    for t in score_list:
        events.append((t, 0, points[i]))
for i, score_list in enumerate(scores_team2):
    for t in score_list:
        events.append((t, 1, points[i]))

events.sort()
score = [0, 0]
adv_time = [0, 0]
prev_time = 1

for t, team, pts in events:
    duration = t - prev_time
    if score[0] > score[1]:
        adv_time[0] += duration
    elif score[1] > score[0]:
        adv_time[1] += duration
    score[team] += pts
    prev_time = t

duration = 81 - prev_time
if score[0] > score[1]:
    adv_time[0] += duration
elif score[1] > score[0]:
    adv_time[1] += duration

print(f"{teams[0]}: {score[0]} {adv_time[0]}")
print(f"{teams[1]}: {score[1]} {adv_time[1]}")
