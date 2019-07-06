def length_longest_consecutive_elements(array):
    element_dict = {}
    largest_value = 0
    plus_one = False

    for element in array:
        # Incase we have duplicates in the array
        if not element_dict.get(element):
            # Length of sequence from element is 1
            element_dict[element] = 1

            # If we have found a sequence for (element + 1)
            if element_dict.get(element + 1):
                # Making sure both the beginning and end have the same length 
                element_dict[element] += element_dict[element + element_dict[element + 1]]
                plus_one = True

            # If we have found a sequence for (element - 1)
            if element_dict.get(element - 1):
                # Making sure both the beginning and end have the same length 
                element_dict[element] += element_dict[element - element_dict[element - 1]]
                element_dict[element - element_dict[element - 1]] = element_dict[element]
                
            # So we dont have to set the end of the sequence's value twice
            if plus_one:
                element_dict[element + element_dict[element + 1]] = element_dict[element]                
                plus_one = False

            # If our new value is larger than our previous largest
            if element_dict[element] > largest_value:
                largest_value = element_dict[element]

    return largest_value