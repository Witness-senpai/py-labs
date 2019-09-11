alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
path_allBook = "lab1/allBook.txt"
path_partBook = "lab1/partBook.txt"

#Частота букв
def letters_freq(path_in, path_out):
    lfreq = {letter: 0 for letter in alphabet}

    with open(path_in) as f:
        text = f.read()
        for letter in text:
            if (letter.lower() in alphabet):
                lfreq[letter.lower()] += 1

    sort_lfreq = sorted(lfreq.items(), key=lambda key: key[1], reverse=True) 
    with open(path_out, 'w')as f:
        for el in sort_lfreq:
            f.write(str(el) + "\n")
    
#Частота биграмм
def bigrams_freq(path_in, path_out):
    bifreq = {i + j: 0 for i in alphabet for j in alphabet}

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

#Зашифровка шифром Цезаря
def cesar_encode(path_in, path_out, key):
    all_text = ''
    with open(path_in, 'r') as fin:
        all_text = fin.read()
    
    with open(path_out, 'w') as fout:
        for letter in all_text:
            encode_letter = letter
            if letter.lower() in alphabet:
                if letter.islower():
                    encode_letter = alphabet[(alphabet.find(letter.lower()) + key) % len(alphabet)]
                else:
                    encode_letter = alphabet[(alphabet.find(letter.lower()) + key) % len(alphabet)].upper()
            fout.write(encode_letter)

#Расшифровка шифра Цезаря
def cesar_decode(path_in, path_out, key):
    all_text = ''
    with open(path_in, 'r') as fin:
        all_text = fin.read()
    
    with open(path_out, 'w') as fout:
        for letter in all_text:
            encode_letter = letter
            if letter.lower() in alphabet:
                if letter.islower():
                    encode_letter = alphabet[(alphabet.find(letter.lower()) - key) % len(alphabet)]
                else:
                    encode_letter = alphabet[(alphabet.find(letter.lower()) - key) % len(alphabet)].upper()
            fout.write(encode_letter)

#Частотый анализ по буквам и биграммам в исходном тексте всей книги
#letters_freq(path_allBook, "lab1/letters_freq_all.txt")
#bigrams_freq(path_allBook, "lab1/bigrams_freq_all.txt")

#Частотный анализ по буквам и биграммам в части исходного текста книги
#letters_freq(path_partBook, "lab1/letters_freq_part.txt")
#bigrams_freq(path_partBook, "lab1/bigrams_freq_part.txt")

#Зашифровка и расшифровка шифром Цезаря части исходного текста книги
cesar_encode(path_partBook, "lab1/partBook_encode.txt", 5)
cesar_decode("lab1/partBook_encode.txt", "lab1/partBook_decode.txt", 5)
