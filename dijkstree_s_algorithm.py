from math import inf

graph = dict()  # Создаёт граф в котором будут описаны все соединения, и их стоимость.
graph['start'] = dict()  # Создаёт хэш-таблицу, в которой будут соединения между стартом и связанными с ним точками.
graph['start']['a'] = 6  # Указывает, что вес между стартом и точкой A - 6.
graph['start']['b'] = 2  # Указывает, что вес между стартом и точкой B - 2.
graph['a'] = dict()  # Хеш-таблица, в которой будут описаны все соединения между А и точками связанными с ним.
graph['a']['fin'] = 1  # Вес между А и концом - 1.
graph['b'] = dict()  # Хэщ-таблица, в которой будут описаны все соединения между B и точками связанными с ним.
graph['b']['a'] = 3  # Вес между B и A - 3.
graph['b']['fin'] = 5  # Вес между B и концом - 5.
graph['fin'] = dict()  # Пустая хещ-таблица, которая означает крайнюю точку.

infinity = inf  # Переменная которая содержит значение бесконечности.
costs = dict()  # Хэщ-таблица, в которой хранятся все минимальные веса к каждой точке.
costs['a'] = graph['start']['a']  # Цена самого дешевого пути к А.
costs['b'] = graph['start']['b']  # Цена самого дешевого пути к B.
costs['fin'] = infinity  # Цена самого дешевого пути к концу, а так как он в начале не известен, значит = бесконечности.

parents = dict()  # Хэш-таблица, которая содержит родителей каждой из точки, поможет в вычислении самого легкого пути.
parents['a'] = 'start'  # Родителем для точки А в начале является стартовая точка.
parents['b'] = 'start'  # Родителем для точки B в начале является стартовая точка.
parents['fin'] = None  # Так как у конечной точки в начале нет родителя, мы присваиваем ей значение None.

processed = []  # Список в котором будут находиться все уже обработанные узлы.


def find_lowest_cost_node(costs):
    """Находит узел с наименьшим весом."""
    lowest_cost = inf  # По стандарту меньший узел равен бесконечности.
    lowest_cost_node = None  # В начале узел с наименьшим весом неизвестен.
    for node in costs:  # Перебирает все узлы из таблицы с ценами.
        cost = costs[node]  # Определяется цена нынешнего узла.
        if cost < lowest_cost and node not in processed:  # Если цена на данный момент меньше менимальной и узел ещё не был обработан.
            lowest_cost = cost  # Обновляется минимальная цена на текущую.
            lowest_cost_node = node  # Определяется новый узел с самым меньшим весом.
    return lowest_cost_node  # Возвращается узел с самой меньшей ценой.


node = find_lowest_cost_node(costs)  # Находит узел с наименьшей стоимостью.
while node is not None:  # Пока существуют еще узлы, которые не были обработаны.
    cost = costs[node]  # Определяет цену обрабатываемой цепи.
    neighbors = graph[node]  # Список содержащий всех соседей данного узла.
    for n in neighbors.keys():  # Перебирает все значения соседей используемого узла.
        new_cost = cost + neighbors[n]  # Определяет новую цену для каждого узла.
        if costs[n] > new_cost:  # Если старая цена больше новой.
            costs[n] = new_cost  # Новая цена заносится в значении хэш=таблицы с ценами.
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

fin = ['fin']
node1 = 'fin'
while node1 != 'start':
    node1 = parents[node1]
    fin.append(node1)

print(fin)
