## Kipland Melton | boot.dev | 7/7/24

def get_words(text):
    words = text.split()
    return len(words)

def get_book(path):
    with open(path) as f:
        return f.read()

def main():
    path_to_file = 'books/frankenstein.txt'
    text = get_book(path_to_file)
    words = get_words(text)

    print(f"{words} words in given file")

main()