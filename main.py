import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_num_words, get_char_count, sorts_dict_to_list

def get_book_text(filepath):
    book_content = ""
    with open(filepath) as f:
        book_content = f.read()
    return book_content


def main():

    book1 = get_book_text(sys.argv[1])
    char_count_in_book = get_char_count(book1)
    sorted_book_list = sorts_dict_to_list(char_count_in_book)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book1)} total words")
    print("--------- Character Count -------")
    for char_and_count in sorted_book_list:
        if char_and_count["char"].isalpha() == False:
            continue
        else:
            print(f"{char_and_count["char"]}: {char_and_count["num"]}")

    print("============= END ===============")

main()

