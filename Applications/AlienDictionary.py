from collections import defaultdict, deque


def alien_letter_order(words):
    graph = create_graph(words)
    return topological_sort(graph)


def create_graph(words):
    letters = set("".join(words))
    graph = {letter: set() for letter in letters}

    for pair in zip(words, words[1:]):
        # Unpack each pair of adjacent words.
        for before, after in zip(*pair):
            if before != after:
                graph[after].add(before)
                break

    return graph


def topological_sort(graph):
    # Start off our to-do list with all letters without prerequisites.
    todo = deque([letter for letter, previous in graph.items() if not previous])

    # Create a new data structure to map letters to successor letters.
    letter_to_next = defaultdict(list)
    for letter, prevs in graph.items():
        for prev in prevs:
            letter_to_next[prev].append(letter)

    result = []
    while todo:
        letter = todo.popleft()
        result.append(letter)

        # Remove this prerequisite from all successor letters.
        # If any letter now does not have any prerequisites, add it to todo.
        for n in letter_to_next[letter]:
            graph[n].remove(letter)
            if not graph[n]:
                todo.append(n)

    return result if len(result) == len(graph) else None
