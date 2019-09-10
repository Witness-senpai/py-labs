letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
freq = {letter: 0 for letter in letters}

with open("lab1/orig.txt", encoding='windows-1251') as f:
    text = f.read()
    for letter in text:
        if (letter.lower() in letters):
            freq[letter.lower()] += 1

sort_freq = sorted(freq.items(), key=lambda key: key[1], reverse=True) 

for el in sort_freq:
    print(el)