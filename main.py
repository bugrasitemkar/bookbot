import sys
from stats import get_num_words, get_char_count, get_sorted_char_count

def get_book_text(path_to_file):
    if path_to_file == None:
        return ''
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    contents = get_book_text(path_to_file)
    print(get_num_words(contents))
    char_counts = get_char_count(contents)
    sorted_chars = get_sorted_char_count(char_counts)

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

main()
