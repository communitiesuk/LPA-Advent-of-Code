with open('input_jac.txt') as f:
    data = [d.strip() for d in f.readlines()]
    
graph = {d.split(":")[0]: d.split(":")[1].split(" ")[1:] for d in data}

def count_paths(current, finish, graph):
    if current == finish:
        return 1
    neighbours = graph[current]
    if not neighbours:
        return 0
    result = 0
    for neighbour in neighbours:
        result += count_paths(neighbour, "out", graph)
    return result

def count_paths_via(graph, current, finish, has_dac=False, has_fft=False, memo=None):
    if memo is None:
        memo = {}

    if current == "dac":
        has_dac = True
    if current == "fft":
        has_fft = True

    if current == finish:
        return 1 if has_dac and has_fft else 0

    state = (current, has_dac, has_fft)
    if state in memo:
        return memo[state]

    total_paths = 0
    for neighbour in graph.get(current, []):
        total_paths += count_paths_via(graph, neighbour, finish, has_dac, has_fft, memo)

    memo[state] = total_paths
    return total_paths

print(count_paths("you", "out", graph))
print(count_paths_via(graph, "svr", "out"))