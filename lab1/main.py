alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
bifreq = {i + j: 0 for i in alphabet for j in alphabet} #все возможные биграммы

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
    
    return sort_lfreq
    
#Частота биграмм
def bigrams_freq(path_in, path_out):
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
    
    return sort_bifreq

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

def findIndex(sequence, el):
    for i in range(len(sequence)):
        if sequence[i][0] == el:
            return i

def decode_by_letters(path_in, path_out, freq_all, freq_part):
    all_text = ''
    with open(path_in, 'r') as fin:
        all_text = fin.read()
    
    with open(path_out, 'w') as fout:
        for letter in all_text:
            decode_letter = letter
            if letter.lower() in alphabet:
                if letter.islower():
                    decode_letter = freq_all[findIndex(freq_part, letter.lower())][0]
                else:
                    decode_letter = freq_all[findIndex(freq_part, letter.lower())][0].upper()
            fout.write(decode_letter)

def decode_by_bigrams(path_in, path_out, freq_all, freq_part):
    all_text = ''
    with open(path_in, 'r') as fin:
        all_text = fin.read()
    
    with open(path_out, 'w') as fout:
        for i in range(len(all_text) - 1):
            decode_bigram = all_text[i] + all_text[i+1]
            if decode_bigram[0].lower() in alphabet and \
               decode_bigram[1].lower() in alphabet:
                if decode_bigram.islower():
                    decode_bigram = freq_all[findIndex(freq_part, decode_bigram.lower())][0]
                elif decode_bigram[0].isupper() and decode_bigram[0].islower():
                    decode_bigram = freq_all[findIndex(freq_part, decode_bigram.lower())][0]
                    decode_bigram = decode_bigram[0].upper() + decode_bigram[1]
                else:
                    decode_bigram = freq_all[findIndex(freq_part, decode_bigram.lower())][0].upper()
            fout.write(decode_bigram)

#Частотый анализ по буквам и биграммам в исходном тексте всей книги
lFreq_all = letters_freq(path_allBook, "lab1/letters_freq_all.txt")
biFreq_all = bigrams_freq(path_allBook, "lab1/bigrams_freq_all.txt")

#Зашифровка шифром Цезаря части исходного текста книги
cesar_encode(path_partBook, "lab1/partBook_encode.txt", 3)

#Частотный анализ по буквам и биграммам зашифрованной части текста книги
lFreq_part = letters_freq("lab1/partBook_encode.txt", "lab1/letters_freq_encode.txt")
biFreq_part = bigrams_freq("lab1/partBook_encode.txt", "lab1/bigrams_freq_encode.txt")

#Расшифрока части книги на основе частотного анализа букв во всей книге
decode_by_letters("lab1/partBook_encode.txt", "lab1/partBook_decode_letters.txt", lFreq_all, lFreq_part)

#Расшифровка на оcнове биграмм
decode_by_bigrams("lab1/partBook_encode.txt", "lab1/partBook_decode_bigrams.txt", biFreq_all, biFreq_part)

