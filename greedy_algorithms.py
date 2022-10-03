states_arr = ['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az']
states_needed = set(states_arr)

kone = ['id', 'nv', 'ut']
ktwo = ['wa', 'id', 'mt']
kthree = ['or', 'nv', 'ca']
kfour = ['nv', 'ut']
kfive = ['ca', 'az']

stations = dict()
stations['kone'] = set(kone)
stations['ktwo'] = set(ktwo)
stations['kthree'] = set(kthree)
stations['kfour'] = set(kfour)
stations['kfive'] = set(kfive)

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
print(final_stations)