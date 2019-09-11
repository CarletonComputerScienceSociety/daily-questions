def mostVowels(words):
    vowels = 0
    vowelCount = 0
    vowelWord = ''
    for word in words:
        vowels = 0
        for character in word:
            if str.lower(character) in {'a', 'e', 'i', 'o', 'u'}:
                vowels += 1
        if vowels > vowelCount:
            vowelWord = word
            vowelCount = vowels
        elif vowels == vowelCount:
            vowelWord = [vowelWord]
            vowelWord.append(word)
    return vowelWord


print(mostVowels(['Pippi', 'Yuzu', 'Maria', 'Mocha']))
print(mostVowels(['Arthur', 'Dutch', 'Bill', 'Javier']))
print(mostVowels(['Jebediah', 'Bill', 'Bob', 'Valentina']))
