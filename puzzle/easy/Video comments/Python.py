n = int(input())
lines = [input() for _ in range(n)]
comments = []

for idx, line in enumerate(lines):
    reply = line.startswith("    ")
    data = line[4:] if reply else line
    name, date, likes, priority = data.split('|')
    comments.append({
        'orig': line,
        'name': name,
        'date': date,
        'likes': int(likes),
        'priority': priority,
        'reply': reply,
        'index': idx
    })

top_level = []
reply_map = {}

current_top = None
for c in comments:
    if not c['reply']:
        top_level.append(c)
        current_top = c['index']
        reply_map[current_top] = []
    else:
        reply_map[current_top].append(c)

def sort_key(c):
    if c['priority'] == 'Pinned':
        p = 0
    elif c['priority'] == 'Followed':
        p = 1
    else:
        p = 2
    return (p, -c['likes'], -int(c['date'].replace(':','')), c['index'])

sorted_top = sorted(top_level, key=sort_key)

output = []
for c in sorted_top:
    output.append(c['orig'])
    replies = reply_map[c['index']]
    sorted_replies = sorted(replies, key=sort_key)
    output.extend([r['orig'] for r in sorted_replies])

for line in output:
    print(line)
