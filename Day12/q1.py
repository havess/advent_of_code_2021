lines = open('input.txt', 'r').read().splitlines()
graph = {}
for line in lines:
    a, b = line.split('-')
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)

paths = []
def search(seen, path, node):
    if node == "end":
        paths.append(path)
        return

    for neigh in graph[node]:
        if neigh.isupper() or neigh not in seen:
            temp = set(seen)
            if neigh.islower():
                seen.add(neigh)
            search(seen, path + [neigh], neigh)
            seen = temp

search({"start"}, ["start"], "start")
print(len(paths))
