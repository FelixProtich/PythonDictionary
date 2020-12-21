counts = dict()
names = ['chen', 'chev', 'chen', 'zia', 'cev']
for name in names:
    counts[name] = counts.get(name, 0)+1
    print('counts', counts)

