from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        print(f.read())

def fancy_print_characters(list, filepath):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...\n----------- Word Count ----------")
    print(f"Found {get_word_count(filepath)} total words\n--------- Character Count -------")
    for character in list:
        if character['char'].isalpha():
            print(f"{character['char']}: {character['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
    
    character_count = get_char_count(file)
    character_count_list = dict_splitser(character_count)
    fancy_print_characters(character_count_list, file)

main()