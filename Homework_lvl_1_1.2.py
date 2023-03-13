# 1.2
# Пункт А.

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

import random
result = sum([x[1] for x in random.sample(my_favorite_songs, 3,)])

print('Пункт А: Три песни звучат', int(result), 'минут')

# # Пункт В.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

import random
songs = list(my_favorite_songs_dict.values())
res = sum(random.sample(songs, 3))
print('Пункт В: Три песни звучат', int(res), 'минут')

# Пункт С/A

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
import random
songs = [*my_favorite_songs[0], *my_favorite_songs[1], *my_favorite_songs[2], *my_favorite_songs[3], *my_favorite_songs[4], *my_favorite_songs[5], *my_favorite_songs[6], *my_favorite_songs[7], *my_favorite_songs[8],]
del songs[::-2]
print('Пункт С/A. Случайные песни:', random.sample(songs, 3))

# Пункт С/B

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

import random
songs = list(my_favorite_songs_dict.keys())
print('Пункт С/B. Случайные песни:', random.sample(songs, 3))


# Пункт D

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]


import datetime
from math import *
numb = [i[1] for i in my_favorite_songs]
sng = [i[0] for i in my_favorite_songs]

n1 = 3.03
min = int(floor(n1))
sec = int(n1 * 100 % 100)
res1 = (datetime.time(00, min, sec).strftime(('%M:%S')))
n2 = 4.02
min = int(floor(n2))
sec = int(n2 * 100 % 100)
res2 = (datetime.time(00, min, sec).strftime(('%M:%S')))
n3 = 3.40
min = int(floor(n3))
sec = int(n3 * 100 % 100)
res3 = (datetime.time(00, min, sec).strftime(('%M:%S')))
n4 = 3.03
min = int(floor(n4))
sec = int(n4 * 100 % 100)
res4 = (datetime.time(00, min, sec).strftime(('%M:%S')))
n5 = 5.28
min = int(floor(n5))
sec = int(n5 * 100 % 100)
res5 = (datetime.time(00, min, sec).strftime(('%M:%S')))
n6 = 4.15
min = int(floor(n6))
sec = int(n6 * 100 % 100)
res6 = (datetime.time(00, min, sec).strftime(('%M:%S')))
n7 = 4.04
min = int(floor(n7))
sec = int(n7 * 100 % 100)
res7 = (datetime.time(00, min, sec).strftime(('%M:%S')))
n8 = 2.58
min = int(floor(n8))
sec = int(n8 * 100 % 100)
res8 = (datetime.time(00, min, sec).strftime(('%M:%S')))
n9 = 4.02
min = int(floor(n9))
sec = int(n9 * 100 % 100)
res9 = (datetime.time(00, min, sec).strftime(('%M:%S')))

my_favorite_songs = []
my_favorite_songs.append([sng[0], res1])
my_favorite_songs.append([sng[1], res2])
my_favorite_songs.append([sng[2], res3])
my_favorite_songs.append([sng[3], res4])
my_favorite_songs.append([sng[4], res5])
my_favorite_songs.append([sng[5], res6])
my_favorite_songs.append([sng[6], res7])
my_favorite_songs.append([sng[7], res8])
my_favorite_songs.append([sng[8], res9])

print('Пункт D:', my_favorite_songs)




# Пункт А: Три песни звучат 11 минут
# Пункт В: Три песни звучат 12 минут
# Пункт С/A. Случайные песни: ['Easy', 'Nowhere to Run', 'A Sorta Fairytale']
# Пункт С/B. Случайные песни: ["Staying' Alive", 'Easy', 'New Salvation']
# Пункт D: [['Waste a Moment', '03:03'], ['New Salvation', '04:01'], ["Staying' Alive", '03:40'], ['Out of Touch', '03:03'], ['A Sorta Fairytale', '05:28'], ['Easy', '04:15'], ['Beautiful Day', '04:04'], ['Nowhere to Run', '02:58'], ['In This World', '04:01']]
