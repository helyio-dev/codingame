gymnasts = input().split(',')
categories = input().split(',')
n = int(input())

records = {}
for _ in range(n):
    data = input().split(',')
    name = data[0]
    bars = float(data[1])
    beam = float(data[2])
    floor = float(data[3])
    
    if name not in records:
        records[name] = {'bars': -1, 'beam': -1, 'floor': -1}
    
    records[name]['bars'] = max(records[name]['bars'], bars)
    records[name]['beam'] = max(records[name]['beam'], beam) 
    records[name]['floor'] = max(records[name]['floor'], floor)

for gymnast in gymnasts:
    output = []
    for category in categories:
        score = records[gymnast][category]
        if score == int(score):
            output.append(str(int(score)))
        else:
            output.append(str(score))
    print(','.join(output))