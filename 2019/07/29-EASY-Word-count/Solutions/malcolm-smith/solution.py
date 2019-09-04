string = str.lower('Blue hair, blue tie, hiding in your wi-fi')
search = ('blue', 'red', 'wi-fi')


def wordCount(string, search):
    output = {}
    for word in search:
        output[word] = str.count(string, word)

    return output


print(wordCount(string, search))
