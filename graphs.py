from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


def search(graph, name='you'):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                if graph[person]:
                    search_queue += graph[person]
                searched.append(person)
    return False


my_graph = dict()
my_graph['you'] = ['Marlin', 'Hloe', "Mark"]
my_graph['Marlin'] = []
my_graph['Hloe'] = ['Mackm']
my_graph['Mark'] = []
my_graph['Mackm'] = []


print(search(my_graph))
