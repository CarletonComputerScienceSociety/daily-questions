class WinLoseNode():
    '''
        Returns a tuple of the first element to lose to
        the given node, and an array of all other nodes
        that the given node beat
    '''

    def get_biggest_losers(self):
        losers = []
        prev_winner = None
        curr_winner = self

        while True:
            if isinstance(curr_winner, int) or not curr_winner.loser:
                return (prev_winner.loser, losers[:-1])

            prev_winner = curr_winner
            curr_winner = curr_winner.winner
            losers.append(prev_winner.loser)

    def __init__(self, value, winner, loser):
        self.value = value
        self.winner = winner
        self.loser = loser


def get_value(maybe_node):
    '''
        Returns the integer value of the input
    '''
    if isinstance(maybe_node, int):
        return maybe_node
    else:
        return maybe_node.value


def get_kth_largest(array, k):
    old_win_lose_nodes = []
    curr_win_lose_nodes = []

    # Initial loop to create the nodes
    for i in range(0, len(array), 2):
        try:
            if array[i] > array[i+1]:
                curr_win_lose_nodes.append(WinLoseNode(
                    array[i], array[i], array[i+1]))
            else:
                curr_win_lose_nodes.append(WinLoseNode(
                    array[i+1], array[i+1], array[i]))
        except IndexError:
            curr_win_lose_nodes.append(WinLoseNode(array[i], array[i], None))

    # Finding the biggest element
    while True:
        old_win_lose_nodes = curr_win_lose_nodes
        curr_win_lose_nodes = []

        # If we have found the biggest element
        if len(old_win_lose_nodes) == 1:
            break

        for i in range(0, len(old_win_lose_nodes), 2):
            try:
                if get_value(old_win_lose_nodes[i]) > get_value(old_win_lose_nodes[i+1]):
                    curr_win_lose_nodes.append(WinLoseNode(get_value(old_win_lose_nodes[i]),
                                                           old_win_lose_nodes[i], old_win_lose_nodes[i+1]))
                else:
                    curr_win_lose_nodes.append(WinLoseNode(get_value(old_win_lose_nodes[i+1]),
                                                           old_win_lose_nodes[i+1], old_win_lose_nodes[i]))
            except IndexError:
                curr_win_lose_nodes.append(WinLoseNode(get_value(old_win_lose_nodes[i]),
                                                       old_win_lose_nodes[i], None))

    smallest_loser = None

    # To find the kth largest element
    for i in range(0, k-1):
        # Refer to the comments for the function
        biggest_losers = old_win_lose_nodes[0].get_biggest_losers()
        smallest_loser = biggest_losers[0]

        for loser in biggest_losers[1]:
            if get_value(smallest_loser) > get_value(loser):
                smallest_loser = WinLoseNode(
                    get_value(smallest_loser), smallest_loser, loser)
            else:
                smallest_loser = WinLoseNode(
                    get_value(loser), loser, smallest_loser)

        old_win_lose_nodes[0] = smallest_loser

    return get_value(old_win_lose_nodes[0])
