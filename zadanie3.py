def muliply_word(word,sentence):
    iter_word = iter((word*round(len(sentence)/len(word)))[:len(sentence)])
    return "".join(next(iter_word)if sentence[i].isalnum() else sentence[i]
                for i in range(len(sentence)))
def vigenere_cipher(word, sentence):
    longer_word = muliply_word(word, sentence)
    return "".join(chr(((ord(elem)-65+ord(element)-65)%26)+65) if element.isalpha()  else element for (elem,element) in zip(longer_word.upper(),sentence.upper()))

print(vigenere_cipher("TAJNE","TO JEST BARDZO TAJNY TEKST"))