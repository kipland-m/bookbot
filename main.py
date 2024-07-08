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

    return char_dict

def sort_on(dict):
    return dict["occurence"]

def create_list_of_dicts(char_dict):
    char_dicts = []

    for char, occurs in char_dict.items():
        if char.isalpha():
            new_dict = {"character": char, "occurence": occurs}
            char_dicts.append(new_dict)
        else:
            continue

    char_dicts.sort(reverse=True, key=sort_on)
    return char_dicts

def display_report(dict):
    for item in dict:
        print(f"The {item["character"]} char was found {item["occurence"]} times.")
    

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
    list_of_dicts = create_list_of_dicts(num_chars)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words in given file\n")
    print(display_report(list_of_dicts))
    
main()