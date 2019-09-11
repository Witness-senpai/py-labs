letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
path_allBook = "lab1/allBook.txt"
path_partBook = "lab1/partBook.txt"

#Частота букв
def letters_freq(path_in, path_out):
    lfreq = {letter: 0 for letter in letters}

    with open(path_in) as f:
        text = f.read()
        for letter in text:
            if (letter.lower() in letters):
                lfreq[letter.lower()] += 1

    sort_lfreq = sorted(lfreq.items(), key=lambda key: key[1], reverse=True) 
    with open(path_out, 'w')as f:
        for el in sort_lfreq:
            f.write(str(el) + "\n")
    
#Частота биграмм
def bigrams_freq(path_in, path_out):
    bifreq = {i + j: 0 for i in letters for j in letters}

    with open(path_in) as f:
        text = f.read()
        for i in range(len(text) - 1):
            bigram = (text[i] + text[i+1]).lower()
            if (bigram in bifreq.keys()):
                bifreq[bigram] += 1

    sort_bifreq = sorted(bifreq.items(), key=lambda key: key[1], reverse=True)
    with open(path_out, 'w') as f:
        for el in sort_bifreq:
            f.write(str(el) + "\n")

#Частотый анализ по буквам и биграммам в исходном тексте всей книги
letters_freq(path_allBook, "lab1/letters_freq_all.txt")
bigrams_freq(path_allBook, "lab1/bigrams_freq_all.txt")

#Частотный анализ по буквам и биграммам в части исходного текста книги
letters_freq(path_partBook, "lab1/letters_freq_part.txt")
bigrams_freq(path_partBook, "lab1/bigrams_freq_part.txt")
