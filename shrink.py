import random


import random

with open('C:\\Users\\harol\\Desktop\\Advanced Deep Learning Pper\\sentence_length.txt') as f:
    lines = list(f)
with open('C:\\Users\\harol\\Desktop\\Advanced Deep Learning Pper\\sentence_length_small.txt', "w") as f:

    for i in range(500):
        f.write(random.choice(lines))
