## Kipland Melton | boot.dev | 7/7/24

def get_num_of_char(text):

    char_dict = {}
    chars_list = []

    for char in text:
        chars_list.append(char.lower())

    for char in chars_list:
        if char not in char_dict:
            char_dict[char] = 0
        if char in char_dict:
            char_dict[char] += 1

    print(char_dict)

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
    num_chars = get_num_of_char(text)


    # print(f"{text}")
    print(f"{words} words in given file")
    print(num_chars)

main()