def main():
    book_path = "books/frankenstein.txt"
    text = readBook(book_path)
    num_words = wordCoun(text)
    #print(f"{num_words} words found in document")
    characters = characterCount(text)
    filtered_dict = {key: value for key, value in characters.items() if key.isalpha()}
    sorted_dict = sorted(filtered_dict.items(), key=lambda item: item[1], reverse=True)
    for key, value in sorted_dict:
        print(f"The '{key}' character was found {value} times")

def characterCount(text):
    counter = {}
    for c in text:
        lowered = c.lower()
        if lowered in counter:
            counter[lowered] += 1
        else:
            counter[lowered] = 1
    return counter

def wordCoun(text):
    words = text.split()
    return len(words)

def readBook(path):
    with open(path) as f:
        return f.read()

main()