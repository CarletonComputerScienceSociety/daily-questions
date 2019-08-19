input = [
    ('Mamma Mia', ['ABBA']),
    ('Ghost Rule', ['DECO*27', 'Hatsune Miku']),
    ('Animals', ['Martin Garrix']),
    ('Remember The Name', ['Ed Sheeran', 'Eminem', '50 Cent']),
    ('404 Not Found', [])
]


def songTitle(song):
    artists = ''
    if len(song[1]) > 1:
        for artist in range(len(song[1])):
            artists += (song[1][artist] + ', ')
        artists += ('and ' + song[1][-1] + ' - ')
    elif len(song[1]) == 1:
        artists = song[1][0] + ' - '
    else:
        artists = ''

    return artists + song[0]


for song in input:
    print(songTitle(song))
