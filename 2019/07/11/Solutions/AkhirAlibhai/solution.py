import copy

def list_permutations(elements):
    if len(elements) == 1:
        return [list(elements)]

    permutations = []
    for element in elements:
        curr_elements = copy.deepcopy(elements)
        curr_elements.remove(element)

        rest_of_permutation = list_permutations(curr_elements)

        for permutation in rest_of_permutation:
                permutations.append([element] + permutation)
        
    return permutations