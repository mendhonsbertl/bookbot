from stats import (
    get_num_words,
    chars_dict_to_sorted_list,
    get_chars_dict,
)
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        num_words = get_num_words(text)
        sorted_chars = chars_dict_to_sorted_list(text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for i in sorted_chars:
            if i["char"].isalpha():
                print(f"{i['char']}: {i['num']}")
        print("--------- End Report -------")




def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
main()