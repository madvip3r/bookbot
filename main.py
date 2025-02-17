def main():
    book_path = "books/frankenstein.txt"
    text = readBook(book_path)
    num_words = wordCoun(text)
    #print(f"{num_words} words found in document")
    characters = characterCount(text)
    print(characters)

def characterCount(text):
    lower_text = text.lower()
    freq = {}
    for c in set(lower_text):
        freq[c] = text.count(c)
    return freq

def wordCoun(text):
    words = text.split()
    return len(words)

def readBook(path):
    with open(path) as f:
        return f.read()

main()