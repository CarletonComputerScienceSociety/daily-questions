
class Node:
    def __init__(self, letter):
        self.letter = letter
        self.neighbors = set()

    def search(self, word, path='', visited=set()):
        visited = visited | {self}
        path += self.letter
        if path == word:
            return True
        if path == word[:len(path)]:
            unvisited = self.neighbors - visited
            return True in [n.search(word, path, visited) for n in unvisited]
        return False


def word_search(grid, word):
    return True in [node.search(word) for node in grid_to_graph(grid)]


def grid_to_graph(grid):
    nodes = [[Node(letter) for letter in row] for row in grid]

    for row in range(0, len(nodes)):
        for col in range(0, len(nodes[row])):
            if row > 0:
                nodes[row][col].neighbors.add(nodes[row-1][col])
            if row < len(nodes) - 1:
                nodes[row][col].neighbors.add(nodes[row+1][col])
            if col > 0:
                nodes[row][col].neighbors.add(nodes[row][col-1])
            if col < len(nodes[row]) - 1:
                nodes[row][col].neighbors.add(nodes[row][col+1])

    return [node for row in nodes for node in row]


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

print(word_search(board, 'ABCCED'))
print(word_search(board, 'SEE'))
print(word_search(board, 'ABCB'))
